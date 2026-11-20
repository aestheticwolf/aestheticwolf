import os
import markdown
import subprocess

with open('README.md', 'r', encoding='utf-8') as f:
    md_text = f.read()

# Convert markdown to html with table and fenced code extensions
html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

# Fix local asset links to file:/// URLs
repo_dir = os.path.abspath('.').replace('\\', '/')
html_body = html_body.replace('src="./assets/', f'src="file:///{repo_dir}/assets/')
html_body = html_body.replace('srcset="./assets/', f'srcset="file:///{repo_dir}/assets/')

full_html = f'''<!DOCTYPE html>
<html lang="en" style="background-color: #080B14; color: #F5F5F7;">
<head>
<meta charset="utf-8">
<title>Live README.md Preview</title>
<style>
  body {{
    background-color: #080B14;
    color: #F5F5F7;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 14px;
    line-height: 1.5;
    margin: 0;
    padding: 24px 0;
    display: flex;
    justify-content: center;
  }}
  .markdown-body {{
    max-width: 980px;
    width: 100%;
    box-sizing: border-box;
    padding: 0 16px;
  }}
  table {{
    border-spacing: 0;
    border-collapse: collapse;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
  }}
  table td {{
    padding: 8px;
    border: none;
    vertical-align: middle;
  }}
  code {{
    background: rgba(110, 118, 129, 0.4);
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-size: 85%;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    color: #38BDF8;
  }}
  h3 {{
    margin-top: 12px;
    margin-bottom: 8px;
    font-weight: 700;
  }}
  a {{
    color: #38BDF8;
    text-decoration: none;
  }}
  img {{
    max-width: 100%;
    box-sizing: border-box;
  }}
</style>
</head>
<body>
<div class="markdown-body">
{html_body}
</div>
</body>
</html>'''

preview_file = os.path.abspath('scratch/live_readme_preview.html')
with open(preview_file, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Saved preview to:", preview_file)

# Render full page screenshot using Edge
edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
screenshot_file = os.path.abspath('scratch/live_readme_full.png')

cmd = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--window-size=1200,900',
    '--screenshot=' + screenshot_file,
    'file:///' + preview_file.replace('\\', '/')
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Screenshot return code:", res.returncode)
print("Screenshot exists:", os.path.exists(screenshot_file))
if os.path.exists(screenshot_file):
    print("Screenshot file size:", os.path.getsize(screenshot_file), "bytes")
