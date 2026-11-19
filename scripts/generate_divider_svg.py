"""
Generate elegant, high-tech animated gradient divider SVGs matching the 2026 dark design system:
Primary background: #080B14
Card background: #121827
Navy: #101B32
Violet: #8B5CF6
Electric blue: #3B82F6
Cyan: #22D3EE
Emerald: #10B981
"""
import xml.etree.ElementTree as ET

def generate_divider():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 24" width="100%" height="24" fill="none">
  <defs>
    <linearGradient id="divGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0"/>
      <stop offset="20%" stop-color="#8B5CF6" stop-opacity="0.2"/>
      <stop offset="40%" stop-color="#3B82F6" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="1"/>
      <stop offset="60%" stop-color="#3B82F6" stop-opacity="0.7"/>
      <stop offset="80%" stop-color="#8B5CF6" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="divCore" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0"/>
      <stop offset="25%" stop-color="#8B5CF6" stop-opacity="0.3"/>
      <stop offset="45%" stop-color="#3B82F6" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#F5F5F7" stop-opacity="1"/>
      <stop offset="55%" stop-color="#22D3EE" stop-opacity="0.85"/>
      <stop offset="75%" stop-color="#8B5CF6" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </linearGradient>
    <filter id="divBlur" x="-10%" y="-100%" width="120%" height="300%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
    </filter>
  </defs>
  <!-- Ambient wide glow beam -->
  <line x1="80" y1="12" x2="920" y2="12" stroke="url(#divGlow)" stroke-width="4" filter="url(#divBlur)" opacity="0.6">
    <animate attributeName="opacity" values="0.4;0.75;0.4" dur="4s" repeatCount="indefinite"/>
  </line>
  <!-- Core sharp laser trace -->
  <line x1="80" y1="12" x2="920" y2="12" stroke="url(#divCore)" stroke-width="1.2" opacity="0.9"/>
  <!-- Micro focal center notch -->
  <circle cx="500" cy="12" r="2.5" fill="#22D3EE" filter="url(#divBlur)" opacity="0.8">
    <animate attributeName="r" values="2;3.2;2" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="500" cy="12" r="1.2" fill="#FFFFFF"/>
</svg>'''
    
    # Validate XML
    ET.fromstring(svg_content)
    
    with open('assets/divider.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content.strip() + '\n')
    print("Successfully generated assets/divider.svg")

if __name__ == '__main__':
    generate_divider()
