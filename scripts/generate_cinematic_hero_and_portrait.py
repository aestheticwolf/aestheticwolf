import os
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def build_pixel_animation():
    print("Loading assets...")
    # Load base hero (1000x420)
    hero_base = Image.open('scratch/hero_base.png').convert('RGB')
    base_w, base_h = hero_base.size

    # Load static portrait
    portrait_full = Image.open('assets/richard-portrait-static.png').convert('RGBA')

    # Dimensions for the portrait inside hero
    # Right side placement: x=625, y=24, width=350, height=386
    pw, ph = 350, 386
    portrait = portrait_full.resize((pw, ph), Image.Resampling.LANCZOS)
    port_arr = np.array(portrait)

    # Base background color: #080B14
    bg_color = (8, 11, 20)

    # 1. Slice portrait into square pixel blocks (8x8)
    block_size = 8
    cx, cy = pw // 2, int(ph * 0.42)

    np.random.seed(1337)
    random.seed(1337)

    blocks = []
    for by in range(0, ph, block_size):
        for bx in range(0, pw, block_size):
            bw = min(block_size, pw - bx)
            bh = min(block_size, ph - by)
            patch = port_arr[by:by+bh, bx:bx+bw]
            # Check average alpha
            alpha_mean = patch[:, :, 3].mean()
            if alpha_mean > 12:
                # Direction vector away from face center
                dx = (bx + bw/2.0) - cx
                dy = (by + bh/2.0) - cy
                dist = math.hypot(dx, dy) + 1.0
                nx = dx / dist
                ny = dy / dist

                # Random scatter distance and angular drift
                scatter_dist = random.uniform(80, 220)
                drift_x = random.uniform(-40, 40)
                drift_y = random.uniform(-30, 30)

                accent = None
                if random.random() < 0.16:
                    accent = random.choice([
                        (34, 211, 238),   # Cyan #22D3EE
                        (59, 130, 246),   # Electric Blue #3B82F6
                        (139, 92, 246),   # Violet #8B5CF6
                        (245, 245, 247),  # White #F5F5F7
                    ])

                blocks.append({
                    'bx': bx, 'by': by, 'bw': bw, 'bh': bh,
                    'patch': patch,
                    'patch_im': Image.fromarray(patch),
                    'sx': nx * scatter_dist + drift_x,
                    'sy': ny * scatter_dist + drift_y,
                    'accent': accent,
                    'rand_delay': random.uniform(0.0, 0.25)
                })

    print(f"Total active pixel blocks: {len(blocks)}")

    # Digital particles for ambient cybernetic cloud
    particles = []
    for _ in range(35):
        particles.append({
            'x': random.uniform(20, pw - 20),
            'y': random.uniform(20, ph - 40),
            'vx': random.uniform(-30, 30),
            'vy': random.uniform(-40, -10),
            'size': random.choice([2, 3, 4]),
            'color': random.choice([(34, 211, 238), (139, 92, 246), (59, 130, 246)])
        })

    # Prepare fonts for typing text
    try:
        font_mono = ImageFont.truetype("consola.ttf", 19)
    except:
        font_mono = ImageFont.load_default()

    roles = [
        "Full-Stack Developer",
        "Software Engineer",
        "React & React Native Developer",
        "Backend Developer",
        "AI Application Developer"
    ]

    # Pre-render sharp full portrait pasted onto background
    port_sharp_canvas = Image.new('RGB', (pw, ph), bg_color)
    port_sharp_canvas.paste(portrait, (0, 0), portrait)

    # 2. Build 10-second timeline frames
    # Timeline specification:
    # 0.0s - 3.0s (3000ms): Reconstruction (20 frames, 150ms each)
    # 3.0s - 7.0s (4000ms): Sharp portrait hold (10 frames, 400ms each - typing text rotates)
    # 7.0s - 8.0s (1000ms): Disintegration (10 frames, 100ms each)
    # 8.0s - 10.0s (2000ms): Reassembly back to start (14 frames, 142ms each)
    # Total duration = 3000 + 4000 + 1000 + 2000 = 10,000ms = 10.0 seconds!

    hero_frames = []
    portrait_frames = []
    frame_durations = []

    def render_portrait_frame(disp_factor, block_coarseness=1, scan_y=None, particle_alpha=0.0):
        """Render the portrait at a given displacement and coarseness."""
        canvas = Image.new('RGB', (pw, ph), bg_color)
        draw = ImageDraw.Draw(canvas)

        if disp_factor <= 0.001 and block_coarseness <= 1:
            # 100% sharp photographic portrait
            canvas.paste(portrait, (0, 0), portrait)
        elif disp_factor <= 0.001 and block_coarseness > 1:
            # Grid-locked but coarse pixel blocks
            # Downsample and upsample box filter
            small_w = max(1, pw // block_coarseness)
            small_h = max(1, ph // block_coarseness)
            pix = portrait.resize((small_w, small_h), Image.Resampling.BOX).resize((pw, ph), Image.Resampling.NEAREST)
            canvas.paste(pix, (0, 0), pix)
        else:
            # Physically displaced and scattered pixel blocks
            for b in blocks:
                # Individual block response with slight easing
                eff_disp = max(0.0, min(1.0, disp_factor + (b['rand_delay'] - 0.12) * disp_factor))
                cur_x = int(b['bx'] + b['sx'] * eff_disp)
                cur_y = int(b['by'] + b['sy'] * eff_disp)

                if -block_size < cur_x < pw and -block_size < cur_y < ph:
                    patch = b['patch_im']
                    # Fade alpha slightly when far from home
                    if eff_disp > 0.1:
                        pa = np.array(patch)
                        alpha_scale = max(0.2, 1.0 - 0.5 * eff_disp)
                        pa[:, :, 3] = (pa[:, :, 3] * alpha_scale).astype(np.uint8)
                        patch = Image.fromarray(pa)
                    canvas.paste(patch, (cur_x, cur_y), patch)

                    # Cybernetic particle borders on scattered blocks
                    if b['accent'] and eff_disp > 0.2:
                        draw.rectangle(
                            [cur_x, cur_y, cur_x + b['bw'], cur_y + b['bh']],
                            outline=b['accent'],
                            width=1
                        )

        # Scanning laser beam
        if scan_y is not None and 0 <= scan_y < ph:
            draw.line([(0, scan_y), (pw, scan_y)], fill=(34, 211, 238), width=2)
            draw.line([(10, scan_y - 1), (pw - 10, scan_y - 1)], fill=(139, 92, 246), width=1)
            draw.line([(10, scan_y + 1), (pw - 10, scan_y + 1)], fill=(59, 130, 246), width=1)

        # Ambient floating digital particles
        if particle_alpha > 0.05:
            for p in particles:
                px = int(p['x'] + p['vx'] * particle_alpha)
                py = int(p['y'] + p['vy'] * particle_alpha)
                if 0 <= px < pw and 0 <= py < ph:
                    draw.rectangle([px, py, px + p['size'], py + p['size']], fill=p['color'])

        return canvas

    def composite_hero_frame(portrait_canvas, role_text, cursor_visible):
        """Composite the portrait frame and animated role text onto the hero base."""
        frame = hero_base.copy()
        # Paste portrait at x=625, y=24
        frame.paste(portrait_canvas, (625, 24))

        # Draw left-side typing text at x=86, y=228
        # Clear typing area background
        draw = ImageDraw.Draw(frame)
        draw.rectangle([86, 224, 460, 252], fill=(8, 11, 20))

        # Role text in cyan/violet
        color_map = {
            "Full-Stack Developer": (56, 189, 248),
            "Software Engineer": (129, 140, 248),
            "React & React Native Developer": (34, 211, 238),
            "Backend Developer": (167, 139, 250),
            "AI Application Developer": (103, 232, 249)
        }
        text_color = color_map.get(role_text, (56, 189, 248))
        draw.text((86, 226), role_text, font=font_mono, fill=text_color)

        if cursor_visible:
            # Measure text width
            bbox = font_mono.getbbox(role_text)
            text_w = bbox[2] - bbox[0]
            cx = 86 + text_w + 4
            draw.line([(cx, 228), (cx, 248)], fill=(34, 211, 238), width=2)

        return frame

    print("Generating Phase 1: 0.0s - 3.0s (Reconstruction)...")
    # 20 frames, duration 150ms each (3000ms total)
    for i in range(20):
        prog = i / 19.0 # 0.0 to 1.0
        # Inward motion: displacement factor goes from 1.0 down to 0.0
        disp = max(0.0, (1.0 - prog) ** 1.8)
        # Block coarseness: 16 -> 8 -> 4 -> 2 -> 1
        coarseness = max(1, int(16 * (1.0 - prog))) if disp < 0.25 else 1
        # Laser scanner sweeps down from y=0 to y=ph
        scan_y = int(prog * ph) if prog < 0.85 else None
        p_canvas = render_portrait_frame(disp, coarseness, scan_y, particle_alpha=1.0 - prog)

        role = roles[0] # Full-Stack Developer
        cursor = (i % 2 == 0)
        h_frame = composite_hero_frame(p_canvas, role, cursor)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        frame_durations.append(150)

    print("Generating Phase 2: 3.0s - 7.0s (Sharp photographic hold)...")
    # 10 frames, duration 400ms each (4000ms total)
    # Portrait is 100% sharp photograph held rock-solid
    p_sharp = render_portrait_frame(0.0, 1, None, 0.0)
    for i in range(10):
        # Rotate roles: frame 0..4 = Software Engineer, frame 5..9 = React & React Native Developer
        role = roles[1] if i < 5 else roles[2]
        cursor = (i % 2 == 0)
        h_frame = composite_hero_frame(p_sharp, role, cursor)

        hero_frames.append(h_frame)
        portrait_frames.append(p_sharp)
        frame_durations.append(400)

    print("Generating Phase 3: 7.0s - 8.0s (Disintegration)...")
    # 10 frames, duration 100ms each (1000ms total)
    # Displacement factor goes from 0.0 up to 1.0
    for i in range(10):
        prog = (i + 1) / 10.0 # 0.1 to 1.0
        disp = (prog ** 1.4)
        scan_y = int(prog * ph)
        p_canvas = render_portrait_frame(disp, 1, scan_y, particle_alpha=prog)

        role = roles[3] # Backend Developer
        cursor = True
        h_frame = composite_hero_frame(p_canvas, role, cursor)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        frame_durations.append(100)

    print("Generating Phase 4: 8.0s - 10.0s (Reassembly)...")
    # 14 frames, duration 142ms each (2000ms total)
    # Displacement factor goes from 1.0 down to ~0.05 (seamless loop back to Phase 1!)
    for i in range(14):
        prog = i / 14.0 # 0.0 to ~0.93
        disp = max(0.0, (1.0 - prog) ** 1.5)
        coarseness = max(1, int(12 * (1.0 - prog))) if disp < 0.3 else 1
        p_canvas = render_portrait_frame(disp, coarseness, None, particle_alpha=1.0 - prog)

        role = roles[4] # AI Application Developer
        cursor = (i % 2 == 0)
        h_frame = composite_hero_frame(p_canvas, role, cursor)

        hero_frames.append(h_frame)
        portrait_frames.append(p_canvas)
        frame_durations.append(142)

    total_duration_ms = sum(frame_durations)
    print(f"Total frames: {len(hero_frames)}, Total cycle duration: {total_duration_ms} ms ({total_duration_ms/1000:.2f} s)")

    # 3. Save representative verification frames
    hero_frames[0].save('scratch/verify_frame_01_reconstruct.png')
    hero_frames[19].save('scratch/verify_frame_20_sharp_hold.png')
    hero_frames[34].save('scratch/verify_frame_35_disintegrate.png')
    hero_frames[48].save('scratch/verify_frame_49_reassemble.png')
    print("Saved representative frames in scratch/ for verification.")

    # 4. Save assets/richard-portrait-reveal.gif
    print("Quantizing and saving assets/richard-portrait-reveal.gif...")
    p_quantized = [f.convert('P', palette=Image.Palette.ADAPTIVE, colors=256) for f in portrait_frames]
    p_gif_path = 'assets/richard-portrait-reveal.gif'
    p_quantized[0].save(
        p_gif_path,
        save_all=True,
        append_images=p_quantized[1:],
        duration=frame_durations,
        loop=0,
        optimize=True
    )
    p_size_mb = os.path.getsize(p_gif_path) / (1024 * 1024)
    print(f"Saved {p_gif_path} ({p_size_mb:.2f} MB, loop=0)")

    # 5. Save assets/hero.gif (Complete Unified Hero Banner)
    print("Quantizing and saving assets/hero.gif...")
    h_quantized = [f.convert('P', palette=Image.Palette.ADAPTIVE, colors=256) for f in hero_frames]
    h_gif_path = 'assets/hero.gif'
    h_quantized[0].save(
        h_gif_path,
        save_all=True,
        append_images=h_quantized[1:],
        duration=frame_durations,
        loop=0,
        optimize=True
    )
    h_size_mb = os.path.getsize(h_gif_path) / (1024 * 1024)
    print(f"Saved {h_gif_path} ({h_size_mb:.2f} MB, loop=0)")

    # 6. Verify frame differences mathematically
    arr_reconstruct = np.array(hero_frames[0], dtype=np.float32)
    arr_sharp = np.array(hero_frames[19], dtype=np.float32)
    arr_disint = np.array(hero_frames[34], dtype=np.float32)

    diff_recon_sharp = np.abs(arr_reconstruct - arr_sharp).mean()
    diff_disint_sharp = np.abs(arr_disint - arr_sharp).mean()
    diff_recon_disint = np.abs(arr_reconstruct - arr_disint).mean()

    print("\n=== FRAME VARIANCE VERIFICATION ===")
    print(f"Mean pixel diff (Reconstruction vs Sharp): {diff_recon_sharp:.2f}")
    print(f"Mean pixel diff (Disintegration vs Sharp): {diff_disint_sharp:.2f}")
    print(f"Mean pixel diff (Reconstruction vs Disintegration): {diff_recon_disint:.2f}")

    assert diff_recon_sharp > 5.0, "Frames lack reconstruction variance!"
    assert diff_disint_sharp > 5.0, "Frames lack disintegration variance!"
    print("VERIFICATION SUCCESS: Real pixel transformation confirmed mathematically across frames!")

if __name__ == '__main__':
    build_pixel_animation()
