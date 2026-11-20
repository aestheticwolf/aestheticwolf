import os
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def generate_workspace_network():
    print("==================================================")
    print("GENERATING DEVELOPER WORKSPACE: DIGITAL CORE & CONNECTED NETWORK")
    print("==================================================")

    w, h = 1000, 480
    num_frames = 30
    frame_duration_ms = 100  # 30 frames x 100ms = 3,000ms (3.0s) exact loop
    
    # Fonts
    try:
        font_mono_lg = ImageFont.truetype("consola.ttf", 13)
        font_mono_md = ImageFont.truetype("consola.ttf", 11)
        font_mono_sm = ImageFont.truetype("consola.ttf", 9)
        font_sans_bold = ImageFont.truetype("arialbd.ttf", 13)
        font_core = ImageFont.truetype("arialbd.ttf", 12)
    except:
        font_mono_lg = ImageFont.load_default()
        font_mono_md = ImageFont.load_default()
        font_mono_sm = ImageFont.load_default()
        font_sans_bold = ImageFont.load_default()
        font_core = ImageFont.load_default()

    # Central Core position
    cx, cy = 500, 245

    # 13 Connected Technology Nodes
    # Each node has: id, label, category, x, y, color (RGB), bg_color, links
    nodes = [
        # Top Cluster
        {
            'id': 'nextjs', 'label': 'Next.js', 'cat': 'FRONTEND',
            'x': 370, 'y': 95, 'color': (226, 232, 240), 'accent': (248, 250, 252),
            'links': ['react', 'core']
        },
        {
            'id': 'firebase', 'label': 'Firebase', 'cat': 'CLOUD DB',
            'x': 500, 'y': 80, 'color': (255, 202, 40), 'accent': (245, 158, 11),
            'links': ['core', 'flutter']
        },
        {
            'id': 'python', 'label': 'Python', 'cat': 'LANGUAGE',
            'x': 630, 'y': 95, 'color': (96, 165, 250), 'accent': (59, 130, 246),
            'links': ['core', 'fastapi', 'ai']
        },
        
        # Left Cluster (Frontend & Mobile)
        {
            'id': 'react', 'label': 'React', 'cat': 'UI LIBRARY',
            'x': 250, 'y': 145, 'color': (97, 218, 251), 'accent': (34, 211, 238),
            'links': ['core', 'typescript', 'reactnative']
        },
        {
            'id': 'typescript', 'label': 'TypeScript', 'cat': 'CORE TYPING',
            'x': 130, 'y': 240, 'color': (49, 120, 198), 'accent': (96, 165, 250),
            'links': ['core', 'javascript', 'react']
        },
        {
            'id': 'reactnative', 'label': 'React Native', 'cat': 'MOBILE UI',
            'x': 230, 'y': 335, 'color': (56, 189, 248), 'accent': (34, 211, 238),
            'links': ['core', 'javascript']
        },
        {
            'id': 'javascript', 'label': 'JavaScript', 'cat': 'RUNTIME',
            'x': 135, 'y': 385, 'color': (247, 223, 30), 'accent': (250, 204, 21),
            'links': ['typescript']
        },

        # Right Cluster (Backend, AI & Ecosystem)
        {
            'id': 'fastapi', 'label': 'FastAPI', 'cat': 'ASYNC API',
            'x': 750, 'y': 145, 'color': (45, 212, 191), 'accent': (20, 184, 166),
            'links': ['core', 'python', 'nodejs']
        },
        {
            'id': 'nodejs', 'label': 'Node.js', 'cat': 'BACKEND',
            'x': 870, 'y': 240, 'color': (34, 197, 94), 'accent': (74, 222, 128),
            'links': ['core', 'postgresql']
        },
        {
            'id': 'ai', 'label': 'AI / LLMs', 'cat': 'INTELLIGENCE',
            'x': 770, 'y': 335, 'color': (168, 85, 247), 'accent': (192, 132, 252),
            'links': ['core', 'python']
        },
        {
            'id': 'git', 'label': 'Git', 'cat': 'DEV SYSTEM',
            'x': 865, 'y': 385, 'color': (248, 113, 113), 'accent': (239, 68, 68),
            'links': ['nodejs']
        },

        # Bottom Cluster (Databases & Cross-Platform)
        {
            'id': 'flutter', 'label': 'Flutter', 'cat': 'CROSS-PLATFORM',
            'x': 365, 'y': 415, 'color': (56, 189, 248), 'accent': (2, 136, 209),
            'links': ['core']
        },
        {
            'id': 'postgresql', 'label': 'PostgreSQL', 'cat': 'SQL RELATIONAL',
            'x': 500, 'y': 420, 'color': (96, 165, 250), 'accent': (59, 130, 246),
            'links': ['core', 'mongodb']
        },
        {
            'id': 'mongodb', 'label': 'MongoDB', 'cat': 'DOCUMENT STORE',
            'x': 635, 'y': 415, 'color': (34, 197, 94), 'accent': (16, 185, 129),
            'links': ['core']
        }
    ]

    # Map node id to node object
    node_map = {n['id']: n for n in nodes}

    # Pulse particles travelling along connections
    # We create a deterministic set of data packets
    random.seed(2026)
    packets = []
    # Core to each node
    for i, n in enumerate(nodes):
        packets.append({
            'from': (cx, cy),
            'to': (n['x'], n['y']),
            'phase': i / float(len(nodes)),
            'color': n['accent'],
            'speed': 1.0
        })
    # Node to node connections
    inter_links = [
        ('react', 'typescript'), ('react', 'reactnative'), ('python', 'fastapi'),
        ('python', 'ai'), ('fastapi', 'nodejs'), ('nodejs', 'postgresql'),
        ('postgresql', 'mongodb'), ('firebase', 'nextjs')
    ]
    for i, (n1_id, n2_id) in enumerate(inter_links):
        n1 = node_map[n1_id]
        n2 = node_map[n2_id]
        packets.append({
            'from': (n1['x'], n1['y']),
            'to': (n2['x'], n2['y']),
            'phase': (i * 0.23) % 1.0,
            'color': (34, 211, 238),
            'speed': 1.0
        })

    # Ambient background particles
    ambient_particles = []
    for _ in range(35):
        ambient_particles.append({
            'x': random.uniform(40, w - 40),
            'y': random.uniform(60, h - 40),
            'radius': random.uniform(1.0, 2.5),
            'color': random.choice([(34, 211, 238), (139, 92, 246), (59, 130, 246), (16, 185, 129)]),
            'alpha': random.uniform(0.2, 0.7),
            'drift_x': random.uniform(-10, 10),
            'drift_y': random.uniform(-15, 15)
        })

    # Pre-render base background canvas
    base_bg = Image.new('RGBA', (w, h), (8, 11, 20, 255))
    draw_bg = ImageDraw.Draw(base_bg)

    # 1. Background radial ambient washes
    # Left violet glow, center cyan glow, right blue glow
    glow_arr = np.zeros((h, w, 3), dtype=np.float32)
    # Base dark color
    glow_arr[:, :] = [8, 11, 20]

    y_coords, x_coords = np.ogrid[:h, :w]

    # Center Cyan Core radial aura
    dist_core = np.sqrt((x_coords - cx)**2 + (y_coords - cy)**2)
    glow_core = np.clip(1.0 - dist_core / 240.0, 0, 1.0) ** 1.8
    for c, val in enumerate([34, 211, 238]):  # Cyan
        glow_arr[:, :, c] += glow_core * val * 0.16

    # Left Violet ambient
    dist_left = np.sqrt((x_coords - 200)**2 + (y_coords - 240)**2)
    glow_left = np.clip(1.0 - dist_left / 280.0, 0, 1.0) ** 2.0
    for c, val in enumerate([139, 92, 246]):  # Violet
        glow_arr[:, :, c] += glow_left * val * 0.14

    # Right Electric Blue ambient
    dist_right = np.sqrt((x_coords - 800)**2 + (y_coords - 240)**2)
    glow_right = np.clip(1.0 - dist_right / 280.0, 0, 1.0) ** 2.0
    for c, val in enumerate([59, 130, 246]):  # Electric Blue
        glow_arr[:, :, c] += glow_right * val * 0.13

    base_bg = Image.fromarray(np.clip(glow_arr, 0, 255).astype(np.uint8)).convert('RGBA')
    draw_bg = ImageDraw.Draw(base_bg)

    # 2. Subtle technical grid
    grid_spacing = 36
    for gx in range(grid_spacing, w, grid_spacing):
        draw_bg.line([(gx, 0), (gx, h)], fill=(34, 211, 238, 10), width=1)
    for gy in range(grid_spacing, h, grid_spacing):
        draw_bg.line([(0, gy), (w, gy)], fill=(34, 211, 238, 10), width=1)

    # 3. Outer chassis border & cybernetic corner brackets
    draw_bg.rounded_rectangle([2, 2, w - 3, h - 3], radius=16, outline=(41, 46, 64), width=1)

    # Corner crosshairs
    def draw_crosshair(x, y):
        draw_bg.line([(x - 6, y), (x + 6, y)], fill=(34, 211, 238, 100), width=1)
        draw_bg.line([(x, y - 6), (x, y + 6)], fill=(34, 211, 238, 100), width=1)

    draw_crosshair(24, 24)
    draw_crosshair(w - 24, 24)
    draw_crosshair(24, h - 24)
    draw_crosshair(w - 24, h - 24)

    # 4. Top Telemetry Status Bar
    # Status pill left
    draw_bg.rounded_rectangle([24, 18, 236, 42], radius=12, fill=(16, 21, 36), outline=(139, 92, 246, 120), width=1)
    draw_bg.ellipse([34, 26, 42, 34], fill=(16, 185, 129))  # Emerald beacon
    draw_bg.text((48, 24), "DIGITAL WORKSPACE CORE", font=font_mono_sm, fill=(245, 245, 247))

    # Right telemetry text
    telemetry_label = "INTERCONNECTED TECHNOLOGY NETWORK • DISTRIBUTED RUNTIME"
    draw_bg.text((w - 28, 24), telemetry_label, font=font_mono_sm, fill=(148, 163, 184), anchor="ra")

    # Render all 30 frames
    frames = []

    for f_idx in range(num_frames):
        t = f_idx / float(num_frames)  # 0.0 to 1.0
        frame = base_bg.copy()
        draw = ImageDraw.Draw(frame)

        # 1. Floating ambient particles
        for p in ambient_particles:
            px = p['x'] + p['drift_x'] * math.sin(t * 2 * math.pi)
            py = p['y'] + p['drift_y'] * math.cos(t * 2 * math.pi)
            alpha_pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi + p['x'])
            p_color = p['color'] + (int(255 * p['alpha'] * alpha_pulse),)
            draw.ellipse([px - p['radius'], py - p['radius'], px + p['radius'], py + p['radius']], fill=p_color)

        # 2. Connection lines (Circuits from Core to Nodes)
        for n in nodes:
            # Draw subtle circuit vector line
            draw.line([(cx, cy), (n['x'], n['y'])], fill=(30, 41, 59, 160), width=1)
            # Pulsing overlay line
            pulse_alpha = int(40 + 35 * math.sin(t * 2 * math.pi + (n['x'] + n['y']) * 0.01))
            draw.line([(cx, cy), (n['x'], n['y'])], fill=(34, 211, 238, pulse_alpha), width=1)

        # Inter-node connections
        for n1_id, n2_id in inter_links:
            n1 = node_map[n1_id]
            n2 = node_map[n2_id]
            draw.line([(n1['x'], n1['y']), (n2['x'], n2['y'])], fill=(139, 92, 246, 50), width=1)

        # 3. Animated data packets travelling along lines
        for pkt in packets:
            p_t = (t * pkt['speed'] + pkt['phase']) % 1.0
            fx, fy = pkt['from']
            tx, ty = pkt['to']
            cur_x = fx + (tx - fx) * p_t
            cur_y = fy + (ty - fy) * p_t

            # Glow aura
            draw.ellipse([cur_x - 3, cur_y - 3, cur_x + 3, cur_y + 3], fill=pkt['color'] + (120,))
            # Core bright dot
            draw.ellipse([cur_x - 1.5, cur_y - 1.5, cur_x + 1.5, cur_y + 1.5], fill=(255, 255, 255, 240))

        # 4. Central Digital Core
        # Concentric rotating rings
        ring1_r = 68
        ring2_r = 52
        ring3_r = 38
        
        # Rotating dashed orbital 1
        angle1 = t * 2 * math.pi
        for seg in range(8):
            a_start = angle1 + seg * (math.pi / 4.0)
            a_end = a_start + math.pi / 7.0
            # Draw arc approximation with small line segments
            arc_pts = []
            for step in range(6):
                sub_a = a_start + (a_end - a_start) * (step / 5.0)
                arc_pts.append((cx + ring1_r * math.cos(sub_a), cy + ring1_r * math.sin(sub_a)))
            draw.line(arc_pts, fill=(34, 211, 238, 140), width=1)

        # Rotating orbital ring 2 (reverse)
        angle2 = -t * 2 * math.pi
        for seg in range(6):
            a_start = angle2 + seg * (math.pi / 3.0)
            a_end = a_start + math.pi / 5.0
            arc_pts = []
            for step in range(5):
                sub_a = a_start + (a_end - a_start) * (step / 4.0)
                arc_pts.append((cx + ring2_r * math.cos(sub_a), cy + ring2_r * math.sin(sub_a)))
            draw.line(arc_pts, fill=(139, 92, 246, 150), width=1)

        # 4 satellite micro-beacons on ring 2
        for b_i in range(4):
            b_angle = angle2 + b_i * (math.pi / 2.0)
            bx = cx + ring2_r * math.cos(b_angle)
            by = cy + ring2_r * math.sin(b_angle)
            draw.ellipse([bx - 2, by - 2, bx + 2, by + 2], fill=(34, 211, 238, 220))

        # Solid Core base
        core_pulse_r = ring3_r + 2.0 * math.sin(t * 2 * math.pi)
        draw.ellipse([cx - core_pulse_r - 4, cy - core_pulse_r - 4, cx + core_pulse_r + 4, cy + core_pulse_r + 4],
                     outline=(34, 211, 238, 80), width=1)
        draw.ellipse([cx - core_pulse_r, cy - core_pulse_r, cx + core_pulse_r, cy + core_pulse_r],
                     fill=(16, 22, 38, 240), outline=(34, 211, 238, 200), width=2)
        
        # Core Emblem & Text
        draw.text((cx, cy - 8), "DIGITAL", font=font_mono_sm, fill=(148, 163, 184), anchor="mm")
        draw.text((cx, cy + 6), "CORE", font=font_core, fill=(34, 211, 238), anchor="mm")

        # 5. Render Technology Satellite Nodes
        for n in nodes:
            nx, ny = n['x'], n['y']
            
            # Subtle node float
            float_y = ny + 2.0 * math.sin(t * 2 * math.pi + (nx * 0.05))

            # Node card box (compact, clean, futuristic)
            card_w, card_h = 108, 38
            x0 = nx - card_w // 2
            y0 = float_y - card_h // 2
            x1 = x0 + card_w
            y1 = y0 + card_h

            # Soft glow under node
            draw.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], radius=8, fill=(13, 19, 33, 180),
                                  outline=n['accent'] + (70,), width=1)
            # Node body
            draw.rounded_rectangle([x0, y0, x1, y1], radius=7, fill=(16, 22, 36, 245),
                                  outline=n['accent'] + (160,), width=1)

            # Left accent stripe
            draw.line([(x0 + 4, y0 + 6), (x0 + 4, y1 - 6)], fill=n['accent'] + (220,), width=2)

            # Active beacon dot
            beacon_alpha = int(180 + 75 * math.sin(t * 2 * math.pi + (nx * 0.02)))
            draw.ellipse([x0 + 12, y0 + 10, x0 + 18, y0 + 16], fill=n['accent'] + (beacon_alpha,))

            # Node Labels
            draw.text((x0 + 24, y0 + 13), n['cat'], font=font_mono_sm, fill=(148, 163, 184), anchor="lm")
            draw.text((x0 + 12, y0 + 26), n['label'], font=font_sans_bold, fill=n['color'], anchor="lm")

        frames.append(frame.convert('RGB'))

    print(f"Rendered {len(frames)} frames. Building adaptive palette...")
    sample_frame = frames[0]
    palette_im = sample_frame.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)

    print("Quantizing frames (dither=NONE for crisp vector lines)...")
    quantized_frames = [f.quantize(palette=palette_im, dither=Image.Dither.NONE) for f in frames]

    out_gif = 'assets/workspace-network.gif'
    print(f"Saving {out_gif}...")
    quantized_frames[0].save(
        out_gif,
        save_all=True,
        append_images=quantized_frames[1:],
        duration=[frame_duration_ms] * num_frames,
        loop=0
    )
    size_mb = os.path.getsize(out_gif) / (1024 * 1024)
    print(f"Saved {out_gif}: {size_mb:.2f} MB ({len(frames)} frames, {num_frames * frame_duration_ms} ms)")

    # Also generate high-fidelity standalone SVG version
    generate_workspace_network_svg()

