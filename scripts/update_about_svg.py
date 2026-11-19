import re

with open("assets/about.svg", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update root tag: remove height="100%"
text = re.sub(
    r'<svg\s+xmlns="http://www.w3.org/2000/svg"\s+viewBox="0 0 1000 640"\s+width="100%"\s+height="100%">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" width="100%">',
    text
)

# 2. Update background fills from #08090D to #080B14
text = text.replace('#08090D', '#080B14')
text = text.replace('stop-color="#08090D"', 'stop-color="#080B14"')

# 3. Update Glows to Violet and Teal / Emerald with animated pulsing
old_glows = """    <radialGradient id="aboutVoidGlow1" cx="15%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.14" />
      <stop offset="60%" stop-color="#8B5CF6" stop-opacity="0.03" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="aboutVoidGlow2" cx="50%" cy="65%" r="45%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.12" />
      <stop offset="55%" stop-color="#3B82F6" stop-opacity="0.02" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="aboutVoidGlow3" cx="85%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.14" />
      <stop offset="60%" stop-color="#22D3EE" stop-opacity="0.03" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""

new_glows = """    <radialGradient id="aboutVoidGlow1" cx="15%" cy="20%" r="50%">
      <animate attributeName="cx" values="15%;20%;15%" dur="16s" repeatCount="indefinite" />
      <animate attributeName="cy" values="20%;16%;20%" dur="16s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.18" />
      <stop offset="60%" stop-color="#8B5CF6" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="aboutVoidGlow2" cx="50%" cy="65%" r="45%">
      <stop offset="0%" stop-color="#101B32" stop-opacity="0.25" />
      <stop offset="55%" stop-color="#0D1321" stop-opacity="0.10" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="aboutVoidGlow3" cx="85%" cy="30%" r="50%">
      <animate attributeName="cx" values="85%;80%;85%" dur="18s" repeatCount="indefinite" />
      <animate attributeName="cy" values="30%;35%;30%" dur="18s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.16" />
      <stop offset="60%" stop-color="#22D3EE" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""
text = text.replace(old_glows, new_glows)

# 4. Enhance card chassis to #121827 / #101B32
text = text.replace('fill="#101322"', 'fill="#121827"')
text = text.replace('fill="#0D101C"', 'fill="#0D1321"')
text = text.replace('fill="#141829"', 'fill="#151D30"')

# 5. Ensure high-contrast text typography
text = text.replace('fill="#FFFFFF"', 'fill="#F5F5F7"')
text = text.replace('fill="#F8FAFC"', 'fill="#F5F5F7"')
text = text.replace('fill="#E2E8F0"', 'fill="#F5F5F7"')
text = text.replace('fill="#CBD5E1"', 'fill="#A1A1AA"')
text = text.replace('fill="#94A3B8"', 'fill="#A1A1AA"')
text = text.replace('fill="#64748B"', 'fill="#8B949E"')

with open("assets/about.svg", "w", encoding="utf-8") as f:
    f.write(text)

print("about.svg updated successfully!")
