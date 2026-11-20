import math
import random
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_checkmark(draw, x, y, color=(16, 185, 129, 255), width=2):
    # Precise vector checkmark
    p1 = (x, y + 6)
    p2 = (x + 3, y + 10)
    p3 = (x + 8, y + 2)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def draw_prompt_arrow(draw, x, y, color=(34, 211, 238, 255), width=2):
    p1 = (x, y + 2)
    p2 = (x + 4, y + 6)
    p3 = (x, y + 10)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def create_behind_the_code():
    base_path = 'scratch/base_cropped.png'
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Missing {base_path}")
        
    base_img = Image.open(base_path).convert('RGBA')
    w, h = base_img.size

    # Fonts
    font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
    font_code_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 12)
    font_tab = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
    font_term = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 10)
    font_term_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 10)
    font_ui = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 10)

    # Pre-generate 30 ambient particles
    random.seed(42)
    particles = []
    for _ in range(30):
        particles.append({
            'x': random.uniform(20, w - 20),
            'y': random.uniform(20, h - 30),
            'speed': random.uniform(1.0, 2.8),
            'rad': random.uniform(1.2, 2.2),
            'color': random.choice([(34, 211, 238), (139, 92, 246), (167, 139, 250)])
        })

    num_frames = 36
    frames = []

    full_cmd = "$ npm run dev"
    term_stages = [
        "Initializing development environment",
        "Loading application modules",
        "Connecting services",
        "Compiling project",
        "Server running: http://localhost:3000",
        "Ready for development"
    ]

    for f_idx in range(num_frames):
        t = f_idx / float(num_frames)
        
        # ----------------------------------------------------
        # 1. Soft Volumetric Laptop & Ambient Glow Layer
        # ----------------------------------------------------
        glow_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_layer)

        glow_pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        glow_alpha = int(35 + 25 * glow_pulse)
        # Soft blurred radial screen glow
        glow_draw.ellipse([200, 280, 420, 420], fill=(34, 211, 238, glow_alpha))
        glow_draw.ellipse([590, 80, 710, 240], fill=(139, 92, 246, int(15 + 12 * math.cos(t * 2 * math.pi))))
        
        # Blur the glow layer for smooth lighting
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=16))

        # UI Overlay Layer
        frame_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(frame_overlay)

        # ----------------------------------------------------
        # 2. Holographic Scan Beam (frames 14 to 28)
        # ----------------------------------------------------
        if 14 <= f_idx <= 28:
            scan_prog = (f_idx - 14) / 14.0
            beam_x = int(scan_prog * (w + 80) - 40)
            draw.rectangle([beam_x, 0, beam_x + 2, h], fill=(34, 211, 238, 40))
            draw.rectangle([beam_x - 20, 0, beam_x + 22, h], fill=(139, 92, 246, 10))

        # ----------------------------------------------------
        # 3. Ambient Floating Particles
        # ----------------------------------------------------
        for p in particles:
            py = (p['y'] - f_idx * p['speed']) % h
            px = (p['x'] + math.sin(t * 2 * math.pi + p['y']) * 10.0) % w
            r = p['rad']
            p_alpha = int(130 + 80 * math.sin(t * 4 * math.pi + p['x']))
            c = p['color']
            draw.ellipse([px - r, py - r, px + r, py + r], fill=c + (p_alpha,))

        # ----------------------------------------------------
        # 4. Left Floating Code Panel (developer.tsx)
        # ----------------------------------------------------
        code_dy = math.sin(t * 2 * math.pi) * 3.5
        px, py, pw, ph = 24, int(26 + code_dy), 345, 235

        # Glass panel shadow
        draw.rounded_rectangle([px+2, py+4, px+pw+2, py+ph+4], radius=10, fill=(0, 0, 0, 95))
        # Dark glass panel background
        draw.rounded_rectangle([px, py, px+pw, py+ph], radius=10, fill=(8, 14, 28, 230), outline=(34, 211, 238, 90), width=1)
        # Header bar
        draw.rounded_rectangle([px, py, px+pw, py+28], radius=10, fill=(13, 21, 38, 245))
        draw.rectangle([px, py+16, px+pw, py+28], fill=(13, 21, 38, 245))
        draw.line([px, py+28, px+pw, py+28], fill=(34, 211, 238, 45), width=1)

        # Window controls (mac dots)
        draw.ellipse([px+12, py+9, px+20, py+17], fill=(239, 68, 68, 220))
        draw.ellipse([px+26, py+9, px+34, py+17], fill=(245, 158, 11, 220))
        draw.ellipse([px+40, py+9, px+48, py+17], fill=(16, 185, 129, 220))

        # Active tab
        draw.rounded_rectangle([px+60, py+4, px+180, py+27], radius=4, fill=(18, 28, 52, 240))
        draw.text((px+72, py+7), 'developer.tsx', font=font_tab, fill=(34, 211, 238, 245))
        draw.text((px+pw-75, py+8), 'UTF-8  TSX', font=font_ui, fill=(100, 116, 139, 200))

        # Code Syntax Highlighting
        code_lines = [
            [('const', (192, 132, 252)), (' developer', (34, 211, 238)), (' = {', (241, 245, 249))],
            [('  name: ', (226, 232, 240)), ('"Richard D\'Souza"', (52, 211, 153)), (',', (148, 163, 184))],
            [('  role: ', (226, 232, 240)), ('"Full-Stack Developer"', (52, 211, 153)), (',', (148, 163, 184))],
            [('  focus: [', (226, 232, 240)), ('"Web"', (52, 211, 153)), (', ', (148, 163, 184)), ('"Mobile"', (52, 211, 153)), (', ', (148, 163, 184)), ('"AI"', (52, 211, 153)), (']', (226, 232, 240))],
            [('};', (241, 245, 249))],
            [('function ', (192, 132, 252)), ('buildSomething', (34, 211, 238)), ('() {', (241, 245, 249))],
            [('  return ', (192, 132, 252)), ('createIdeas', (34, 211, 238)), ('();', (241, 245, 249))],
            [('}', (241, 245, 249))],
            [('// production runtime active', (100, 116, 139))]
        ]

        cy = py + 38
        for seg_list in code_lines:
            cx = px + 18
            for txt, color in seg_list:
                draw.text((cx, cy), txt, font=font_code, fill=color + (255,))
                bbox = draw.textbbox((cx, cy), txt, font=font_code)
                cx = bbox[2]
            cy += 19

        # ----------------------------------------------------
        # 5. Right Floating Terminal (bash ~ dev-server)
        # ----------------------------------------------------
        term_dy = math.cos(t * 2 * math.pi) * 3.0
        tx, ty, tw, th = 730, int(28 + term_dy), 246, 248

        # Glass panel shadow
        draw.rounded_rectangle([tx+2, ty+4, tx+tw+2, ty+th+4], radius=10, fill=(0, 0, 0, 95))
        # Dark glass panel background
        draw.rounded_rectangle([tx, ty, tx+tw, ty+th], radius=10, fill=(6, 10, 24, 235), outline=(139, 92, 246, 90), width=1)
        # Header
        draw.rounded_rectangle([tx, ty, tx+tw, ty+26], radius=10, fill=(11, 16, 34, 245))
        draw.rectangle([tx, ty+14, tx+tw, ty+26], fill=(11, 16, 34, 245))
        draw.line([tx, ty+26, tx+tw, ty+26], fill=(139, 92, 246, 45), width=1)

        # Window dots
        draw.ellipse([tx+10, ty+8, tx+17, ty+15], fill=(239, 68, 68, 200))
        draw.ellipse([tx+22, ty+8, tx+29, ty+15], fill=(245, 158, 11, 200))
        draw.ellipse([tx+34, ty+8, tx+41, ty+15], fill=(16, 185, 129, 200))
        draw.text((tx+50, ty+6), 'bash ~ workstation', font=font_term, fill=(148, 163, 184, 230))

        # Terminal Typing Logic
        char_count = min(len(full_cmd), int((f_idx / 7.0) * len(full_cmd))) if f_idx <= 7 else len(full_cmd)
        cmd_typed = full_cmd[:char_count]
        show_cursor = (f_idx % 4 < 2)

        tcy = ty + 36
        draw.text((tx+14, tcy), '$ ', font=font_term_bold, fill=(34, 211, 238, 255))
        draw.text((tx+26, tcy), cmd_typed[2:] if len(cmd_typed) > 2 else '', font=font_term, fill=(248, 250, 252, 255))
        if show_cursor and f_idx <= 8:
            cmd_bbox = draw.textbbox((tx+26, tcy), cmd_typed[2:] if len(cmd_typed) > 2 else '', font=font_term)
            cursor_x = cmd_bbox[2] + 2
            draw.text((cursor_x, tcy), '█', font=font_term, fill=(34, 211, 238, 230))
        tcy += 20

        # Sequential reveal counts
        revealed_count = 0
        if f_idx >= 8: revealed_count = 1
        if f_idx >= 12: revealed_count = 2
        if f_idx >= 16: revealed_count = 3
        if f_idx >= 20: revealed_count = 4
        if f_idx >= 24: revealed_count = 5
        if f_idx >= 28: revealed_count = 6

        for i in range(revealed_count):
            line_txt = term_stages[i]
            if i < 4:
                # Stage with checkmark
                draw_checkmark(draw, tx + 14, tcy, color=(16, 185, 129, 255), width=2)
                draw.text((tx + 28, tcy), line_txt, font=font_term, fill=(203, 213, 225, 235))
            else:
                # Stage with prompt arrow
                draw_prompt_arrow(draw, tx + 14, tcy, color=(34, 211, 238, 255), width=2)
                text_col = (34, 211, 238, 250) if '3000' in line_txt else (248, 250, 252, 245)
                draw.text((tx + 24, tcy), line_txt, font=font_term, fill=text_col)
            tcy += 18

        if revealed_count == 6 and show_cursor:
            draw_prompt_arrow(draw, tx + 14, tcy + 2, color=(34, 211, 238, 255), width=2)
            draw.text((tx + 24, tcy), '█', font=font_term, fill=(34, 211, 238, 220))

        # ----------------------------------------------------
        # 6. Vignette Overlay for Seamless Dark Integration
        # ----------------------------------------------------
        vignette = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        v_draw = ImageDraw.Draw(vignette)
        for y_v in range(12):
            alpha = int((1.0 - y_v / 12.0) * 120)
            v_draw.line([(0, y_v), (w, y_v)], fill=(8, 11, 20, alpha))
        for y_v in range(15):
            alpha = int((y_v / 15.0) * 160)
            v_draw.line([(0, h - 15 + y_v), (w, h - 15 + y_v)], fill=(8, 11, 20, alpha))
        for x_v in range(10):
            alpha = int((1.0 - x_v / 10.0) * 100)
            v_draw.line([(x_v, 0), (x_v, h)], fill=(8, 11, 20, alpha))
        for x_v in range(10):
            alpha = int((x_v / 10.0) * 100)
            v_draw.line([(w - 10 + x_v, 0), (w - 10 + x_v, h)], fill=(8, 11, 20, alpha))

        # Composite frame: base -> glow -> overlay -> vignette
        composed = Image.alpha_composite(base_img, glow_layer)
        composed = Image.alpha_composite(composed, frame_overlay)
        composed = Image.alpha_composite(composed, vignette)
        frames.append(composed.convert('RGB'))

    # Save frames for inspection
    frames[0].save('scratch/behind_the_code_frame0.png')
    frames[28].save('scratch/behind_the_code_frame28.png')
    print("Test frames saved to scratch/behind_the_code_frame0.png and frame28.png")

    # Generate optimized GIF
    gif_out_path = 'assets/behind-the-code.gif'
    palette_frames = []
    palette_img = frames[0].quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    
    for f in frames:
        pf = f.quantize(colors=256, palette=palette_img, dither=Image.Dither.NONE)
        palette_frames.append(pf)

    palette_frames[0].save(
        gif_out_path,
        save_all=True,
        append_images=palette_frames[1:],
        duration=250, # 250ms * 36 = 9000ms = 9.0 seconds loop
        loop=0,
        optimize=True
    )
    
    size_mb = os.path.getsize(gif_out_path) / (1024 * 1024)
    print(f"Generated {gif_out_path} ({len(frames)} frames, 9.0s loop, {size_mb:.2f} MB)")

if __name__ == '__main__':
    create_behind_the_code()
