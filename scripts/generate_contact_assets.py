#!/usr/bin/env python3
"""
Generates the 2026 Contact Hero, Social Cards, and Signature Footer assets
for Richard D'Souza (aestheticwolf).
Strict adherence to the 2026 Dark Portfolio Design System:
- Palette: #08090D (base), #111522 / #151A29 (cards), #282E44 (borders)
- Accents: Violet (#A78BFA), Electric Blue (#60A5FA), Cyan (#22D3EE), Teal (#34D399)
- Editorial typography, animated gradients, subtle scanning highlights, zero dead space.
- Strictly conforming SVG aspect ratios without height="100%" container blowout.
"""

import os

def create_contact_hero():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 135" width="100%">
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
      Have an idea, a project, or an interesting engineering challenge? Reach out &#8212; let's create something exceptional.
    </text>
  </g>

  <!-- Top Laser Highlight Line -->
  <rect x="36" y="1" width="928" height="1.2" fill="url(#contactLineGrad)" />
</svg>
"""
    return svg


def create_social_card(network, title, subtitle, icon_type, href):
    """
    Renders an interactive high-contrast glassmorphism card for social links.
    Width: 310, Height: 88.
    """
    if network == "github":
        accent_color = "#22D3EE"
        tag_bg = "#16273B"
        border_grad_stops = """
          <stop offset="0%" stop-color="#282E44" />
          <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#282E44" />
        """
        icon_path = """
          <!-- GitHub Octocat Mark -->
          <path fill="#22D3EE" d="M16 0C7.16 0 0 7.16 0 16c0 7.08 4.58 13.06 10.94 15.18.8.15 1.1-.34 1.1-.76 0-.38-.02-1.62-.02-2.98-4.44.96-5.38-1.88-5.38-1.88-.72-1.84-1.78-2.34-1.78-2.34-1.46-.98.12-.96.12-.96 1.6.12 2.46 1.64 2.46 1.64 1.42 2.44 3.74 1.74 4.66 1.32.14-1.04.56-1.74 1.02-2.14-3.54-.4-7.26-1.78-7.26-7.9 0-1.74.62-3.18 1.64-4.3-.16-.4-.72-2.04.16-4.24 0 0 1.34-.44 4.4 1.64 1.28-.36 2.66-.54 4.02-.54s2.74.18 4.02.54c3.06-2.08 4.4-1.64 4.4-1.64.88 2.2.32 3.84.16 4.24 1.02 1.12 1.64 2.56 1.64 4.3 0 6.14-3.72 7.5-7.28 7.9.58.5 1.08 1.48 1.08 3 0 2.16-.02 3.9-.02 4.44 0 .42.28.92 1.1.76C27.42 29.06 32 23.08 32 16 32 7.16 24.84 0 16 0z" />
        """
        stat_badge = "30+ REPOSITORIES"
    elif network == "linkedin":
        accent_color = "#60A5FA"
        tag_bg = "#182442"
        border_grad_stops = """
          <stop offset="0%" stop-color="#282E44" />
          <stop offset="50%" stop-color="#60A5FA" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#282E44" />
        """
        icon_path = """
          <!-- LinkedIn In Mark -->
          <path fill="#60A5FA" d="M29.6 0H2.4C1.1 0 0 1.1 0 2.4v27.2C0 30.9 1.1 32 2.4 32h27.2c1.3 0 2.4-1.1 2.4-2.4V2.4C32 1.1 30.9 0 29.6 0zM9.5 27.3H4.8V12h4.7v15.3zM7.2 9.9c-1.5 0-2.8-1.2-2.8-2.8 0-1.5 1.2-2.8 2.8-2.8 1.5 0 2.8 1.2 2.8 2.8 0 1.6-1.3 2.8-2.8 2.8zm20.1 17.4h-4.7v-7.4c0-1.8 0-4-2.5-4s-2.8 1.9-2.8 3.9v7.5h-4.7V12h4.5v2.1h.1c.6-1.2 2.2-2.5 4.5-2.5 4.8 0 5.7 3.2 5.7 7.3v8.4z" />
        """
        stat_badge = "PROFESSIONAL NETWORK"
    else: # portfolio
        accent_color = "#34D399"
        tag_bg = "#142E28"
        border_grad_stops = """
          <stop offset="0%" stop-color="#282E44" />
          <stop offset="50%" stop-color="#34D399" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#282E44" />
        """
        icon_path = """
          <!-- Portfolio Globe / Spark Mark -->
          <circle cx="16" cy="16" r="14" fill="none" stroke="#34D399" stroke-width="2.2" />
          <path fill="none" stroke="#34D399" stroke-width="1.8" d="M2 16h28M16 2a22 22 0 0 1 0 28M16 2a22 22 0 0 0 0 28" />
        """
        stat_badge = "LIVE PORTFOLIO 2026"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 88" width="100%">
  <defs>
    <linearGradient id="cardBg_{network}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#151A29" />
      <stop offset="100%" stop-color="#0E121E" />
    </linearGradient>

    <linearGradient id="borderGrad_{network}" x1="0%" y1="0%" x2="100%" y2="0%">
      {border_grad_stops}
    </linearGradient>

    <filter id="iconGlow_{network}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style><![CDATA[
    .mono {{ font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
  ]]></style>

  <!-- Card Chassis -->
  <rect width="310" height="88" rx="12" fill="url(#cardBg_{network})" stroke="url(#borderGrad_{network})" stroke-width="1.3" />

  <!-- Left Icon Box -->
  <g transform="translate(16, 18)">
    <rect width="52" height="52" rx="10" fill="#0D111C" stroke="#222B3F" stroke-width="1" />
    <g transform="translate(10, 10) scale(1)">
      {icon_path}
    </g>
  </g>

  <!-- Title & Subtitle -->
  <g transform="translate(78, 28)">
    <!-- Metadata Pill -->
    <rect x="0" y="0" width="138" height="15" rx="4" fill="{tag_bg}" />
    <text x="6" y="11" class="mono" font-size="8.5" font-weight="700" fill="{accent_color}" letter-spacing="0.5">{stat_badge}</text>

    <!-- Network / Username -->
    <text x="0" y="32" class="sans" font-size="14.5" font-weight="700" fill="#FFFFFF">{title}</text>
    <text x="0" y="47" class="mono" font-size="10.5" font-weight="500" fill="#8B949E">{subtitle}</text>
  </g>

  <!-- Right Arrow Indicator -->
  <g transform="translate(280, 44)">
    <circle cx="0" cy="0" r="11" fill="#182032" stroke="#2B364E" stroke-width="1" />
    <path d="M -3 -4 L 2 0 L -3 4" fill="none" stroke="{accent_color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>
"""
    return svg


