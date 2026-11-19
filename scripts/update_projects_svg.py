import re

files = ["project-01-skillpath.svg", "project-02-sentinel.svg", "project-03-artbyheaven.svg"]

for fname in files:
    path = f"assets/{fname}"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Remove height="100%"
    text = re.sub(
        r'<svg\s+xmlns="http://www.w3.org/2000/svg"\s+viewBox="0 0 560 360"\s+width="100%"\s+height="100%">',
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 360" width="100%">',
        text
    )

    # 2. Update background gradient stops to Black and Navy #080B14 - #101B32
    text = re.sub(r'stop-color="#(?:070810|060910|080612)"', 'stop-color="#080B14"', text)
    text = re.sub(r'stop-color="#(?:111424|111624|141126)"', 'stop-color="#101B32"', text)
    text = re.sub(r'stop-color="#(?:0E101E|0E121E|0F0D1E)"', 'stop-color="#0D1321"', text)

    # 3. High contrast text typography
    text = text.replace('fill="#FFFFFF"', 'fill="#F5F5F7"')
    text = text.replace('fill="#F8FAFC"', 'fill="#F5F5F7"')
    text = text.replace('fill="#E2E8F0"', 'fill="#F5F5F7"')
    text = text.replace('fill="#CBD5E1"', 'fill="#A1A1AA"')
    text = text.replace('fill="#94A3B8"', 'fill="#A1A1AA"')
    text = text.replace('fill="#64748B"', 'fill="#8B949E"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"{fname} updated successfully!")
