#!/usr/bin/env python3
"""
Generates the 2026 Contact Hero, Social Cards, and Signature Footer assets
for Richard D'Souza (aestheticwolf).
Strict adherence to the 2026 Dark Portfolio Design System:
- Palette: #08090D (base), #111522 / #151A29 (cards), #282E44 (borders)
- Accents: Violet (#A78BFA), Electric Blue (#60A5FA), Cyan (#22D3EE), Teal (#34D399)
- Editorial typography, animated gradients, subtle scanning highlights, zero dead space.
"""

import os

def create_contact_hero():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 135" width="100%" height="100%">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#111522" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#08090D" stop-opacity="0.98" />
    </linearGradient>

    <!-- Animated Gradient for EXTRAORDINARY -->
    <linearGradient id="extraordinaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A78BFA">
        <animate attributeName="stop-color" values="#A78BFA;#60A5FA;#22D3EE;#A78BFA" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#60A5FA">
        <animate attributeName="stop-color" values="#60A5FA;#22D3EE;#A78BFA;#60A5FA" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#22D3EE">
        <animate attributeName="stop-color" values="#22D3EE;#A78BFA;#60A5FA;#22D3EE" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Animated Divider Line with Laser Scan -->
    <linearGradient id="contactLineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A78BFA" stop-opacity="0" />
      <stop offset="30%" stop-color="#8B5CF6" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#60A5FA" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0" />
    </linearGradient>

    <radialGradient id="cornerGlow" cx="90%" cy="20%" r="60%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0" />
    </radialGradient>

    <filter id="textGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style><![CDATA[
    .mono { font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  ]]></style>

  <!-- Container Chassis -->
  <rect width="1000" height="135" rx="14" fill="url(#heroBg)" stroke="#1F283D" stroke-width="1.2" />
  <rect width="1000" height="135" rx="14" fill="url(#cornerGlow)" />

  <!-- 01. Category Label with Live Pulsing Dot -->
  <g transform="translate(36, 26)">
    <circle cx="6" cy="6" r="3.5" fill="#34D399" />
    <circle cx="6" cy="6" r="6.5" fill="none" stroke="#34D399" stroke-width="1.2" opacity="0.6">
      <animate attributeName="r" values="3.5;8;3.5" dur="2.4s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2.4s" repeatCount="indefinite" />
    </circle>
    <text x="20" y="10" class="mono" font-size="10.5" font-weight="700" fill="#22D3EE">LET'S CONNECT / GET IN TOUCH</text>
    <text x="238" y="10" class="sans" font-size="11" fill="#4B5563">•</text>
    <text x="252" y="10" class="mono" font-size="10" font-weight="600" fill="#A1A1AA">OPEN FOR COLLABORATION &amp; INQUIRIES</text>
  </g>

  <!-- 02. Main Editorial Heading -->
  <g transform="translate(36, 68)">
    <text x="0" y="0" class="sans" font-size="26" font-weight="800" fill="#FFFFFF" letter-spacing="-0.5">
      LET'S BUILD SOMETHING <tspan fill="url(#extraordinaryGrad)" filter="url(#textGlow)">EXTRAORDINARY.</tspan>
    </text>
  </g>

  <!-- 03. Supporting Introduction with Highlighted Phrases -->
  <g transform="translate(36, 96)">
    <text x="0" y="0" class="sans" font-size="13" fill="#A1A1AA">
      Have an idea, a project, or an interesting technical challenge? <tspan fill="#22D3EE" font-weight="600">Let's connect</tspan> and build something <tspan fill="#A78BFA" font-weight="600">meaningful together</tspan>.
    </text>
  </g>

  <!-- 04. Bottom Divider Line with Animated Laser Scan -->
  <rect x="24" y="118" width="952" height="1" fill="url(#contactLineGrad)" />
  <rect x="24" y="118" width="130" height="1" fill="#22D3EE" opacity="0.9">
    <animate attributeName="x" values="24;822;24" dur="8s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.2;1;0.2" dur="8s" repeatCount="indefinite" />
  </rect>
