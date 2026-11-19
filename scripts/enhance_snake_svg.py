#!/usr/bin/env python3
"""
Enhances Platane/snk generated contribution snake SVGs into a futuristic,
cinematic 2026 dark developer portfolio visualization.
Designed for Richard D'Souza (aestheticwolf).

Palette:
- Background: #08090D
- Secondary background: #101522
- Inactive cells: #161D29
- Low contribution: #064E3B
- Medium contribution: #059669
- High contribution: #10B981
- Peak contribution: #34D399
- Accents: Cyan (#22D3EE), Violet (#8B5CF6), Electric Blue (#3B82F6)
"""

import os
import sys
import re

def enhance_snake_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: input file {input_path} not found.")
        return False

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract style block
    style_m = re.search(r"<style>(.*?)</style>", content, re.DOTALL)
    if not style_m:
        print(f"Warning: no <style> block found in {input_path}")
        return False

    snk_css = style_m.group(1)

    # Replace root colors with the 2026 emerald palette
    new_root = (
        ":root{"
        "--cb:#1F2839;"
        "--cs:#22D3EE;"
        "--ce:#161D29;"
        "--c0:#161D29;"
        "--c1:#064E3B;"
        "--c2:#059669;"
        "--c3:#10B981;"
        "--c4:#34D399;"
        "}"
    )
    snk_css = re.sub(r":root\s*\{[^}]+\}", new_root, snk_css)

    # Height adjustment for the .u progress score rects from 12px to 6px
    # to fit cleanly inside our velocity meter track
    # Original snk has: .u{...} and rects with height="12"
    # We will adjust them to fit the track
    extra_css = """
    .mono { font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }

    /* Snake glow and head refinement */
    .s {
      filter: drop-shadow(0 0 5px #22D3EE) drop-shadow(0 0 10px rgba(34, 211, 238, 0.6));
    }
    .s.s0 {
      fill: #FFFFFF !important;
      stroke: #22D3EE !important;
      stroke-width: 1.2px;
    }
    .s.s1, .s.s2, .s.s3 {
      fill: #22D3EE !important;
    }

    /* Peak and high contribution cells subtle glow */
    .c.c4 {
      filter: drop-shadow(0 0 3px rgba(52, 211, 153, 0.75));
    }
    .c.c3 {
      filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.5));
    }

    /* Velocity progress meter styling */
    .u {
      height: 6px !important;
      rx: 2px;
      ry: 2px;
    }
    .u.u0 { fill: #064E3B !important; }
    .u.u1 { fill: #059669 !important; }
    .u.u2 { fill: #10B981 !important; }
    .u.u3 { fill: #34D399 !important; filter: drop-shadow(0 0 3px rgba(52, 211, 153, 0.8)); }
    """

    # Extract all elements inside the original <svg> after </style>
    body_content = content[style_m.end():]
    body_content = re.sub(r"</svg>\s*$", "", body_content)

    # Separate .u rects (score meter) from cells and snake segments
    # In snk:
    # <rect class="u u0" height="12" width="707.3" x="0.0" y="144"/>
    # We want .u rects inside a dedicated track at y=196
    # Let's adjust y="144" in .u rects to y="196"
    def rep_u_y(match):
        r = match.group(0)
        r = re.sub(r'y="144(?:\.0)?"', 'y="196"', r)
        r = re.sub(r'height="12(?:\.0)?"', 'height="6"', r)
        return r

    body_content = re.sub(r'<rect class="u[^"]*"[^>]+/>', rep_u_y, body_content)

    # Construct the complete 2026 container SVG
    new_svg = f"""<svg viewBox="0 0 1000 280" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <desc>Enhanced 2026 Contribution Trajectory for Richard D'Souza (aestheticwolf)</desc>
  <defs>
    <!-- Dark Container Gradients -->
    <linearGradient id="frameBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#101522" stop-opacity="0.98" />
      <stop offset="50%" stop-color="#0B0E17" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#08090D" stop-opacity="0.98" />
    </linearGradient>

    <!-- Animated Chromatic Border -->
    <linearGradient id="frameBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.65">
        <animate attributeName="stop-color" values="#10B981;#22D3EE;#8B5CF6;#10B981" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#282E44" stop-opacity="0.75" />
      <stop offset="70%" stop-color="#1E2337" stop-opacity="0.55" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.65">
        <animate attributeName="stop-color" values="#8B5CF6;#10B981;#22D3EE;#8B5CF6" dur="10s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Scanning Header Line -->
    <linearGradient id="scanLineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0" />
      <stop offset="30%" stop-color="#10B981" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#8B5CF6" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#10B981" stop-opacity="0" />
    </linearGradient>

    <!-- Ambient Glows -->
    <radialGradient id="emeraldAura" cx="15%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#10B981" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="violetAura" cx="85%" cy="70%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.07" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0" />
    </radialGradient>

    <!-- Drop Shadow -->
    <filter id="frameShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.55" />
    </filter>
  </defs>

  <style><![CDATA[
{snk_css}
{extra_css}
  ]]></style>

  <!-- ============================================================== -->
  <!-- 01. CONTAINER CHASSIS & AMBIENT GLOWS                          -->
  <!-- ============================================================== -->
  <!-- Outer Backdrop -->
  <rect width="1000" height="280" rx="16" fill="#08090D" />

  <!-- Main Glassmorphic Card -->
  <g filter="url(#frameShadow)">
    <rect x="16" y="16" width="968" height="248" rx="14" fill="url(#frameBg)" stroke="url(#frameBorder)" stroke-width="1.2" />
    <!-- Ambient Radial Overlays -->
    <rect x="16" y="16" width="968" height="248" rx="14" fill="url(#emeraldAura)" />
    <rect x="16" y="16" width="968" height="248" rx="14" fill="url(#violetAura)" />
  </g>

  <!-- Floating Micro-Particles (Futuristic Atmosphere) -->
  <circle cx="50" cy="70" r="1.5" fill="#10B981" opacity="0.3">
    <animate attributeName="opacity" values="0.2;0.6;0.2" dur="4s" repeatCount="indefinite" />
  </circle>
  <circle cx="950" cy="110" r="1.5" fill="#8B5CF6" opacity="0.3">
    <animate attributeName="opacity" values="0.3;0.7;0.3" dur="5s" repeatCount="indefinite" />
  </circle>
  <circle cx="920" cy="210" r="1.2" fill="#22D3EE" opacity="0.4">
    <animate attributeName="opacity" values="0.2;0.8;0.2" dur="3.5s" repeatCount="indefinite" />
  </circle>

  <!-- ============================================================== -->
  <!-- 02. TOP HUD / TELEMETRY HEADER                                 -->
  <!-- ============================================================== -->
  <g transform="translate(36, 28)">
    <!-- Pulsing Live Indicator -->
    <circle cx="6" cy="6" r="4" fill="#34D399" />
    <circle cx="6" cy="6" r="7" fill="none" stroke="#34D399" stroke-width="1.2" opacity="0.6">
      <animate attributeName="r" values="4;9;4" dur="2.4s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2.4s" repeatCount="indefinite" />
    </circle>

    <!-- Header Titles -->
    <text x="22" y="10" class="mono" font-size="11" font-weight="700" fill="#22D3EE">CONTRIBUTION TRAJECTORY</text>
    <text x="200" y="10" class="sans" font-size="11" fill="#4B5563">•</text>
    <text x="214" y="10" class="mono" font-size="10.5" font-weight="600" fill="#A1A1AA">52-WEEK VELOCITY ENGINE</text>

    <!-- Right Header Telemetry Badge -->
    <g transform="translate(928, 0)">
      <rect x="-190" y="-3" width="190" height="22" rx="11" fill="#141A29" stroke="#252F47" stroke-width="0.9" />
      <circle cx="-178" cy="8" r="3" fill="#8B5CF6" />
      <text x="-168" y="12" class="mono" font-size="9" font-weight="700" fill="#DDD6FE">PLATANE/SNK // ACTIVE</text>
    </g>

    <!-- Divider Line with Animated Laser Scan -->
    <rect x="-4" y="22" width="936" height="1" fill="url(#scanLineGrad)" />
    <rect x="-4" y="22" width="140" height="1" fill="#22D3EE" opacity="0.9">
      <animate attributeName="x" values="-4;796;-4" dur="9s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.3;1;0.3" dur="9s" repeatCount="indefinite" />
    </rect>
  </g>

  <!-- ============================================================== -->
  <!-- 03. AUTHENTIC CONTRIBUTION GRID & SNAKE ENGINE                 -->
  <!-- Centered at x=76, y=66                                         -->
  <!-- ============================================================== -->
  <g transform="translate(76, 66)">
    <!-- Velocity Progress Meter Background Track -->
    <rect x="0" y="196" width="848" height="6" rx="3" fill="#131926" stroke="#1E273A" stroke-width="0.8" />
{body_content}
  </g>

  <!-- ============================================================== -->
  <!-- 04. BOTTOM HUD: VELOCITY METRICS & 5-TIER LEGEND               -->
  <!-- ============================================================== -->
  <g transform="translate(76, 246)">
    <!-- Left: Progression Status -->
    <g transform="translate(0, 0)">
      <circle cx="4" cy="-3.5" r="3" fill="#10B981" />
      <text x="14" y="0" class="mono" font-size="9.5" font-weight="600" fill="#64748B">HARVEST VELOCITY // 52-WEEK REPOSITORY CADENCE</text>
    </g>

    <!-- Right: 5-Tier Contribution Intensity Legend -->
    <g transform="translate(680, 0)">
      <text x="0" y="0" class="sans" font-size="10" font-weight="500" fill="#8B949E">Less</text>

      <!-- Tier 1: No Contributions -->
      <rect x="32" y="-9" width="11" height="11" rx="2.5" fill="#161D29" stroke="#252E42" stroke-width="0.8" />

      <!-- Tier 2: Low Activity -->
      <rect x="48" y="-9" width="11" height="11" rx="2.5" fill="#064E3B" stroke="#0F664F" stroke-width="0.8" />

      <!-- Tier 3: Moderate Activity -->
      <rect x="64" y="-9" width="11" height="11" rx="2.5" fill="#059669" stroke="#12A87A" stroke-width="0.8" />

      <!-- Tier 4: High Activity -->
      <rect x="80" y="-9" width="11" height="11" rx="2.5" fill="#10B981" stroke="#25D99F" stroke-width="0.8" />

      <!-- Tier 5: Maximum Peak Activity -->
      <rect x="96" y="-9" width="11" height="11" rx="2.5" fill="#34D399" stroke="#5EEAD4" stroke-width="0.8" style="filter: drop-shadow(0 0 3px rgba(52, 211, 153, 0.8));" />

      <text x="114" y="0" class="sans" font-size="10" font-weight="500" fill="#8B949E">More</text>
    </g>
  </g>
</svg>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_svg)

    print(f"Successfully enhanced {input_path} -> {output_path} ({len(new_svg)} bytes)")
    return True

def main():
    # If called with --dist, process files in dist/
    if "--dist" in sys.argv:
        dist_dark = "dist/github-contribution-grid-snake-dark.svg"
        if os.path.exists(dist_dark):
            enhance_snake_file(dist_dark, dist_dark)
            # Also copy to assets/ for README direct reference
            import shutil
            assets_target = "assets/github-contribution-grid-snake-dark.svg"
            os.makedirs("assets", exist_ok=True)
            shutil.copy2(dist_dark, assets_target)
            print(f"Copied {dist_dark} to {assets_target}")
    else:
        # Local development / default run
        src = r"C:\Users\richa\.gemini\antigravity\brain\c55eedce-f2fe-4537-a7bd-91c8d58d1d9e\scratch\live_snake_dark.svg"
        dst = r"a:\0\a\repo\assets\github-contribution-grid-snake-dark.svg"
        enhance_snake_file(src, dst)

if __name__ == "__main__":
    main()