def generate_workspace_network_svg():
    out_svg = 'assets/workspace-network.svg'
    print(f"Generating vector companion {out_svg}...")
    
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 480" width="100%" fill="none">
  <defs>
    <!-- Background Atmospheric Glows -->
    <radialGradient id="coreGlow" cx="50%" cy="51%" r="35%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.22" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="leftGlow" cx="20%" cy="50%" r="40%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.16" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="rightGlow" cx="80%" cy="50%" r="40%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.16" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <!-- Technical Grid Pattern -->
    <pattern id="netGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#22D3EE" stroke-width="0.5" stroke-opacity="0.04" />
    </pattern>

    <style>
      .f-mono { font-family: "JetBrains Mono", "SF Mono", Consolas, Menlo, monospace; }
      .f-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
      @keyframes pulseCore {
        0%, 100% { transform: scale(1); opacity: 0.85; }
        50% { transform: scale(1.05); opacity: 1; }
      }
      @keyframes rotateCW {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
      @keyframes rotateCCW {
        from { transform: rotate(360deg); }
        to { transform: rotate(0deg); }
      }
      @keyframes dashMove {
        to { stroke-dashoffset: -72; }
      }
      .orbit-cw {
        transform-origin: 500px 245px;
        animation: rotateCW 20s linear infinite;
      }
      .orbit-ccw {
        transform-origin: 500px 245px;
        animation: rotateCCW 15s linear infinite;
      }
      .dash-pulse {
        stroke-dasharray: 8 12;
        animation: dashMove 3s linear infinite;
      }
    </style>
  </defs>

  <!-- Base Canvas -->
  <rect width="1000" height="480" rx="16" fill="#080B14" stroke="#292E40" stroke-width="1.2" />
  <rect width="1000" height="480" rx="16" fill="url(#netGrid)" />
  <rect width="1000" height="480" rx="16" fill="url(#coreGlow)" />
  <rect width="1000" height="480" rx="16" fill="url(#leftGlow)" />
  <rect width="1000" height="480" rx="16" fill="url(#rightGlow)" />

  <!-- Corner Crosshairs -->
  <g stroke="#22D3EE" stroke-opacity="0.35" stroke-width="1">
    <path d="M 18 24 L 30 24 M 24 18 L 24 30" />
    <path d="M 982 24 L 970 24 M 976 18 L 976 30" />
    <path d="M 18 456 L 30 456 M 24 450 L 24 462" />
    <path d="M 982 456 L 970 456 M 976 450 L 976 462" />
  </g>

  <!-- Top Telemetry Status Bar -->
  <g transform="translate(24, 18)">
    <rect width="212" height="24" rx="12" fill="#101524" stroke="rgba(139, 92, 246, 0.4)" stroke-width="1" />
    <circle cx="12" cy="12" r="4" fill="#10B981" />
    <text x="24" y="15.5" class="f-mono" font-size="9" font-weight="700" fill="#F5F5F7" letter-spacing="1.2">DIGITAL WORKSPACE CORE</text>
    
    <text x="952" y="15.5" class="f-mono" font-size="9" fill="#94A3B8" text-anchor="end" letter-spacing="0.8">
      INTERCONNECTED TECHNOLOGY NETWORK • DISTRIBUTED RUNTIME
    </text>
  </g>

  <!-- Network Circuit Lines (Core to Nodes) -->
  <g stroke="rgba(34, 211, 238, 0.18)" stroke-width="1.2">
    <line x1="500" y1="245" x2="370" y2="95" class="dash-pulse" />
    <line x1="500" y1="245" x2="500" y2="80" class="dash-pulse" />
    <line x1="500" y1="245" x2="630" y2="95" class="dash-pulse" />
    <line x1="500" y1="245" x2="250" y2="145" class="dash-pulse" />
    <line x1="500" y1="245" x2="130" y2="240" class="dash-pulse" />
    <line x1="500" y1="245" x2="230" y2="335" class="dash-pulse" />
    <line x1="500" y1="245" x2="750" y2="145" class="dash-pulse" />
    <line x1="500" y1="245" x2="870" y2="240" class="dash-pulse" />
    <line x1="500" y1="245" x2="770" y2="335" class="dash-pulse" />
    <line x1="500" y1="245" x2="365" y2="415" class="dash-pulse" />
    <line x1="500" y1="245" x2="500" y2="420" class="dash-pulse" />
    <line x1="500" y1="245" x2="635" y2="415" class="dash-pulse" />
  </g>

  <!-- Inter-Node Circuit Traces -->
  <g stroke="rgba(139, 92, 246, 0.22)" stroke-width="1">
    <line x1="250" y1="145" x2="130" y2="240" />
    <line x1="250" y1="145" x2="230" y2="335" />
    <line x1="130" y1="240" x2="135" y2="385" />
    <line x1="630" y1="95" x2="750" y2="145" />
    <line x1="630" y1="95" x2="770" y2="335" />
    <line x1="750" y1="145" x2="870" y2="240" />
    <line x1="870" y1="240" x2="865" y2="385" />
    <line x1="500" y1="420" x2="635" y2="415" />
    <line x1="365" y1="415" x2="500" y2="420" />
  </g>

  <!-- Central Digital Core Rings -->
  <g class="orbit-cw">
    <circle cx="500" cy="245" r="68" fill="none" stroke="#22D3EE" stroke-width="1.2" stroke-dasharray="14 10" opacity="0.6" />
    <circle cx="568" cy="245" r="2.5" fill="#22D3EE" />
    <circle cx="432" cy="245" r="2.5" fill="#22D3EE" />
  </g>
  <g class="orbit-ccw">
    <circle cx="500" cy="245" r="52" fill="none" stroke="#8B5CF6" stroke-width="1.2" stroke-dasharray="10 8" opacity="0.65" />
    <circle cx="500" cy="193" r="2.5" fill="#8B5CF6" />
    <circle cx="500" cy="297" r="2.5" fill="#8B5CF6" />
  </g>
  <circle cx="500" cy="245" r="38" fill="#101626" stroke="#22D3EE" stroke-width="1.8" />
  <circle cx="500" cy="245" r="44" fill="none" stroke="#22D3EE" stroke-width="0.8" opacity="0.4" />
  <text x="500" y="240" class="f-mono" font-size="8.5" fill="#94A3B8" text-anchor="middle">DIGITAL</text>
  <text x="500" y="254" class="f-sans" font-size="12" font-weight="800" fill="#22D3EE" text-anchor="middle">CORE</text>

  <!-- Technology Satellite Nodes -->
  <!-- Top: Next.js -->
  <g transform="translate(316, 76)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(248, 250, 252, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#F8FAFC" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#F8FAFC" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">FRONTEND</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#E2E8F0">Next.js</text>
  </g>

  <!-- Top: Firebase -->
  <g transform="translate(446, 61)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(245, 158, 11, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#F59E0B" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#FFCA28" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">CLOUD DB</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#FFCA28">Firebase</text>
  </g>

  <!-- Top: Python -->
  <g transform="translate(576, 76)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(59, 130, 246, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#3B82F6" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#60A5FA" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">LANGUAGE</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#60A5FA">Python</text>
  </g>

  <!-- Left: React -->
  <g transform="translate(196, 126)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(34, 211, 238, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#22D3EE" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#22D3EE" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">UI LIBRARY</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#61DAFB">React</text>
  </g>

  <!-- Left: TypeScript -->
  <g transform="translate(76, 221)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(49, 120, 198, 0.55)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#3178C6" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#60A5FA" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">CORE TYPING</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#93C5FD">TypeScript</text>
  </g>

  <!-- Left: React Native -->
  <g transform="translate(176, 316)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(56, 189, 248, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#38BDF8" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#38BDF8" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">MOBILE UI</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#38BDF8">React Native</text>
  </g>

  <!-- Left: JavaScript -->
  <g transform="translate(81, 366)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(247, 223, 30, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#F7DF1E" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#FACC15" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">RUNTIME</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#FDE047">JavaScript</text>
  </g>

  <!-- Right: FastAPI -->
  <g transform="translate(696, 126)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(45, 212, 191, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#2DD4BF" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#2DD4BF" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">ASYNC API</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#2DD4BF">FastAPI</text>
  </g>

  <!-- Right: Node.js -->
  <g transform="translate(816, 221)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(34, 197, 94, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#22C55E" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#4ADE80" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">BACKEND</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#4ADE80">Node.js</text>
  </g>

  <!-- Right: AI / LLMs -->
  <g transform="translate(716, 316)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(168, 85, 247, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#A855F7" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#C084FC" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">INTELLIGENCE</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#C084FC">AI / LLMs</text>
  </g>

  <!-- Right: Git -->
  <g transform="translate(811, 366)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(248, 113, 113, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#F87171" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#EF4444" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">DEV SYSTEM</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#F87171">Git</text>
  </g>

  <!-- Bottom: Flutter -->
  <g transform="translate(311, 396)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(56, 189, 248, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#0284C7" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#38BDF8" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">MOBILE</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#38BDF8">Flutter</text>
  </g>

  <!-- Bottom: PostgreSQL -->
  <g transform="translate(446, 401)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(96, 165, 250, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#3B82F6" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#60A5FA" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">RELATIONAL</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#93C5FD">PostgreSQL</text>
  </g>

  <!-- Bottom: MongoDB -->
  <g transform="translate(581, 396)">
    <rect width="108" height="38" rx="7" fill="#101624" stroke="rgba(16, 185, 129, 0.45)" stroke-width="1" />
    <line x1="4" y1="6" x2="4" y2="32" stroke="#10B981" stroke-width="2" />
    <circle cx="15" cy="14" r="3" fill="#34D399" />
    <text x="24" y="16" class="f-mono" font-size="7.5" fill="#94A3B8">NO-SQL DB</text>
    <text x="12" y="29" class="f-sans" font-size="11" font-weight="700" fill="#34D399">MongoDB</text>
  </g>
</svg>'''
    with open(out_svg, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Saved {out_svg}")

if __name__ == '__main__':
    generate_workspace_network()
