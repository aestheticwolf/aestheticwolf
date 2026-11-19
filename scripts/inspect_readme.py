import re

with open('README.md', 'r', encoding='utf-8') as f:
    txt = f.read()

print('Matches for vscode:', re.findall(r'vscode[^\s"\'<>]*', txt))
print('Matches for file://:', re.findall(r'file://[^\s"\'<>]*', txt))
print('Matches for localhost:', re.findall(r'localhost[^\s"\'<>]*', txt))
print('Total tables:', len(re.findall(r'<table\b', txt)), 'closing tables:', len(re.findall(r'</table>', txt)))
print('Total tr:', len(re.findall(r'<tr\b', txt)), 'closing tr:', len(re.findall(r'</tr>', txt)))
print('Total td:', len(re.findall(r'<td\b', txt)), 'closing td:', len(re.findall(r'</td>', txt)))
