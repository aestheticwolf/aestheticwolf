import xml.etree.ElementTree as ET

def update_p3():
    with open('assets/project-03-artbyheaven.svg', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace gradient definitions and colors for Art by Heaven to Amber (#FB923C) & Coral/Pink (#F472B6)
    content = content.replace(
        '<stop offset="0%" stop-color="#A78BFA" />\n      <stop offset="50%" stop-color="#EC4899" />\n      <stop offset="100%" stop-color="#22D3EE" />',
        '<stop offset="0%" stop-color="#FB923C" />\n      <stop offset="50%" stop-color="#F472B6" />\n      <stop offset="100%" stop-color="#F97316" />'
    )
    content = content.replace(
        '<stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.22" />\n      <stop offset="60%" stop-color="#EC4899" stop-opacity="0.08" />',
        '<stop offset="0%" stop-color="#FB923C" stop-opacity="0.24" />\n      <stop offset="60%" stop-color="#F472B6" stop-opacity="0.10" />'
    )
    content = content.replace('stroke="#2B2044"', 'stroke="rgba(251, 146, 60, 0.3)"')
    content = content.replace('stroke="#2D2248"', 'stroke="#38251C"')
    content = content.replace('fill="#16122C"', 'fill="#1A131F"')
    content = content.replace('fill="#DDD6FE"', 'fill="#FED7AA"')
    content = content.replace('fill="#20153D" stroke="#8B5CF6"', 'fill="#2E1C14" stroke="#FB923C"')
    content = content.replace('fill="#C4B5FD"', 'fill="#FED7AA"')
    content = content.replace('stroke="rgba(167, 139, 250, 0.4)"', 'stroke="rgba(251, 146, 60, 0.45)"')
    content = content.replace('fill="#0E0C1C"', 'fill="#140F16"')
    content = content.replace('fill="#1D1734"', 'fill="#261A18"')
    content = content.replace('fill="#A78BFA"', 'fill="#FB923C"')
    content = content.replace('stroke="#EC4899"', 'stroke="#F472B6"')
    content = content.replace('fill="#F472B6"', 'fill="#F472B6"')
    content = content.replace('fill="#8B5CF6"', 'fill="#FB923C"')
    content = content.replace('stroke="#4C1D95"', 'stroke="#9A3412"')
    content = content.replace('fill="#1C1438"', 'fill="#261814"')
    content = content.replace('fill="#171230"', 'fill="#241716"')
    content = content.replace('fill="#1F1338"', 'fill="#2E1A16"')
    content = content.replace('fill="#2C204A"', 'fill="#3D241C"')
    content = content.replace('stroke="#2C204A"', 'stroke="#45271A"')
    content = content.replace('stroke="#EC4899"', 'stroke="#FB923C"')
    content = content.replace('fill="#EC4899"', 'fill="#F472B6"')
    content = content.replace('fill="#1A1532"', 'fill="#291A18"')

    # Validate XML
    ET.fromstring(content)

    with open('assets/project-03-artbyheaven.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("assets/project-03-artbyheaven.svg successfully upgraded to Amber (#FB923C) and Coral/Pink (#F472B6)!")

if __name__ == '__main__':
    update_p3()