</svg>
"""
    return svg

def create_social_card(platform, handle, tagline, href, color, icon_svg):
    card_border_id = f"border_{platform}"
    card_glow_id = f"glow_{platform}"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 88" width="100%" height="100%">
  <defs>
    <linearGradient id="{card_border_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.6">
        <animate attributeName="stop-color" values="{color};#A78BFA;{color}" dur="6s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#282E44" stop-opacity="0.7" />
      <stop offset="100%" stop-color="{color}" stop-opacity="0.3" />
    </linearGradient>

    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#121726" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0B0E17" stop-opacity="0.98" />
    </linearGradient>

    <filter id="{card_glow_id}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <style><![CDATA[
    .mono {{ font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .card-box:hover {{
      cursor: pointer;
    }}
  ]]></style>

  <!-- Card Chassis -->
  <g filter="url(#{card_glow_id})">
    <rect x="2" y="2" width="306" height="84" rx="13" fill="url(#cardBg)" stroke="url(#{card_border_id})" stroke-width="1.3" />
  </g>

  <!-- Icon Circle Badge -->
  <g transform="translate(18, 18)">
    <circle cx="24" cy="24" r="23" fill="#161C2C" stroke="#283550" stroke-width="1" />
    <g transform="translate(12, 12)">
      {icon_svg}
    </g>
  </g>

  <!-- Platform Information -->
  <g transform="translate(76, 26)">
    <text x="0" y="14" class="sans" font-size="15" font-weight="700" fill="#FFFFFF">{platform}</text>
    <text x="0" y="32" class="mono" font-size="11" font-weight="600" fill="{color}">{handle}</text>
    <text x="0" y="47" class="sans" font-size="9.5" fill="#71717A">{tagline}</text>
  </g>

  <!-- External Link Indicator Pill -->
  <g transform="translate(242, 18)">
    <rect x="0" y="0" width="50" height="22" rx="11" fill="#141B2B" stroke="{color}" stroke-width="0.8" />
    <text x="21" y="14" class="sans" font-size="9.5" font-weight="700" fill="{color}">GO</text>
    <text x="35" y="14" class="sans" font-size="11" font-weight="700" fill="{color}">↗</text>
  </g>
</svg>
"""
    return svg

def create_footer():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 135" width="100%" height="100%">
  <defs>
    <!-- Top Divider Line Gradient -->
    <linearGradient id="ftDivider" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0" />
      <stop offset="25%" stop-color="#8B5CF6" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.9" />
      <stop offset="75%" stop-color="#3B82F6" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0" />
    </linearGradient>

    <!-- Gradient for Name -->
    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A78BFA">
        <animate attributeName="stop-color" values="#A78BFA;#60A5FA;#22D3EE;#A78BFA" dur="9s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#60A5FA">
        <animate attributeName="stop-color" values="#60A5FA;#22D3EE;#A78BFA;#60A5FA" dur="9s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#22D3EE">
        <animate attributeName="stop-color" values="#22D3EE;#A78BFA;#60A5FA;#22D3EE" dur="9s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Subtle Ambient Footer Floor Glow -->
    <radialGradient id="footerGlow" cx="50%" cy="0%" r="65%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.08" />
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#08090D" stop-opacity="0" />
    </radialGradient>

    <filter id="emblemGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style><![CDATA[
    .mono { font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  ]]></style>

  <!-- Footer Ambient Floor -->
  <rect width="1000" height="135" fill="url(#footerGlow)" />

  <!-- Top Animated Divider Line -->
  <rect x="40" y="2" width="920" height="1" fill="url(#ftDivider)" />
  <rect x="40" y="2" width="160" height="1" fill="#22D3EE" opacity="0.9">
    <animate attributeName="x" values="40;800;40" dur="10s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.2;1;0.2" dur="10s" repeatCount="indefinite" />
  </rect>

  <!-- Center Animated Geometric Emblem -->
  <g transform="translate(500, 28)">
    <!-- Rotating Ring -->
    <circle cx="0" cy="0" r="14" fill="#101524" stroke="#283552" stroke-width="1.2" />
    <circle cx="0" cy="0" r="14" fill="none" stroke="#22D3EE" stroke-width="1.2" stroke-dasharray="8 14" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite" />
    </circle>
    <!-- Core Diamond -->
    <polygon points="0,-6 6,0 0,6 -6,0" fill="#A78BFA" filter="url(#emblemGlow)">
      <animate attributeName="fill" values="#A78BFA;#22D3EE;#60A5FA;#A78BFA" dur="6s" repeatCount="indefinite" />
    </polygon>
  </g>

  <!-- Signature Statement -->
  <g transform="translate(500, 62)" text-anchor="middle">
    <text y="0" class="mono" font-size="11" font-weight="700" fill="#A1A1AA" letter-spacing="3.5">
      ENGINEERED WITH PASSION &amp; PRECISION
    </text>
  </g>

  <!-- Name in Animated Gradient -->
  <g transform="translate(500, 94)" text-anchor="middle">
    <text y="0" class="sans" font-size="24" font-weight="800" fill="url(#nameGrad)" letter-spacing="2">
      RICHARD D'SOUZA
    </text>
  </g>

  <!-- Professional Metadata Line -->
  <g transform="translate(500, 118)" text-anchor="middle">
    <text y="0" class="mono" font-size="10" font-weight="600" fill="#64748B" letter-spacing="1.5">
      2026 DIGITAL WORKSPACE • GOA, INDIA • @AESTHETICWOLF • ALL SYSTEMS OPERATIONAL
    </text>
  </g>
