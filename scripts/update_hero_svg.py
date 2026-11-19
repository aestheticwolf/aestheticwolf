import xml.etree.ElementTree as ET

def update_hero():
    with open('assets/hero.svg', 'r', encoding='utf-8') as f:
        content = f.read()

    # Target the badge group
    old_badge_group = '''    <!-- EXACT 3 SMALL INTEGRATED INFORMATION ELEMENTS -->
    <g transform="translate(0, 222)">
      <!-- Indicator 1: Full-Stack Developer -->
      <g transform="translate(0, 0)">
        <rect width="176" height="32" rx="7" fill="#101424" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1" />
        <circle cx="16" cy="16" r="3.5" fill="#8B5CF6" />
        <text x="28" y="20" class="f-mono" font-size="10" font-weight="700" fill="#C4B5FD">Full-Stack Developer</text>
      </g>

      <!-- Indicator 2: M.Sc. Information Technology -->
      <g transform="translate(188, 0)">
        <rect width="210" height="32" rx="7" fill="#101424" stroke="rgba(59, 130, 246, 0.3)" stroke-width="1" />
        <circle cx="16" cy="16" r="3.5" fill="#3B82F6" />
        <text x="28" y="20" class="f-mono" font-size="10" font-weight="700" fill="#93C5FD">M.Sc. Information Tech</text>
      </g>

      <!-- Indicator 3: React • Node • AI -->
      <g transform="translate(410, 0)">
        <rect width="168" height="32" rx="7" fill="#101424" stroke="rgba(34, 211, 238, 0.3)" stroke-width="1" />
        <circle cx="16" cy="16" r="3.5" fill="#22D3EE" />
        <text x="28" y="20" class="f-mono" font-size="10" font-weight="700" fill="#67E8F9">React • Node • AI</text>
      </g>
    </g>'''

    assert old_badge_group in content, "old_badge_group not found in hero.svg"
    content = content.replace(old_badge_group, '')

    # Adjust vertical translation and spacing of the left group
    content = content.replace('<g transform="translate(48, 98)">', '<g transform="translate(48, 108)">')
    content = content.replace(
        '<text x="0" y="178" class="f-sans" font-size="15.5" fill="#A1A1AA" letter-spacing="0.2">\n      Architecting high-performance web applications, mobile platforms and intelligent software solutions.\n    </text>',
        '<text x="0" y="192" class="f-sans" font-size="16" fill="#CBD5E1" letter-spacing="0.25">\n      Architecting <tspan fill="#F5F5F7" font-weight="600">high-performance</tspan> web applications, mobile platforms and intelligent software solutions.\n    </text>'
    )

    # Validate XML
    ET.fromstring(content)

    with open('assets/hero.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("hero.svg successfully updated: 3 badges removed, spacing optimized!")

if __name__ == '__main__':
    update_hero()
