import base64
import os
import xml.etree.ElementTree as ET
from PIL import Image

def build_hero():
    # 1. Optimize portrait PNG to 700x771 for Retina embedding in SVG
    src_portrait = 'assets/richard-portrait-static.png'
    opt_portrait = 'scratch/portrait_for_svg.png'
    im = Image.open(src_portrait)
    im_opt = im.resize((700, 771), Image.Resampling.LANCZOS)
    im_opt.save(opt_portrait, format='PNG', optimize=True)

    with open(opt_portrait, 'rb') as f:
        b64_data = base64.b64encode(f.read()).decode('utf-8')
    data_uri = f"data:image/png;base64,{b64_data}"
    print(f"Base64 data URI length: {len(data_uri)} chars (~{len(data_uri)/1024:.1f} KB)")

    # 2. Build hero SVG
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 420" width="100%" fill="none">
  <defs>
    <!-- Background Atmospheric Lighting -->
    <radialGradient id="heroVoidGlow" cx="20%" cy="30%" r="65%">
      <animate attributeName="cx" values="20%;25%;20%" dur="16s" repeatCount="indefinite" />
      <animate attributeName="cy" values="30%;26%;30%" dur="16s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.22" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.10" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="heroCyanFocal" cx="78%" cy="45%" r="55%">
      <animate attributeName="cx" values="78%;74%;78%" dur="18s" repeatCount="indefinite" />
      <animate attributeName="cy" values="45%;50%;45%" dur="18s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.28" />
      <stop offset="45%" stop-color="#8B5CF6" stop-opacity="0.14" />
      <stop offset="85%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <!-- Portrait Ambient Underglow -->
    <radialGradient id="portraitBackdropGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.30" />
      <stop offset="40%" stop-color="#3B82F6" stop-opacity="0.18" />
      <stop offset="75%" stop-color="#8B5CF6" stop-opacity="0.10" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <!-- Editorial Name Linear Gradient -->
    <linearGradient id="heroNameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="55%" stop-color="#F1F5F9" />
      <stop offset="85%" stop-color="#E0E7FF" />
      <stop offset="100%" stop-color="#C4B5FD" />
    </linearGradient>

    <!-- Top Laser Accent Rim -->
    <linearGradient id="heroBeamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0" />
      <stop offset="25%" stop-color="#8B5CF6" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="1" />
      <stop offset="75%" stop-color="#22D3EE" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0" />
    </linearGradient>

    <!-- Scanning Laser Gradient -->
    <linearGradient id="laserBeamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0" />
      <stop offset="20%" stop-color="#8B5CF6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="1" />
      <stop offset="80%" stop-color="#3B82F6" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0" />
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="heroGridPattern" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#22D3EE" stroke-width="0.5" stroke-opacity="0.05" />
      <circle cx="36" cy="36" r="0.8" fill="#8B5CF6" fill-opacity="0.25" />
    </pattern>

    <!-- Filter Shadows -->
    <filter id="nameShadow" x="-5%" y="-5%" width="110%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#8B5CF6" flood-opacity="0.2" />
    </filter>

    <filter id="portraitGlowFilter" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="#22D3EE" flood-opacity="0.18" />
      <feDropShadow dx="0" dy="8" stdDeviation="20" flood-color="#8B5CF6" flood-opacity="0.14" />
    </filter>

    <style>
      @keyframes blinkCursor {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      @keyframes pulseBeacon {{
        0%, 100% {{ transform: scale(1); opacity: 0.5; }}
        50% {{ transform: scale(1.3); opacity: 0.95; }}
      }}
      @keyframes floatParticlesSlow {{
        0%, 100% {{ transform: translateY(0px) translateX(0px); }}
        50% {{ transform: translateY(-7px) translateX(3px); }}
      }}
      @keyframes floatParticlesReverse {{
        0%, 100% {{ transform: translateY(0px) translateX(0px); }}
        50% {{ transform: translateY(6px) translateX(-4px); }}
      }}

      /* 5-Phase Rotating Typing Animation (15s cycle: 3s each) */
      @keyframes roleCycle1 {{
        0%, 18% {{ opacity: 1; transform: translateY(0px); }}
        20%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes roleCycle2 {{
        0%, 19% {{ opacity: 0; transform: translateY(4px); }}
        21%, 38% {{ opacity: 1; transform: translateY(0px); }}
        40%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes roleCycle3 {{
        0%, 39% {{ opacity: 0; transform: translateY(4px); }}
        41%, 58% {{ opacity: 1; transform: translateY(0px); }}
        60%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes roleCycle4 {{
        0%, 59% {{ opacity: 0; transform: translateY(4px); }}
        61%, 78% {{ opacity: 1; transform: translateY(0px); }}
        80%, 100% {{ opacity: 0; transform: translateY(-4px); }}
      }}
      @keyframes roleCycle5 {{
        0%, 79% {{ opacity: 0; transform: translateY(4px); }}
        81%, 98% {{ opacity: 1; transform: translateY(0px); }}
        100% {{ opacity: 0; transform: translateY(-4px); }}
      }}

      /* Laser Scan Beam Keyframes: Sweeps down once in 2.4s, then stays invisible */
      @keyframes scanBeamOnce {{
        0% {{ transform: translateY(0px); opacity: 0; }}
        8% {{ opacity: 1; }}
        80% {{ opacity: 0.9; }}
        95% {{ transform: translateY(380px); opacity: 0; }}
        100% {{ transform: translateY(380px); opacity: 0; }}
      }}

      /* Digital Pixel Dissolve: Assembles and dissolves into sharp portrait */
      @keyframes pixelOverlayFade {{
        0% {{ opacity: 0.85; }}
        40% {{ opacity: 0.70; }}
        75% {{ opacity: 0.25; }}
        100% {{ opacity: 0; }}
      }}

      .f-sans {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      }}
      .f-mono {{
        font-family: "JetBrains Mono", "SF Mono", Consolas, Menlo, monospace;
      }}
      .cursor-blink {{
        animation: blinkCursor 0.85s infinite;
      }}
      .pulse-beacon {{
        animation: pulseBeacon 2.5s infinite ease-in-out;
        transform-origin: 60px 50px;
      }}
      .particle-layer1 {{
        animation: floatParticlesSlow 6s ease-in-out infinite;
      }}
      .particle-layer2 {{
        animation: floatParticlesReverse 7s ease-in-out infinite;
      }}

      .rc-1 {{ animation: roleCycle1 15s infinite; }}
      .rc-2 {{ animation: roleCycle2 15s infinite; }}
      .rc-3 {{ animation: roleCycle3 15s infinite; }}
      .rc-4 {{ animation: roleCycle4 15s infinite; }}
      .rc-5 {{ animation: roleCycle5 15s infinite; }}

      .scan-laser {{
        animation: scanBeamOnce 2.6s ease-out forwards;
      }}
      .pixel-dissolve {{
        animation: pixelOverlayFade 2.4s ease-out forwards;
      }}
    </style>
  </defs>

  <!-- Deep Black Base Canvas -->
  <rect width="1000" height="420" rx="18" fill="#080B14" />

  <!-- Multi-layered Ambient Atmosphere Glows -->
  <rect width="1000" height="420" rx="18" fill="url(#heroVoidGlow)" />
  <rect width="1000" height="420" rx="18" fill="url(#heroCyanFocal)" />
  <rect x="1" y="1" width="998" height="418" rx="17" fill="url(#heroGridPattern)" />

  <!-- Architectural Outer Border & Neon Top Accent -->
  <rect x="1" y="1" width="998" height="418" rx="17" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.2" />
  <path d="M 50 1 L 950 1" stroke="url(#heroBeamGrad)" stroke-width="2.5" stroke-linecap="round" />

  <!-- Corner Precision Crosshairs -->
  <g stroke="#22D3EE" stroke-opacity="0.35" stroke-width="1">
    <path d="M 22 28 L 32 28 M 27 23 L 27 33" />
    <path d="M 978 28 L 968 28 M 973 23 L 973 33" />
    <path d="M 22 392 L 32 392 M 27 387 L 27 397" />
    <path d="M 978 392 L 968 392 M 973 387 L 973 397" />
  </g>

  <!-- Floating Ambient Particles -->
  <g class="particle-layer1" fill="#22D3EE" opacity="0.45">
    <circle cx="220" cy="80" r="1.5" />
    <circle cx="480" cy="120" r="1.8" />
    <circle cx="340" cy="340" r="1.2" />
    <circle cx="610" cy="90" r="2" />
  </g>
  <g class="particle-layer2" fill="#8B5CF6" opacity="0.45">
    <circle cx="150" cy="270" r="1.5" />
    <circle cx="560" cy="360" r="1.8" />
    <circle cx="910" cy="140" r="2.2" />
  </g>

  <!-- TOP STATUS BAR -->
  <g transform="translate(48, 38)">
    <rect width="210" height="24" rx="12" fill="#101322" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1" />
    <circle cx="12" cy="12" r="4" fill="#10B981" />
    <circle cx="12" cy="12" r="7" fill="#10B981" class="pulse-beacon" />
    <text x="24" y="15.5" class="f-mono" font-size="9" font-weight="700" fill="#F5F5F7" letter-spacing="1.2">SYSTEM ACTIVE // 2026</text>

    <!-- Geographic & Identity Coordinates -->
    <text x="904" y="16" class="f-mono" font-size="9.5" fill="#8B949E" text-anchor="end" letter-spacing="1">
      GOA, IN • 15.29°N 74.12°E • GITHUB: @AESTHETICWOLF
    </text>
  </g>

  <!-- ==================== LEFT SIDE: EDITORIAL IDENTITY ==================== -->
  <g transform="translate(48, 108)">
    <!-- Professional Domain Label -->
    <text x="0" y="20" class="f-mono" font-size="12" font-weight="700" fill="#8B5CF6" letter-spacing="3.2">
      // SOFTWARE ENGINEER • FULL-STACK DEVELOPER
    </text>

    <!-- Large Editorial Typography: RICHARD D'SOUZA -->
    <text x="0" y="78" class="f-sans" font-size="54" font-weight="900" fill="url(#heroNameGrad)" filter="url(#nameShadow)" letter-spacing="4.5">
      RICHARD D'SOUZA
    </text>

    <!-- Animated Typing Engine -->
    <g transform="translate(0, 114)">
      <rect width="28" height="28" rx="6" fill="#121628" stroke="rgba(34, 211, 238, 0.35)" stroke-width="1" />
      <text x="8.5" y="19" class="f-mono" font-size="15" font-weight="800" fill="#22D3EE">&gt;</text>

      <g transform="translate(38, 0)">
        <text x="0" y="20" class="f-mono rc-1" font-size="19" font-weight="700" fill="#38BDF8">Full-Stack Developer</text>
        <text x="0" y="20" class="f-mono rc-2" font-size="19" font-weight="700" fill="#818CF8">Software Engineer</text>
        <text x="0" y="20" class="f-mono rc-3" font-size="19" font-weight="700" fill="#22D3EE">React &amp; React Native Developer</text>
        <text x="0" y="20" class="f-mono rc-4" font-size="19" font-weight="700" fill="#A78BFA">Backend Developer</text>
        <text x="0" y="20" class="f-mono rc-5" font-size="19" font-weight="700" fill="#67E8F9">AI Application Developer</text>

        <!-- Blinking Terminal Cursor -->
        <line x1="330" y1="3" x2="330" y2="23" stroke="#22D3EE" stroke-width="2.5" class="cursor-blink" />
      </g>
    </g>

    <!-- Short Powerful Professional Introduction (Balanced 2-Line Flow) -->
    <text x="0" y="190" class="f-sans" font-size="15.5" fill="#CBD5E1" letter-spacing="0.2">
      <tspan x="0" dy="0">Architecting <tspan fill="#F5F5F7" font-weight="600">high-performance</tspan> web applications,</tspan>
      <tspan x="0" dy="23">mobile platforms and intelligent software solutions.</tspan>
    </text>
  </g>

  <!-- ==================== RIGHT SIDE: PORTRAIT WITH PIXEL RECONSTRUCTION ==================== -->
  <g transform="translate(625, 24)">
    <!-- Atmospheric Backdrop Aura -->
    <ellipse cx="175" cy="190" rx="175" ry="190" fill="url(#portraitBackdropGlow)" />

    <!-- Cybernetic Targeting Brackets -->
    <g stroke="#22D3EE" stroke-opacity="0.4" stroke-width="1.2" fill="none">
      <path d="M -10 -6 L 14 -6 M -10 -6 L -10 18" />
      <path d="M 360 -6 L 336 -6 M 360 -6 L 360 18" />
      <path d="M -10 392 L 14 392 M -10 392 L -10 368" />
      <path d="M 360 392 L 336 392 M 360 392 L 360 368" />
    </g>

    <!-- Subtle Depth Laser Framing Lines -->
    <line x1="-10" y1="20" x2="-10" y2="360" stroke="#8B5CF6" stroke-width="0.8" stroke-dasharray="6 8" opacity="0.35" />
    <line x1="360" y1="20" x2="360" y2="360" stroke="#22D3EE" stroke-width="0.8" stroke-dasharray="6 8" opacity="0.35" />

    <!-- 01. The Photographically Intact Portrait Image -->
    <g filter="url(#portraitGlowFilter)">
      <image href="{data_uri}" x="0" y="0" width="350" height="386" preserveAspectRatio="xMidYMid meet" />
    </g>

    <!-- 02. Pixel Reconstruction Digital Blocks (Assembles & Dissolves) -->
    <g class="pixel-dissolve" fill="#22D3EE" opacity="0.75">
      <!-- Scattered Digital Pixel Matrix -->
      <rect x="24" y="40" width="12" height="12" fill="#22D3EE" opacity="0.8" />
      <rect x="52" y="80" width="16" height="16" fill="#8B5CF6" opacity="0.7" />
      <rect x="180" y="30" width="14" height="14" fill="#3B82F6" opacity="0.9" />
      <rect x="240" y="70" width="12" height="12" fill="#22D3EE" opacity="0.8" />
      <rect x="290" y="110" width="18" height="18" fill="#A78BFA" opacity="0.6" />
      <rect x="40" y="160" width="14" height="14" fill="#3B82F6" opacity="0.8" />
      <rect x="300" y="190" width="16" height="16" fill="#22D3EE" opacity="0.7" />
      <rect x="310" y="260" width="14" height="14" fill="#8B5CF6" opacity="0.8" />
      <rect x="20" y="270" width="18" height="18" fill="#22D3EE" opacity="0.75" />
      <rect x="80" y="320" width="16" height="16" fill="#3B82F6" opacity="0.7" />
      <rect x="260" y="330" width="14" height="14" fill="#A78BFA" opacity="0.8" />
      
      <!-- Micro-pixel particle accents -->
      <circle cx="110" cy="50" r="3" fill="#FFFFFF" />
      <circle cx="210" cy="120" r="3" fill="#22D3EE" />
      <circle cx="90" cy="220" r="2.5" fill="#8B5CF6" />
      <circle cx="260" cy="210" r="3" fill="#FFFFFF" />
      <circle cx="150" cy="300" r="2.5" fill="#3B82F6" />
    </g>

    <!-- 03. Laser Scanning Beam (Sweeps Once over the Portrait) -->
    <g class="scan-laser">
      <line x1="-15" y1="0" x2="365" y2="0" stroke="url(#laserBeamGrad)" stroke-width="2.2" />
      <circle cx="20" cy="0" r="2" fill="#22D3EE" />
      <circle cx="330" cy="0" r="2" fill="#8B5CF6" />
    </g>

    <!-- 04. Futuristic Cybernetic Telemetry Chip Badge -->
    <g transform="translate(16, 354)">
      <rect width="186" height="24" rx="6" fill="#0D1321" fill-opacity="0.92" stroke="rgba(34, 211, 238, 0.45)" stroke-width="1" />
      <circle cx="12" cy="12" r="3.5" fill="#10B981" />
      <circle cx="12" cy="12" r="6" fill="none" stroke="#10B981" stroke-width="0.8" opacity="0.7">
        <animate attributeName="r" values="3.5;7.5;3.5" dur="3s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="15.5" class="f-mono" font-size="8.5" font-weight="700" fill="#F5F5F7" letter-spacing="1">DEVELOPER IDENTITY</text>
      <text x="144" y="15.5" class="f-mono" font-size="8" font-weight="700" fill="#22D3EE">LIVE</text>
    </g>

    <!-- Mini System Tag Top Right -->
    <g transform="translate(242, 6)">
      <rect width="102" height="18" rx="4" fill="#101424" fill-opacity="0.88" stroke="rgba(139, 92, 246, 0.4)" stroke-width="0.8" />
      <text x="51" y="12.5" class="f-mono" font-size="7.5" font-weight="700" fill="#C4B5FD" text-anchor="middle">RD // PORTFOLIO</text>
    </g>
  </g>
</svg>'''

    # Validate XML
    ET.fromstring(svg_content)

    with open('assets/hero.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content.strip() + '\n')
    print("Successfully built assets/hero.svg with embedded photographic portrait & pixel reconstruction!")

if __name__ == '__main__':
    build_hero()