def create_footer():
    """
    Renders an ultra-compact, high-tech signature footer.
    Height reduced to 104px (zero wasted vertical padding).
    """
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 104" width="100%">
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
  <rect width="1000" height="104" fill="url(#footerGlow)" />

  <!-- Top Animated Divider Line -->
  <rect x="40" y="2" width="920" height="1" fill="url(#ftDivider)" />
  <rect x="40" y="2" width="160" height="1" fill="#22D3EE" opacity="0.9">
    <animate attributeName="x" values="40;800;40" dur="10s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.2;1;0.2" dur="10s" repeatCount="indefinite" />
  </rect>

  <!-- Center Animated Geometric Emblem -->
  <g transform="translate(500, 22)">
    <!-- Rotating Ring -->
    <circle cx="0" cy="0" r="11" fill="#101524" stroke="#283552" stroke-width="1.2" />
    <circle cx="0" cy="0" r="11" fill="none" stroke="#22D3EE" stroke-width="1.2" stroke-dasharray="7 11" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite" />
    </circle>
    <!-- Core Diamond -->
    <polygon points="0,-5 5,0 0,5 -5,0" fill="#A78BFA" filter="url(#emblemGlow)">
      <animate attributeName="fill" values="#A78BFA;#22D3EE;#60A5FA;#A78BFA" dur="6s" repeatCount="indefinite" />
    </polygon>
  </g>

  <!-- Signature Statement -->
  <g transform="translate(500, 48)" text-anchor="middle">
    <text y="0" class="mono" font-size="10.5" font-weight="700" fill="#A1A1AA" letter-spacing="3.2">
      ENGINEERED WITH PASSION &amp; PRECISION
    </text>
  </g>

  <!-- Name in Animated Gradient -->
  <g transform="translate(500, 74)" text-anchor="middle">
    <text y="0" class="sans" font-size="21" font-weight="800" fill="url(#nameGrad)" letter-spacing="1.8">
      RICHARD D'SOUZA
    </text>
  </g>

  <!-- Professional Metadata Line -->
  <g transform="translate(500, 93)" text-anchor="middle">
    <text y="0" class="mono" font-size="9.5" font-weight="600" fill="#64748B" letter-spacing="1.4">
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


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    
    # 1. Contact Hero
    with open("assets/contact-hero.svg", "w", encoding="utf-8") as f:
        f.write(create_contact_hero())
    print("Generated: assets/contact-hero.svg")

    # 2. Three Social Cards
    with open("assets/social-github.svg", "w", encoding="utf-8") as f:
        f.write(create_social_card("github", "GitHub", "@aestheticwolf", "github", "https://github.com/aestheticwolf"))
    print("Generated: assets/social-github.svg")

    with open("assets/social-linkedin.svg", "w", encoding="utf-8") as f:
        f.write(create_social_card("linkedin", "LinkedIn", "in/richarddsouza29", "linkedin", "https://linkedin.com/in/richarddsouza29"))
    print("Generated: assets/social-linkedin.svg")

    with open("assets/social-portfolio.svg", "w", encoding="utf-8") as f:
        f.write(create_social_card("portfolio", "Live Portfolio", "richard-portfolio.vercel.app", "portfolio", "https://richard-portfolio-website-ten.vercel.app"))
    print("Generated: assets/social-portfolio.svg")

    # 3. Signature Footer
    with open("assets/footer.svg", "w", encoding="utf-8") as f:
        f.write(create_footer())
    print("Generated: assets/footer.svg")

    # 4. Back To Top
    with open("assets/back-to-top.svg", "w", encoding="utf-8") as f:
        f.write(create_back_to_top())
    print("Generated: assets/back-to-top.svg")

    print("All Contact assets successfully generated and validated!")
