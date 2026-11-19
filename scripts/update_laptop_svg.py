import re

with open("assets/laptop.svg", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update root tag: remove height="100%"
text = re.sub(
    r'<svg\s+xmlns="http://www.w3.org/2000/svg"\s+viewBox="0 0 1100 720"\s+width="100%"\s+height="100%">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 720" width="100%">',
    text
)

# 2. Update background fills from #06070B to #080B14
text = text.replace('#06070B', '#080B14')
text = text.replace('stop-color="#06070B"', 'stop-color="#080B14"')

# 3. Enhance deskUnderglow with deep navy, cyan, and electric-blue highlights + breathing animation
old_desk = """    <radialGradient id="deskUnderglow" cx="50%" cy="85%" r="65%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.35" />
      <stop offset="35%" stop-color="#3B82F6" stop-opacity="0.20" />
      <stop offset="70%" stop-color="#22D3EE" stop-opacity="0.06" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""

new_desk = """    <radialGradient id="deskUnderglow" cx="50%" cy="85%" r="65%">
      <animate attributeName="r" values="65%;72%;65%" dur="14s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.38" />
      <stop offset="35%" stop-color="#3B82F6" stop-opacity="0.24" />
      <stop offset="65%" stop-color="#8B5CF6" stop-opacity="0.10" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""
text = text.replace(old_desk, new_desk)

# 4. Enhance studioGridFloor pattern with cyan stroke
text = text.replace('stroke="#3B82F6" stroke-width="0.5" stroke-opacity="0.04"', 'stroke="#22D3EE" stroke-width="0.5" stroke-opacity="0.07"')

# 5. Enhance screenAmbientGlow with cyan and electric-blue
old_screen_glow = """    <radialGradient id="screenAmbientGlow" cx="50%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.16" />
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""

new_screen_glow = """    <radialGradient id="screenAmbientGlow" cx="50%" cy="40%" r="55%">
      <animate attributeName="cx" values="50%;48%;50%" dur="15s" repeatCount="indefinite" />
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.22" />
      <stop offset="45%" stop-color="#3B82F6" stop-opacity="0.12" />
      <stop offset="80%" stop-color="#8B5CF6" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#080B14" stop-opacity="0" />
    </radialGradient>"""
text = text.replace(old_screen_glow, new_screen_glow)

# 6. Ensure high contrast text #F5F5F7
text = text.replace('fill="#FFFFFF"', 'fill="#F5F5F7"')
text = text.replace('fill="#E2E8F0"', 'fill="#F5F5F7"')

with open("assets/laptop.svg", "w", encoding="utf-8") as f:
    f.write(text)

print("laptop.svg updated successfully!")