</svg>
"""
    return svg

def create_back_to_top():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 32" width="160" height="32">
  <defs>
    <linearGradient id="btnBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#282E44" />
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#282E44" />
    </linearGradient>
  </defs>
  <style><![CDATA[
    .mono { font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }
  ]]></style>
  <rect x="1" y="1" width="158" height="30" rx="15" fill="#111522" stroke="url(#btnBorder)" stroke-width="1.2" />
  <g transform="translate(80, 20)" text-anchor="middle">
    <text y="0" class="mono" font-size="10" font-weight="700" fill="#22D3EE" letter-spacing="1">▲ BACK TO TOP</text>
  </g>
</svg>
"""
    return svg

def main():
    assets_dir = r"a:\0\a\repo\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # 1. Contact Hero
    hero_svg = create_contact_hero()
    with open(os.path.join(assets_dir, "contact-hero.svg"), "w", encoding="utf-8") as f:
        f.write(hero_svg)
    print("Saved assets/contact-hero.svg")

    # 2. Social Cards
    # GitHub Icon SVG
    github_icon = """<path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" fill="#FFFFFF"/>"""
    gh_card = create_social_card("GitHub", "@aestheticwolf", "Repositories &amp; Codebase", "https://github.com/aestheticwolf", "#22D3EE", github_icon)
    with open(os.path.join(assets_dir, "social-github.svg"), "w", encoding="utf-8") as f:
        f.write(gh_card)
    print("Saved assets/social-github.svg")

    # LinkedIn Icon SVG
    linkedin_icon = """<path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" fill="#0A66C2"/>"""
    li_card = create_social_card("LinkedIn", "in/richarddsouza29", "Professional Network", "https://linkedin.com/in/richarddsouza29", "#60A5FA", linkedin_icon)
    with open(os.path.join(assets_dir, "social-linkedin.svg"), "w", encoding="utf-8") as f:
        f.write(li_card)
    print("Saved assets/social-linkedin.svg")

    # Portfolio Icon SVG
    portfolio_icon = """<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="#10B981"/>"""
    pf_card = create_social_card("Live Portfolio", "richard-portfolio", "Interactive Web Projects", "https://richard-portfolio-website-ten.vercel.app", "#10B981", portfolio_icon)
    with open(os.path.join(assets_dir, "social-portfolio.svg"), "w", encoding="utf-8") as f:
        f.write(pf_card)
    print("Saved assets/social-portfolio.svg")

    # 3. Signature Footer
    footer_svg = create_footer()
    with open(os.path.join(assets_dir, "footer.svg"), "w", encoding="utf-8") as f:
        f.write(footer_svg)
    print("Saved assets/footer.svg")

    # 4. Back To Top
    btt_svg = create_back_to_top()
    with open(os.path.join(assets_dir, "back-to-top.svg"), "w", encoding="utf-8") as f:
        f.write(btt_svg)
    print("Saved assets/back-to-top.svg")

if __name__ == "__main__":
    main()
