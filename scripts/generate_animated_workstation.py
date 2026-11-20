import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def displace_region(img_arr, cx, cy, rx, ry, dy, dx=0.0):
    h, w, c = img_arr.shape
    res = img_arr.copy()
    y_min, y_max = max(0, int(cy - ry)), min(h, int(cy + ry) + 1)
    x_min, x_max = max(0, int(cx - rx)), min(w, int(cx + rx) + 1)
    
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            dx_norm = (x - cx) / float(rx)
            dy_norm = (y - cy) / float(ry)
            dist2 = dx_norm**2 + dy_norm**2
            if dist2 < 1.0:
                weight = (1.0 - dist2)**1.5
                src_y = int(np.clip(round(y - weight * dy), 0, h - 1))
                src_x = int(np.clip(round(x - weight * dx), 0, w - 1))
                res[y, x] = img_arr[src_y, src_x]
    return res

def morph_eye(patch, amount):
    if amount <= 0:
        return patch.copy()
    h, w, c = patch.shape
    res = patch.copy()
    shift = int(14 * amount)
    for y in range(h):
        for x in range(w):
            dist_x = abs(x - w // 2) / (w * 0.46)
            dist_y = (y - 16) / 10.0
            if dist_x < 1.0 and -0.8 < dist_y < 0.8:
                weight = amount * (1.0 - dist_x**2)
                src_y = max(0, int(y - shift * weight))
                res[y, x] = (1.0 - weight) * patch[y, x] + weight * patch[src_y, x]
    return res

def generate_workstation_gif():
    base_path = 'scratch/character_workstation_1000x500.png'
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Missing {base_path}")
        
    base_img = Image.open(base_path).convert('RGB')
    base_arr = np.array(base_img)
    h, w, _ = base_arr.shape
    num_frames = 32

    # Typing schedules: (center_x, center_y, radius_x, radius_y, start_frame, duration, peak_dy)
    left_typing_keys = [
        # Left index/middle finger (x=435, y=418)
        (435, 418, 30, 22, 2, 4, 1.8),
        # Left ring finger (x=395, y=425)
        (395, 425, 26, 20, 9, 4, 1.5),
        # Left index finger tap 2 (x=440, y=415)
        (440, 415, 28, 20, 16, 4, 1.9),
        # Left middle finger tap 3 (x=415, y=422)
        (415, 422, 28, 20, 24, 4, 1.6),
    ]

    right_typing_keys = [
        # Right index finger (x=570, y=412)
        (570, 412, 30, 22, 5, 4, 1.8),
        # Right middle finger (x=595, y=415)
        (595, 415, 28, 22, 12, 4, 1.7),
        # Right ring finger (x=625, y=418)
        (625, 418, 26, 20, 20, 4, 1.5),
        # Right index tap 2 (x=575, y=410)
        (575, 410, 28, 20, 27, 4, 1.8),
    ]

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / float(num_frames) # 0.0 to 1.0
        frame_arr = base_arr.copy()

        # --------------------------------------------------------
        # 1. Subtle Breathing / Body Idle Motion (upper body & head)
        # --------------------------------------------------------
        breath_dy = math.sin(t * 2 * math.pi) * 1.2
        if abs(breath_dy) > 0.1:
            frame_arr = displace_region(frame_arr, 600, 180, 160, 170, breath_dy)

        # --------------------------------------------------------
        # 2. Hand & Finger Typing Animation
        # --------------------------------------------------------
        # Left hand typing
        for (cx, cy, rx, ry, start_f, dur, peak_dy) in left_typing_keys:
            if start_f <= f_idx < start_f + dur:
                local_t = (f_idx - start_f) / float(dur)
                dy = math.sin(local_t * math.pi) * peak_dy
                frame_arr = displace_region(frame_arr, cx, cy, rx, ry, dy)

        # Right hand typing
        for (cx, cy, rx, ry, start_f, dur, peak_dy) in right_typing_keys:
            if start_f <= f_idx < start_f + dur:
                local_t = (f_idx - start_f) / float(dur)
                dy = math.sin(local_t * math.pi) * peak_dy
                frame_arr = displace_region(frame_arr, cx, cy, rx, ry, dy)

        # --------------------------------------------------------
        # 3. Natural Eye Blink (Frames 15..19)
        # --------------------------------------------------------
        blink_amount = 0.0
        if f_idx == 15:
            blink_amount = 0.25
        elif f_idx == 16:
            blink_amount = 0.65
        elif f_idx == 17:
            blink_amount = 0.70
        elif f_idx == 18:
            blink_amount = 0.35
        
        if blink_amount > 0:
            frame_arr[125:160, 570:600] = morph_eye(frame_arr[125:160, 570:600], blink_amount)
            frame_arr[125:160, 610:640] = morph_eye(frame_arr[125:160, 610:640], blink_amount)

        # Convert back to PIL Image for lighting & atmospheric effects
        frame_img = Image.fromarray(frame_arr).convert('RGBA')

        # --------------------------------------------------------
        # 4. Gentle Screen Light Pulsing
        # --------------------------------------------------------
        screen_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(screen_overlay)
        
        screen_pulse = 0.5 + 0.5 * math.sin(t * 4 * math.pi)
        cyan_alpha = int(18 + 12 * screen_pulse)
        # Soft radial light from laptop screen onto hands and keyboard
        s_draw.ellipse([210, 290, 470, 450], fill=(34, 211, 238, cyan_alpha))
        # Soft reflection on character's chest & hoodie
        s_draw.ellipse([540, 240, 700, 360], fill=(59, 130, 246, int(10 + 8 * screen_pulse)))

        screen_overlay = screen_overlay.filter(ImageFilter.GaussianBlur(radius=18))
        frame_img = Image.alpha_composite(frame_img, screen_overlay)

        # --------------------------------------------------------
        # 5. Delicate Rising Coffee Steam
        # --------------------------------------------------------
        steam_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        st_draw = ImageDraw.Draw(steam_overlay)
        
        # Steam wisps above mug (mug rim is at x=555, y=390)
        for s_i in range(3):
            s_phase = (t + s_i * 0.33) % 1.0
            st_y = 390 - s_phase * 55
            st_x = 556 + math.sin(s_phase * 2 * math.pi) * 6.0
            st_r = 4.0 + s_phase * 8.0
            st_alpha = int(45 * math.sin(s_phase * math.pi))
            st_draw.ellipse([st_x - st_r, st_y - st_r*0.6, st_x + st_r, st_y + st_r*0.6], fill=(220, 230, 245, st_alpha))

        steam_overlay = steam_overlay.filter(ImageFilter.GaussianBlur(radius=4))
        frame_img = Image.alpha_composite(frame_img, steam_overlay)

        # --------------------------------------------------------
        # 6. Subtle Edge Vignette for Dark Mode GitHub Blending
        # --------------------------------------------------------
        vignette = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        v_draw = ImageDraw.Draw(vignette)
        for y_v in range(14):
            alpha = int((1.0 - y_v / 14.0) * 110)
            v_draw.line([(0, y_v), (w, y_v)], fill=(8, 11, 20, alpha))
        for y_v in range(16):
            alpha = int((y_v / 16.0) * 150)
            v_draw.line([(0, h - 16 + y_v), (w, h - 16 + y_v)], fill=(8, 11, 20, alpha))
        for x_v in range(12):
            alpha = int((1.0 - x_v / 12.0) * 95)
            v_draw.line([(x_v, 0), (x_v, h)], fill=(8, 11, 20, alpha))
        for x_v in range(12):
            alpha = int((x_v / 12.0) * 95)
            v_draw.line([(w - 12 + x_v, 0), (w - 12 + x_v, h)], fill=(8, 11, 20, alpha))

        frame_img = Image.alpha_composite(frame_img, vignette)
        frames.append(frame_img.convert('RGB'))

    print(f"Generated {len(frames)} animated frames.")
    frames[0].save('scratch/workstation_frame0.png')
    frames[16].save('scratch/workstation_frame16.png')

    # Convert to adaptive palette GIF
    gif_out_path = 'assets/behind-the-code.gif'
    palette_frames = []
    palette_img = frames[0].quantize(colors=256, method=Image.Quantize.MEDIANCUT)

    for f in frames:
        pf = f.quantize(colors=256, palette=palette_img, dither=Image.Dither.FLOYDSTEINBERG)
        palette_frames.append(pf)

    palette_frames[0].save(
        gif_out_path,
        save_all=True,
        append_images=palette_frames[1:],
        duration=110, # 110ms * 32 = 3520ms = 3.52 seconds seamless loop
        loop=0,
        optimize=True
    )

    size_mb = os.path.getsize(gif_out_path) / (1024 * 1024)
    print(f"Saved {gif_out_path} ({len(frames)} frames, 3.52s loop, {size_mb:.2f} MB)")

if __name__ == '__main__':
    generate_workstation_gif()
