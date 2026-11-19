import re

with open("assets/hero.svg", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update root tag: remove height="100%"
text = re.sub(
    r'<svg\s+xmlns="http://www.w3.org/2000/svg"\s+viewBox="0 0 1000 420"\s+width="100%"\s+height="100%">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 420" width="100%">',
    text
)

# 2. Update background fills from #06070B to #080B14
text = text.replace('#06070B', '#080B14')
text = text.replace('stop-color="#06070B"', 'stop-color="#080B14"')

# 3. Add slow animated breathing to heroVoidGlow and heroCyanFocal
void_glow_pattern = r'(<radialGradient id="heroVoidGlow" cx="20%" cy="30%" r="65%">)'
void_glow_replacement = """<radialGradient id="heroVoidGlow" cx="20%" cy="30%" r="65%">
      <animate attributeName="cx" values="20%;25%;20%" dur="16s" repeatCount="indefinite" />
      <animate attributeName="cy" values="30%;26%;30%" dur="16s" repeatCount="indefinite" />"""
text = re.sub(void_glow_pattern, void_glow_replacement, text)

cyan_focal_pattern = r'(<radialGradient id="heroCyanFocal" cx="76%" cy="50%" r="55%">)'
cyan_focal_replacement = """<radialGradient id="heroCyanFocal" cx="76%" cy="50%" r="55%">
      <animate attributeName="cx" values="76%;72%;76%" dur="18s" repeatCount="indefinite" />
      <animate attributeName="cy" values="50%;54%;50%" dur="18s" repeatCount="indefinite" />"""
text = re.sub(cyan_focal_pattern, cyan_focal_replacement, text)

# 4. Enhance glass card layers with deep navy and card background
text = text.replace('stop-color="#1E2338"', 'stop-color="#121827"')
text = text.replace('stop-color="#0D101C"', 'stop-color="#0D1321"')
text = text.replace('stop-color="#161B2E"', 'stop-color="#101B32"')

# 5. Ensure text colors match #F5F5F7 and #A1A1AA
text = text.replace('fill="#FFFFFF"', 'fill="#F5F5F7"')
text = text.replace('fill="#E2E8F0"', 'fill="#F5F5F7"')
text = text.replace('fill="#94A3B8"', 'fill="#A1A1AA"')
text = text.replace('fill="#64748B"', 'fill="#8B949E"')

with open("assets/hero.svg", "w", encoding="utf-8") as f:
    f.write(text)

print("hero.svg updated successfully!")
