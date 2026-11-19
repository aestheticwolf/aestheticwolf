import numpy as np
from PIL import Image, ImageDraw
import random
import os

def generate_pixel_reveal_gif():
    # Load the static portrait
    portrait_full = Image.open('assets/richard-portrait-static.png').convert('RGBA')

    # Output dimensions for the GIF: 420x462 (compact, retina-sharp)
    out_w, out_h = 420, 462
    portrait = portrait_full.resize((out_w, out_h), Image.Resampling.LANCZOS)
    portrait_arr = np.array(portrait, dtype=np.float32)

    bg_color = (8, 11, 20)  # #080B14

    # Seed random for reproducible cinematic particles
    np.random.seed(42)
    random.seed(42)

    frames = []
    durations = []
    total_anim_frames = 22

    # Pre-generate floating digital particles
    num_particles = 45
    particles = []
    for _ in range(num_particles):
        px = random.randint(10, out_w - 10)
        py = random.randint(10, out_h - 40)
        size = random.choice([2, 3, 4, 5])
        color = random.choice([
            (34, 211, 238),   # Cyan #22D3EE
            (59, 130, 246),   # Electric Blue #3B82F6
            (139, 92, 246),   # Violet #8B5CF6
            (167, 139, 250),  # Light Violet #A78BFA
            (245, 245, 247),  # White #F5F5F7
        ])
        speed_y = random.uniform(-15, -4)
        speed_x = random.uniform(-5, 5)
        phase_start = random.uniform(0.0, 0.4)
        phase_end = random.uniform(0.7, 0.95)
        particles.append({
            'x': px, 'y': py, 'size': size, 'color': color,
            'vx': speed_x, 'vy': speed_y, 'start': phase_start, 'end': phase_end
        })

    print(f"Generating {total_anim_frames + 1} frames...")

    for f_idx in range(total_anim_frames + 1):
        t = f_idx / float(total_anim_frames)  # 0.0 to 1.0

        # Base canvas initialized to #080B14
        frame_canvas = np.full((out_h, out_w, 3), bg_color, dtype=np.float32)

        if t >= 0.95:
            # Final sharp phase (Phase 4): 100% full original portrait
            alpha = portrait_arr[:, :, 3:4] / 255.0
            rgb = portrait_arr[:, :, :3]
            blended = rgb * alpha + frame_canvas * (1.0 - alpha)
            frame_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8), mode='RGB')

        elif t < 0.25:
            # PHASE 1: Scattered digital fragments, large block size, displacement
            phase_t = t / 0.25
            block_size = int(28 - 12 * phase_t)  # 28 -> 16
            displacement = int(25 * (1.0 - phase_t))

            small_w = max(1, out_w // block_size)
            small_h = max(1, out_h // block_size)
            small = portrait.resize((small_w, small_h), Image.Resampling.BOX)
            pix = small.resize((out_w, out_h), Image.Resampling.NEAREST)
            pix_arr = np.array(pix, dtype=np.float32)

            shifted = pix_arr.copy()
            if displacement > 0:
                for by in range(0, out_h, block_size):
                    for bx in range(0, out_w, block_size):
                        if random.random() < (0.6 - 0.4 * phase_t):
                            dx = random.randint(-displacement, displacement)
                            dy = random.randint(-displacement // 2, displacement // 2)
                            y2 = min(out_h, by + block_size)
                            x2 = min(out_w, bx + block_size)
                            sy1 = max(0, min(out_h - 1, by + dy))
                            sx1 = max(0, min(out_w - 1, bx + dx))
                            sy2 = min(out_h, sy1 + (y2 - by))
                            sx2 = min(out_w, sx1 + (x2 - bx))
                            shifted[by:by+(sy2-sy1), bx:bx+(sx2-sx1)] = pix_arr[sy1:sy2, sx1:sx2]

            alpha = (shifted[:, :, 3:4] / 255.0) * (0.3 + 0.6 * phase_t)
            rgb = shifted[:, :, :3]
            blended = rgb * alpha + frame_canvas * (1.0 - alpha)
            frame_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8), mode='RGB')

        elif t < 0.65:
            # PHASE 2: Assembling into recognizable face, block size 14 -> 6
            phase_t = (t - 0.25) / 0.40
            block_size = int(14 - 8 * phase_t)  # 14 -> 6
            small_w = max(1, out_w // block_size)
            small_h = max(1, out_h // block_size)
            small = portrait.resize((small_w, small_h), Image.Resampling.BOX)
            pix = small.resize((out_w, out_h), Image.Resampling.NEAREST)
            pix_arr = np.array(pix, dtype=np.float32)

            alpha = (pix_arr[:, :, 3:4] / 255.0) * (0.85 + 0.15 * phase_t)
            rgb = pix_arr[:, :, :3]
            blended = rgb * alpha + frame_canvas * (1.0 - alpha)
            frame_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8), mode='RGB')

        else:
            # PHASE 3: Finer blocks (4px -> 2px) blending into full sharp portrait
            phase_t = (t - 0.65) / 0.30
            block_size = max(1, int(4 - 3 * phase_t))  # 4 -> 1
            if block_size > 1:
                small_w = max(1, out_w // block_size)
                small_h = max(1, out_h // block_size)
                small = portrait.resize((small_w, small_h), Image.Resampling.BOX)
                pix = small.resize((out_w, out_h), Image.Resampling.NEAREST)
                pix_arr = np.array(pix, dtype=np.float32)
                current_arr = pix_arr * (1.0 - phase_t) + portrait_arr * phase_t
            else:
                current_arr = portrait_arr

            alpha = current_arr[:, :, 3:4] / 255.0
            rgb = current_arr[:, :, :3]
            blended = rgb * alpha + frame_canvas * (1.0 - alpha)
            frame_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8), mode='RGB')

        # Draw scanning line and particles
        draw = ImageDraw.Draw(frame_img)

        # Scanning Laser Beam (sweeps down during t = 0.05 to 0.85)
        if 0.05 <= t <= 0.85:
            scan_prog = (t - 0.05) / 0.80
            scan_y = int(scan_prog * (out_h - 20))
            draw.line([(20, scan_y), (out_w - 20, scan_y)], fill=(34, 211, 238), width=2)
            if 1 < scan_y < out_h - 2:
                draw.line([(30, scan_y - 1), (out_w - 30, scan_y - 1)], fill=(139, 92, 246), width=1)
                draw.line([(30, scan_y + 1), (out_w - 30, scan_y + 1)], fill=(59, 130, 246), width=1)

        # Digital floating particles
        if t < 0.92:
            for p in particles:
                if p['start'] <= t <= p['end']:
                    pt = (t - p['start']) / (p['end'] - p['start'])
                    cur_x = int(p['x'] + p['vx'] * pt * 10)
                    cur_y = int(p['y'] + p['vy'] * pt * 10)
                    if 0 <= cur_x < out_w and 0 <= cur_y < out_h:
                        s = p['size']
                        alpha_p = np.sin(pt * np.pi)
                        if alpha_p > 0.2:
                            draw.rectangle([cur_x, cur_y, cur_x + s, cur_y + s], fill=p['color'])

        frames.append(frame_img)
        if f_idx < total_anim_frames:
            durations.append(90)  # ~90ms per frame
        else:
            durations.append(9000)  # 9s hold on final frame

    print("Converting frames to adaptive palette...")
    quantized_frames = []
    # Use final frame to build global palette so the sharp face looks optimal
    palette_im = frames[-1].convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
    for f in frames:
        q = f.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
        quantized_frames.append(q)

    gif_path = 'assets/richard-portrait-reveal.gif'
    print(f"Saving {gif_path}...")
    quantized_frames[0].save(
        gif_path,
        save_all=True,
        append_images=quantized_frames[1:],
        duration=durations,
        optimize=True
    )
    print(f"Successfully generated {gif_path}")

    size_mb = os.path.getsize(gif_path) / (1024 * 1024)
    print(f"GIF file size: {size_mb:.2f} MB")

if __name__ == '__main__':
    generate_pixel_reveal_gif()
