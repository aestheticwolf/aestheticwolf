import re

with open("assets/technology-logos.svg", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update root tag: remove height="100%"
text = re.sub(
    r'<svg\s+xmlns="http://www.w3.org/2000/svg"\s+viewBox="0 0 1000 500"\s+width="100%"\s+height="100%">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="100%">',
    text
)

# 2. Update background fills from #08090D to dark charcoal #0C101A
text = text.replace('#08090D', '#0C101A')
text = text.replace('stop-color="#08090D"', 'stop-color="#0C101A"')

# 3. Add slow breathing animation to techVoidGlow1 and techVoidGlow3
glow1_old = '<radialGradient id="techVoidGlow1" cx="15%" cy="25%" r="55%">'
glow1_new = """<radialGradient id="techVoidGlow1" cx="15%" cy="25%" r="55%">
      <animate attributeName="cx" values="15%;20%;15%" dur="18s" repeatCount="indefinite" />
      <animate attributeName="cy" values="25%;20%;25%" dur="18s" repeatCount="indefinite" />"""
text = text.replace(glow1_old, glow1_new)

glow3_old = '<radialGradient id="techVoidGlow3" cx="85%" cy="35%" r="55%">'
glow3_new = """<radialGradient id="techVoidGlow3" cx="85%" cy="35%" r="55%">
      <animate attributeName="cx" values="85%;80%;85%" dur="16s" repeatCount="indefinite" />
      <animate attributeName="cy" values="35%;40%;35%" dur="16s" repeatCount="indefinite" />"""
text = text.replace(glow3_old, glow3_new)

# 4. Enhance category badge backgrounds to #121827 / #101B32
text = text.replace('fill="#101322"', 'fill="#121827"')
text = text.replace('fill="#0D101C"', 'fill="#0D1321"')

# 5. Ensure high-contrast text typography
text = text.replace('fill="#FFFFFF"', 'fill="#F5F5F7"')
text = text.replace('fill="#E2E8F0"', 'fill="#F5F5F7"')
text = text.replace('fill="#CBD5E1"', 'fill="#A1A1AA"')
text = text.replace('fill="#94A3B8"', 'fill="#A1A1AA"')

with open("assets/technology-logos.svg", "w", encoding="utf-8") as f:
    f.write(text)

print("technology-logos.svg updated successfully!")
