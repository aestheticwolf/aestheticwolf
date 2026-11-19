import xml.etree.ElementTree as ET

HEADERS = [
    {
        "filename": "assets/section-02-workspace-header.svg",
        "accent": "#22D3EE",
        "alt_accent": "#38BDF8",
        "num": "02",
        "label": "02 // RUNTIME • DEV WORKSPACE &amp; HARDWARE",
        "heading": "DEVELOPER WORKSPACE",
        "sub_pre": '"A high-performance engineering environment tailored for ',
        "sub_highlight": 'speed, precision',
        "sub_mid": ', and ',
        "sub_highlight2": 'modern full-stack workflows',
        "sub_post": '."',
    },
    {
        "filename": "assets/section-03-about-header.svg",
        "accent": "#A78BFA",
        "alt_accent": "#C084FC",
        "num": "03",
        "label": "03 // IDENTITY • ACADEMIC RIGOR &amp; PRODUCTION ENGINEERING",
        "heading": "ABOUT &amp; PROFESSIONAL BACKGROUND",
        "sub_pre": '"Merging ',
        "sub_highlight": 'academic computer science rigor',
        "sub_mid": ' with ',
        "sub_highlight2": 'production full-stack engineering',
        "sub_post": '."',
    },
    {
        "filename": "assets/section-04-tech-header.svg",
        "accent": "#60A5FA",
        "alt_accent": "#3B82F6",
        "num": "04",
        "label": "04 // ARCHITECTURE • 5 TIERS &amp; 19 PRODUCTION TECHNOLOGIES",
        "heading": "TECHNOLOGY ECOSYSTEM",
        "sub_pre": '"Official production technology stack across ',
        "sub_highlight": 'core languages, frontend, backend',
        "sub_mid": ', ',
        "sub_highlight2": 'databases, and tooling',
        "sub_post": '."',
    },
    {
        "filename": "assets/section-05-projects-header.svg",
        "accent": "#C084FC",
        "alt_accent": "#A855F7",
        "num": "05",
        "label": "05 // SHOWCASE • FEATURED PRODUCTION REPOSITORIES",
        "heading": "SELECTED PROJECTS",
        "sub_pre": '"Engineering ideas into ',
        "sub_highlight": 'robust, user-centric',
        "sub_mid": ', and ',
        "sub_highlight2": 'scalable digital realities',
        "sub_post": '."',
    },
    {
        "filename": "assets/section-06-analytics-header.svg",
        "accent": "#38BDF8",
        "alt_accent": "#0284C7",
        "num": "06",
        "label": "06 // TELEMETRY • GITHUB ACTIVITY &amp; METRICS",
        "heading": "GITHUB ANALYTICS",
        "sub_pre": '"An overview of my ',
        "sub_highlight": 'development activity',
        "sub_mid": ', repositories, and ',
        "sub_highlight2": 'contribution history',
        "sub_post": '."',
    },
    {
        "filename": "assets/section-07-trajectory-header.svg",
        "accent": "#34D399",
        "alt_accent": "#10B981",
        "num": "07",
        "label": "07 // TRAJECTORY • 52-WEEK COMMIT STREAM",
        "heading": "CONTRIBUTION TRAJECTORY",
        "sub_pre": '"Every contribution represents ',
        "sub_highlight": 'another step in my development journey',
        "sub_mid": '',
        "sub_highlight2": '',
        "sub_post": '."',
    },
]

def generate_headers():
    for h in HEADERS:
        tspan2 = f'<tspan fill="{h["accent"]}" font-weight="600">{h["sub_highlight2"]}</tspan>' if h["sub_highlight2"] else ''
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 84" width="100%" fill="none">
  <defs>
    <linearGradient id="lineGrad_{h["num"]}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{h["accent"]}" stop-opacity="0.9" />
      <stop offset="40%" stop-color="{h["accent"]}" stop-opacity="0.4" />
      <stop offset="100%" stop-color="{h["accent"]}" stop-opacity="0" />
    </linearGradient>
    <filter id="glow_{h["num"]}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
    </filter>
  </defs>

  <style>
    .f-mono {{ font-family: "JetBrains Mono", "SF Mono", Consolas, Menlo, monospace; }}
    .f-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    @keyframes pulse_{h["num"]} {{
      0%, 100% {{ transform: scale(1); opacity: 0.6; }}
      50% {{ transform: scale(1.4); opacity: 1; }}
    }}
    .beacon_{h["num"]} {{
      transform-origin: 8px 16px;
      animation: pulse_{h["num"]} 2.5s infinite ease-in-out;
    }}
  </style>

  <!-- Section Marker: Small Uppercase Label with Glowing Indicator -->
  <g transform="translate(4, 0)">
    <!-- Pulsing Beacon -->
    <circle cx="8" cy="16" r="3" fill="{h["accent"]}" />
    <circle cx="8" cy="16" r="5.5" fill="none" stroke="{h["accent"]}" stroke-width="1.2" class="beacon_{h["num"]}" />
    <text x="24" y="20" class="f-mono" font-size="11" font-weight="700" fill="{h["accent"]}" letter-spacing="2.2">{h["label"]}</text>
  </g>

  <!-- Main Section Heading -->
  <text x="4" y="48" class="f-sans" font-size="22" font-weight="800" fill="#F5F5F7" letter-spacing="1.4">{h["heading"]}</text>

  <!-- Decorative Gradient Laser Trace -->
  <line x1="4" y1="56" x2="420" y2="56" stroke="url(#lineGrad_{h["num"]})" stroke-width="1.5" />

  <!-- Subtitle with Selective Colored Phrases -->
  <text x="4" y="74" class="f-sans" font-size="13" fill="#94A3B8" font-style="italic">
    {h["sub_pre"]}<tspan fill="{h["accent"]}" font-weight="600">{h["sub_highlight"]}</tspan>{h["sub_mid"]}{tspan2}{h["sub_post"]}
  </text>
</svg>'''

        # Verify XML validity
        ET.fromstring(svg)

        with open(h["filename"], 'w', encoding='utf-8') as f:
            f.write(svg.strip() + '\n')
        print(f"Generated {h['filename']}")

if __name__ == '__main__':
    generate_headers()
