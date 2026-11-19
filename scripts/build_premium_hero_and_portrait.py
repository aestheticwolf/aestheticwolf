import os
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def build_premium_hero_and_portrait():
    print("==================================================")
    print("STARTING PREMIUM HERO & PORTRAIT GENERATION")
    print("==================================================")

    # 1. Load original high-resolution portrait
    orig_path = 'assets/richard-portrait.png'
    assert os.path.exists(orig_path), f"Original portrait not found at {orig_path}"
    orig_im = Image.open(orig_path).convert('RGBA')
    w_orig, h_orig = orig_im.size
    print(f"Original portrait loaded: {w_orig}x{h_orig} RGBA")

    # Crop tightly to non-empty alpha bounding box with 6px padding
    arr_orig = np.array(orig_im, dtype=np.float32)
    alpha_channel = arr_orig[:, :, 3]
    row_mask = (alpha_channel > 5).sum(axis=1) > 0
    col_mask = (alpha_channel > 5).sum(axis=0) > 0
    r_min, r_max = np.where(row_mask)[0][[0, -1]]
    c_min, c_max = np.where(col_mask)[0][[0, -1]]
    r_min = max(0, r_min - 6)
    r_max = min(h_orig - 1, r_max + 6)
    c_min = max(0, c_min - 6)
    c_max = min(w_orig - 1, c_max + 6)

    cropped_arr = arr_orig[r_min:r_max+1, c_min:c_max+1].copy()
    ch, cw, _ = cropped_arr.shape
    print(f"Tightly cropped portrait size: {cw}x{ch}")

    # Lower torso natural alpha fade: bottom 22% smoothly eases to 0
    fade_start = int(ch * 0.78)
    fade_len = ch - fade_start
    t_fade = np.linspace(0.0, 1.0, fade_len, dtype=np.float32)
    fade_curve = 0.5 * (1.0 + np.cos(np.pi * t_fade))

    for y_idx in range(fade_start, ch):
        cropped_arr[y_idx, :, 3] *= fade_curve[y_idx - fade_start]

    # Subtle ambient rim lighting:
    cur_alpha = cropped_arr[:, :, 3] / 255.0
    edge_x = np.zeros_like(cur_alpha)
    edge_x[:, 1:-1] = (cur_alpha[:, 2:] - cur_alpha[:, :-2]) / 2.0
    right_rim = np.clip(-edge_x * 2.5, 0, 1.0) * (cur_alpha > 0.25)
    left_rim = np.clip(edge_x * 2.5, 0, 1.0) * (cur_alpha > 0.25)

    right_rim_blur = np.array(
        Image.fromarray((right_rim * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=2.5)),
        dtype=np.float32
    ) / 255.0
    left_rim_blur = np.array(
        Image.fromarray((left_rim * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=2.5)),
        dtype=np.float32
    ) / 255.0

    # Tint rims subtly
    for c, val in enumerate([34, 211, 238]):  # Cyan
        cropped_arr[:, :, c] = np.clip(cropped_arr[:, :, c] + right_rim_blur * val * 0.14, 0, 255)
    for c, val in enumerate([139, 92, 246]):  # Violet
        cropped_arr[:, :, c] = np.clip(cropped_arr[:, :, c] + left_rim_blur * val * 0.12, 0, 255)

    static_portrait = Image.fromarray(np.clip(cropped_arr, 0, 255).astype(np.uint8), mode='RGBA')
    static_portrait.save('assets/richard-portrait-static.png', format='PNG')
    print("Saved high-resolution assets/richard-portrait-static.png")

    # Target portrait placement in hero:
    # x=640, y=26, width=336, height=378 (120px clearance from left text!)
    pw, ph = 336, 378
    portrait_resized = static_portrait.resize((pw, ph), Image.Resampling.LANCZOS)
    port_arr = np.array(portrait_resized)

    # Base hero canvas (1000x420)
    hero_base = Image.open('scratch/hero_base.png').convert('RGBA')
    bg_color_rgb = (8, 11, 20)

    # Slice into square pixel blocks (8x8)
    block_size = 8
    cx, cy = pw // 2, int(ph * 0.42)

    np.random.seed(2026)
    random.seed(2026)

    blocks = []
    for by in range(0, ph, block_size):
        for bx in range(0, pw, block_size):
            bw = min(block_size, pw - bx)
            bh = min(block_size, ph - by)
            patch = port_arr[by:by+bh, bx:bx+bw]
            alpha_mean = patch[:, :, 3].mean()
            if alpha_mean > 12:
                dx = (bx + bw / 2.0) - cx
                dy = (by + bh / 2.0) - cy
                dist = math.hypot(dx, dy) + 1.0
                nx = dx / dist
                ny = dy / dist

                scatter_dist = random.uniform(70, 190)
                drift_x = random.uniform(-35, 35)
                drift_y = random.uniform(-25, 25)

                accent = None
                if random.random() < 0.16:
                    accent = random.choice([
                        (34, 211, 238, 255),   # Cyan
                        (59, 130, 246, 255),   # Electric Blue
                        (139, 92, 246, 255),   # Violet
                        (245, 245, 247, 255),  # White
                    ])

                blocks.append({
                    'bx': bx, 'by': by, 'bw': bw, 'bh': bh,
                    'patch': patch,
                    'patch_im': Image.fromarray(patch, mode='RGBA'),
                    'sx': nx * scatter_dist + drift_x,
                    'sy': ny * scatter_dist + drift_y,
                    'accent': accent,
                    'rand_delay': random.uniform(0.0, 0.20)
                })

    print(f"Sliced portrait into {len(blocks)} active square pixel blocks.")

    particles = []
    for _ in range(30):
        particles.append({
            'x': random.uniform(15, pw - 15),
            'y': random.uniform(15, ph - 30),
            'vx': random.uniform(-20, 20),
            'vy': random.uniform(-30, -8),
            'size': random.choice([2, 3, 4]),
            'color': random.choice([(34, 211, 238), (139, 92, 246), (59, 130, 246)])
        })

    try:
        font_mono = ImageFont.truetype("consola.ttf", 19)
    except:
        font_mono = ImageFont.load_default()

    roles = [
        "Full-Stack Developer",
        "Software Engineer",
        "React & React Native Developer",
        "AI Application Developer"
    ]

    port_sharp_rgba = portrait_resized.copy()

    def render_portrait_layer(disp_factor, coarseness=1, scan_y=None, particle_alpha=0.0):
        layer = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)

        if disp_factor <= 0.001 and coarseness <= 1:
            layer.paste(port_sharp_rgba, (0, 0), port_sharp_rgba)
        elif disp_factor <= 0.001 and coarseness > 1:
            small_w = max(1, pw // coarseness)
            small_h = max(1, ph // coarseness)
            pix = portrait_resized.resize((small_w, small_h), Image.Resampling.BOX).resize((pw, ph), Image.Resampling.NEAREST)
            layer.paste(pix, (0, 0), pix)
        else:
            for b in blocks:
                eff_disp = max(0.0, min(1.0, disp_factor + (b['rand_delay'] - 0.10) * disp_factor))
                cur_x = int(b['bx'] + b['sx'] * eff_disp)
                cur_y = int(b['by'] + b['sy'] * eff_disp)

                if -block_size < cur_x < pw and -block_size < cur_y < ph:
                    patch = b['patch_im']
                    if eff_disp > 0.1:
                        pa = np.array(patch)
                        alpha_scale = max(0.25, 1.0 - 0.45 * eff_disp)
                        pa[:, :, 3] = (pa[:, :, 3] * alpha_scale).astype(np.uint8)
                        patch = Image.fromarray(pa, mode='RGBA')
                    layer.paste(patch, (cur_x, cur_y), patch)

                    if b['accent'] and eff_disp > 0.25:
                        draw.rectangle(
                            [cur_x, cur_y, cur_x + b['bw'], cur_y + b['bh']],
                            outline=b['accent'],
                            width=1
                        )

        if scan_y is not None and 0 <= scan_y < ph:
            draw.line([(0, scan_y), (pw, scan_y)], fill=(34, 211, 238, 240), width=2)
            if 1 < scan_y < ph - 2:
                draw.line([(10, scan_y - 1), (pw - 10, scan_y - 1)], fill=(139, 92, 246, 180), width=1)
                draw.line([(10, scan_y + 1), (pw - 10, scan_y + 1)], fill=(59, 130, 246, 180), width=1)

        if particle_alpha > 0.05:
            for p in particles:
                px = int(p['x'] + p['vx'] * particle_alpha)
                py = int(p['y'] + p['vy'] * particle_alpha)
                if 0 <= px < pw and 0 <= py < ph:
                    draw.rectangle([px, py, px + p['size'], py + p['size']], fill=p['color'] + (220,))

        return layer

    def composite_full_hero(portrait_layer, role_text, cursor_visible):
        frame = hero_base.copy()
        frame.paste(portrait_layer, (640, 26), portrait_layer)

        draw = ImageDraw.Draw(frame)
        draw.rectangle([86, 224, 460, 252], fill=(8, 11, 20))

        color_map = {
            "Full-Stack Developer": (56, 189, 248),
            "Software Engineer": (129, 140, 248),
            "React & React Native Developer": (34, 211, 238),
            "AI Application Developer": (103, 232, 249)
        }
        text_color = color_map.get(role_text, (56, 189, 248))
        draw.text((86, 226), role_text, font=font_mono, fill=text_color)

        if cursor_visible:
            bbox = font_mono.getbbox(role_text)
            text_w = bbox[2] - bbox[0]
            cx = 86 + text_w + 4
            draw.line([(cx, 228), (cx, 248)], fill=(34, 211, 238), width=2)

        return frame.convert('RGB')

    # =========================================================================
    # EXACT 10-SECOND TIMELINE (Exact 10ms-multiple delays for GIF89a standard)
    # Phase 1: 0.0s - 2.55s (2550ms): Reconstruction (15 frames x 170ms)
    # Phase 2: 2.55s - 7.05s (4500ms): Sharp portrait hold (5 frames x 900ms)
    # Phase 3: 7.05s - 9.09s (2040ms): Disintegration (12 frames x 170ms)
    # Phase 4: 9.09s - 10.05s (960ms): Settle to start state (6 frames x 160ms)
    # Total duration = 2550 + 4500 + 2040 + 960 = 10,050ms (~10.05s).
    # =========================================================================

    hero_frames = []
    portrait_frames = []
    durations = []

    print("\n1. Rendering Phase 1: 0.0s - 2.55s (Continuous Pixel Reconstruction)...")
    for i in range(15):
        prog = i / 14.0
        disp = max(0.0, (1.0 - prog) ** 2.2)
        coarseness = max(1, int(14 * (1.0 - prog))) if disp < 0.25 else 1
        scan_y = int(prog * ph) if prog < 0.85 else None
        p_layer = render_portrait_layer(disp, coarseness, scan_y, particle_alpha=1.0 - prog)

        role = roles[0]
        cursor = (i % 2 == 0)
        h_frame = composite_full_hero(p_layer, role, cursor)

        p_canvas = Image.new('RGB', (pw, ph), bg_color_rgb)
        p_canvas.paste(p_layer, (0, 0), p_layer)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        durations.append(170)

    print("2. Rendering Phase 2: 2.55s - 7.05s (Complete Sharp Photograph Hold)...")
    p_layer_sharp = render_portrait_layer(0.0, 1, None, 0.0)
    p_canvas_sharp = Image.new('RGB', (pw, ph), bg_color_rgb)
    p_canvas_sharp.paste(p_layer_sharp, (0, 0), p_layer_sharp)

    for i in range(5):
        role = roles[1] if i < 2 else roles[2]
        cursor = (i % 2 == 0)
        h_frame = composite_full_hero(p_layer_sharp, role, cursor)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas_sharp)
        durations.append(900)

    print("3. Rendering Phase 3: 7.05s - 9.09s (Continuous Pixel Disintegration)...")
    for i in range(12):
        prog = (i + 1) / 12.0
        disp = (3.0 * prog**2 - 2.0 * prog**3)
        scan_y = int(prog * ph)
        p_layer = render_portrait_layer(disp, 1, scan_y, particle_alpha=prog)

        role = roles[3]
        cursor = (i % 2 == 0)
        h_frame = composite_full_hero(p_layer, role, cursor)

        p_canvas = Image.new('RGB', (pw, ph), bg_color_rgb)
        p_canvas.paste(p_layer, (0, 0), p_layer)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        durations.append(170)

    print("4. Rendering Phase 4: 9.09s - 10.05s (Settling to Start State)...")
    for i in range(6):
        prog = i / 5.0
        disp = 1.0 - 0.03 * math.sin(prog * math.pi)
        p_layer = render_portrait_layer(disp, 1, None, particle_alpha=1.0)

        role = roles[3]
        cursor = True
        h_frame = composite_full_hero(p_layer, role, cursor)

        p_canvas = Image.new('RGB', (pw, ph), bg_color_rgb)
        p_canvas.paste(p_layer, (0, 0), p_layer)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        durations.append(160)

    total_cycle_ms = sum(durations)
    print(f"\nTimeline verified: {len(hero_frames)} frames, total duration = {total_cycle_ms} ms ({total_cycle_ms/1000:.2f} s)")

    # Build Adaptive Palette based on sharp photographic frame
    print("Building high-quality adaptive color palette...")
    sample_sharp_hero = hero_frames[15]
    palette_hero = sample_sharp_hero.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)

    sample_sharp_port = portrait_frames[15]
    palette_port = sample_sharp_port.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)

    print("Quantizing hero frames (dither=NONE for crisp typography)...")
    h_quantized = [f.quantize(palette=palette_hero, dither=Image.Dither.NONE) for f in hero_frames]

    print("Quantizing portrait frames...")
    p_quantized = [f.quantize(palette=palette_port, dither=Image.Dither.FLOYDSTEINBERG) for f in portrait_frames]

    # Save GIFs (do not use optimize=True so all 38 discrete timeline frames are preserved!)
    h_gif_path = 'assets/hero.gif'
    print(f"Saving {h_gif_path}...")
    h_quantized[0].save(
        h_gif_path,
        save_all=True,
        append_images=h_quantized[1:],
        duration=durations,
        loop=0
    )
    h_size_mb = os.path.getsize(h_gif_path) / (1024 * 1024)
    print(f"Saved {h_gif_path}: {h_size_mb:.2f} MB")

    p_gif_path = 'assets/richard-portrait-reveal.gif'
    print(f"Saving {p_gif_path}...")
    p_quantized[0].save(
        p_gif_path,
        save_all=True,
        append_images=p_quantized[1:],
        duration=durations,
        loop=0
    )
    p_size_mb = os.path.getsize(p_gif_path) / (1024 * 1024)
    print(f"Saved {p_gif_path}: {p_size_mb:.2f} MB")

    # Generate contact sheet for Part 9 verification
    sheet_w, sheet_h = 1000 * 2, 420 * 3
    contact_sheet = Image.new('RGB', (sheet_w, sheet_h), (8, 11, 20))
    key_indices = [0, 7, 15, 24, 30, 37]
    labels = [
        "01. RECONSTRUCTION START (0.0s) - Scattered Pixel Blocks",
        "02. MID-RECONSTRUCTION (1.2s) - Blocks Assembling",
        "03. SHARP PHOTOGRAPH HOLD (2.55s - 7.05s) - Pristine Face",
        "04. DISINTEGRATION START (7.5s) - Blocks Detaching",
        "05. FULL DISINTEGRATION (8.8s) - Blocks Scattered",
        "06. LOOP CLOSURE (9.9s) - Settled to Seamless Start"
    ]
    for idx, f_idx in enumerate(key_indices):
        col = idx % 2
        row = idx // 2
        x = col * 1000
        y = row * 420
        f_im = hero_frames[f_idx].copy()
        d = ImageDraw.Draw(f_im)
        d.rectangle([10, 10, 480, 32], fill=(13, 19, 33))
        d.text((16, 14), labels[idx], fill=(34, 211, 238))
        contact_sheet.paste(f_im, (x, y))

    contact_sheet.save('scratch/hero_animation_contact_sheet.png')
    print("Saved scratch/hero_animation_contact_sheet.png")

if __name__ == '__main__':
    build_premium_hero_and_portrait()
