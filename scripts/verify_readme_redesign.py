import os
import re
import subprocess
from collections import Counter

def verify_readme():
    print("==================================================")
    print("VALIDATING README.md ASSETS, TAGS, AND STRUCTURE")
    print("==================================================")

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check local asset links
    asset_matches = re.findall(r'src=["\'](\./assets/[^"\']+)["\']', content)
    asset_matches += re.findall(r'srcset=["\'](\./assets/[^"\']+)["\']', content)

    print(f"Found {len(asset_matches)} asset references in README.md:")
    missing = []
    for link in sorted(set(asset_matches)):
        # Normalize path
        rel_path = link.replace('./', '')
        exists = os.path.exists(rel_path)
        print(f"  [{'PASS' if exists else 'FAIL'}] {link} -> {rel_path} ({os.path.getsize(rel_path) if exists else 0} bytes)")
        if not exists:
            missing.append(link)

    assert len(missing) == 0, f"Missing assets found: {missing}"

    # 2. Check HTML paired tags
    open_tags = re.findall(r'<([a-zA-Z0-9]+)(?: [^>]*)?>', content)
    close_tags = re.findall(r'</([a-zA-Z0-9]+)>', content)
    self_closing = {'img', 'source', 'br', 'hr', 'input', 'meta', 'link'}
    paired_open = [t.lower() for t in open_tags if t.lower() not in self_closing]
    paired_close = [t.lower() for t in close_tags]

    open_counts = Counter(paired_open)
    close_counts = Counter(paired_close)
    
    print("\nPaired HTML tag count verification:")
    for tag in sorted(open_counts.keys()):
        o_count = open_counts[tag]
        c_count = close_counts.get(tag, 0)
        status = 'PASS' if o_count == c_count else 'MISMATCH'
        print(f"  [{status}] <{tag}>: {o_count} opened, {c_count} closed")
        assert o_count == c_count, f"Tag mismatch for <{tag}>: {o_count} open vs {c_count} closed"

    # 3. Check for forbidden buzzwords
    buzzwords = [
        'cutting-edge', 'next-generation', 'scalable digital realities',
        'turning ideas into reality', 'building the future',
        'extraordinary', 'high-performance web applications',
        'all systems operational', 'passion & precision'
    ]
    print("\nBuzzwords & marketing filler audit:")
    found_buzzwords = []
    content_lower = content.lower()
    for b in buzzwords:
        if b in content_lower:
            found_buzzwords.append(b)
            print(f"  [WARN] Found buzzword: '{b}'")
        else:
            print(f"  [PASS] Clean: '{b}' not found")
    
    assert len(found_buzzwords) == 0, f"Found buzzwords: {found_buzzwords}"

    print("\n==================================================")
    print("ALL VALIDATION CHECKS PASSED: 100% CLEAN AND SOUND!")
    print("==================================================")

if __name__ == '__main__':
    verify_readme()
