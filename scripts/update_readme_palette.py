import re

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Hero section badges
    old_hero_badges = '''<p align="center">
  <a href="https://komarev.com/ghpvc/?username=aestheticwolf">
    <img src="https://komarev.com/ghpvc/?username=aestheticwolf&label=PROFILE+VIEWS&color=8B5CF6&style=for-the-badge&logo=eye&logoColor=white" alt="Profile Views" />
  </a>
  &nbsp;
  <a href="https://github.com/aestheticwolf" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-aestheticwolf-111522?style=for-the-badge&logo=github&logoColor=22D3EE" alt="GitHub" />
  </a>
  &nbsp;
  <a href="https://linkedin.com/in/richarddsouza29" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-richarddsouza29-111522?style=for-the-badge&logo=linkedin&logoColor=60A5FA" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="https://richard-portfolio-website-ten.vercel.app" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Portfolio-richard--portfolio-111522?style=for-the-badge&logo=vercel&logoColor=10B981" alt="Live Portfolio" />
  </a>
</p>'''

    new_hero_badges = '''<p align="center">
  <a href="https://komarev.com/ghpvc/?username=aestheticwolf">
    <img src="https://komarev.com/ghpvc/?username=aestheticwolf&label=PROFILE+VIEWS&color=8B5CF6&style=for-the-badge&logo=eye&logoColor=white" alt="Profile Views" />
  </a>
  &nbsp;
  <a href="https://github.com/aestheticwolf" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-aestheticwolf-101B32?style=for-the-badge&logo=github&logoColor=22D3EE" alt="GitHub" />
  </a>
  &nbsp;
  <a href="https://linkedin.com/in/richarddsouza29" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-richarddsouza29-101B32?style=for-the-badge&logo=linkedin&logoColor=3B82F6" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="https://richard-portfolio-website-ten.vercel.app" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Portfolio-richard--portfolio-101B32?style=for-the-badge&logo=vercel&logoColor=10B981" alt="Live Portfolio" />
  </a>
</p>'''
    assert old_hero_badges in content, "Hero badges not found"
    content = content.replace(old_hero_badges, new_hero_badges)

    # 2. Upgrade Section Headers with refined mono tags
    # Section 02
    old_s2 = '''<div align="left">
  <small><code>WORKSPACE &bull; RUNTIME ENVIRONMENT &bull; DEV TELEMETRY</code></small>
  <h2>DEVELOPER WORKSPACE</h2>
  <p><em>"A high-performance engineering environment tailored for speed, precision, and modern full-stack workflows."</em></p>
</div>'''
    new_s2 = '''<div align="left">
  <small><code>02 // RUNTIME &bull; DEV WORKSPACE &amp; HARDWARE</code></small>
  <h2>DEVELOPER WORKSPACE</h2>
  <p><em>"A high-performance engineering environment tailored for speed, precision, and modern full-stack workflows."</em></p>
</div>'''
    assert old_s2 in content, "Section 02 header not found"
    content = content.replace(old_s2, new_s2)

    # Section 03
    old_s3 = '''<div align="left">
  <small><code>IDENTITY &bull; ACADEMIC FOUNDATION &bull; CAREER TIMELINE</code></small>
  <h2>ABOUT &amp; PROFESSIONAL BACKGROUND</h2>
  <p><em>"Merging academic computer science rigor with production full-stack engineering."</em></p>
</div>'''
    new_s3 = '''<div align="left">
  <small><code>03 // IDENTITY &bull; ACADEMIC RIGOR &amp; PRODUCTION ENGINEERING</code></small>
  <h2>ABOUT &amp; PROFESSIONAL BACKGROUND</h2>
  <p><em>"Merging academic computer science rigor with production full-stack engineering."</em></p>
</div>'''
    assert old_s3 in content, "Section 03 header not found"
    content = content.replace(old_s3, new_s3)

    # Section 04
    old_s4 = '''<div align="left">
  <small><code>STACK ARCHITECTURE &bull; 5 TIERS &bull; 19 PRODUCTION TECHNOLOGIES</code></small>
  <h2>TECHNOLOGY ECOSYSTEM</h2>
  <p><em>"Official production technology stack across core languages, frontend, backend, databases, and tooling."</em></p>
</div>'''
    new_s4 = '''<div align="left">
  <small><code>04 // ARCHITECTURE &bull; 5 TIERS &bull; 19 PRODUCTION TECHNOLOGIES</code></small>
  <h2>TECHNOLOGY ECOSYSTEM</h2>
  <p><em>"Official production technology stack across core languages, frontend, backend, databases, and tooling."</em></p>
</div>'''
    assert old_s4 in content, "Section 04 header not found"
    content = content.replace(old_s4, new_s4)

    # Section 05
    old_s5 = '''<div align="left">
  <small><code>SELECTED WORK / 2026 &bull; FEATURED PRODUCTION REPOSITORIES</code></small>
  <h2>SELECTED PROJECTS</h2>
  <p><em>"Engineering ideas into robust, user-centric, and scalable digital realities."</em></p>
</div>'''
    new_s5 = '''<div align="left">
  <small><code>05 // SHOWCASE &bull; FEATURED PRODUCTION REPOSITORIES</code></small>
  <h2>SELECTED PROJECTS</h2>
  <p><em>"Engineering ideas into robust, user-centric, and scalable digital realities."</em></p>
</div>'''
    assert old_s5 in content, "Section 05 header not found"
    content = content.replace(old_s5, new_s5)

    # Section 06
    old_s6 = '''<div align="left">
  <small><code>GITHUB ACTIVITY / ANALYTICS &bull; LIVE REPOSITORY TELEMETRY</code></small>
  <h2>GITHUB ANALYTICS</h2>
  <p><em>"An overview of my development activity, repositories, and contribution history."</em></p>
</div>'''
    new_s6 = '''<div align="left">
  <small><code>06 // TELEMETRY &bull; GITHUB ACTIVITY &amp; METRICS</code></small>
  <h2>GITHUB ANALYTICS</h2>
  <p><em>"An overview of my development activity, repositories, and contribution history."</em></p>
</div>'''
    assert old_s6 in content, "Section 06 header not found"
    content = content.replace(old_s6, new_s6)

    # Section 07
    old_s7 = '''<div align="left">
  <small><code>GITHUB ACTIVITY / CONTRIBUTION HISTORY &bull; 52-WEEK HEATMAP</code></small>
  <h2>CONTRIBUTION TRAJECTORY</h2>
  <p><em>"Every contribution represents another step in my development journey."</em></p>
</div>'''
    new_s7 = '''<div align="left">
  <small><code>07 // TRAJECTORY &bull; 52-WEEK COMMIT STREAM</code></small>
  <h2>CONTRIBUTION TRAJECTORY</h2>
  <p><em>"Every contribution represents another step in my development journey."</em></p>
</div>'''
    assert old_s7 in content, "Section 07 header not found"
    content = content.replace(old_s7, new_s7)

    # 3. Upgrade Project Badges in Section 05
    # Project 01
    old_p1_badges = '''      <p>
        <img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React Native" />
        <img src="https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white" alt="Expo" />
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase" />
      </p>'''
    new_p1_badges = '''      <p>
        <img src="https://img.shields.io/badge/React_Native-101B32?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React Native" />
        <img src="https://img.shields.io/badge/Expo-101B32?style=for-the-badge&logo=expo&logoColor=white" alt="Expo" />
        <img src="https://img.shields.io/badge/TypeScript-101B32?style=for-the-badge&logo=typescript&logoColor=3178C6" alt="TypeScript" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Firebase" />
      </p>'''
    assert old_p1_badges in content, "Project 01 badges not found"
    content = content.replace(old_p1_badges, new_p1_badges)

    # Project 01 button
    content = content.replace(
        'img.shields.io/badge/EXPLORE_REPOSITORY-111522?style=for-the-badge&logo=github&logoColor=22D3EE',
        'img.shields.io/badge/EXPLORE_REPOSITORY-101B32?style=for-the-badge&logo=github&logoColor=22D3EE'
    )

    # Project 02
    old_p2_badges = '''      <p>
        <img src="https://img.shields.io/badge/React.js-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React.js" />
        <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
        <img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white" alt="Express.js" />
        <img src="https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB Atlas" />
        <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT" />
        <img src="https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white" alt="Cloudinary" />
      </p>'''
    new_p2_badges = '''      <p>
        <img src="https://img.shields.io/badge/React.js-101B32?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React.js" />
        <img src="https://img.shields.io/badge/Node.js-101B32?style=for-the-badge&logo=node.js&logoColor=5FA04E" alt="Node.js" />
        <img src="https://img.shields.io/badge/Express.js-101B32?style=for-the-badge&logo=express&logoColor=white" alt="Express.js" />
        <img src="https://img.shields.io/badge/MongoDB_Atlas-101B32?style=for-the-badge&logo=mongodb&logoColor=47A248" alt="MongoDB Atlas" />
        <img src="https://img.shields.io/badge/JWT-101B32?style=for-the-badge&logo=jsonwebtokens&logoColor=FB015B" alt="JWT" />
        <img src="https://img.shields.io/badge/Cloudinary-101B32?style=for-the-badge&logo=cloudinary&logoColor=3448C5" alt="Cloudinary" />
      </p>'''
    assert old_p2_badges in content, "Project 02 badges not found"
    content = content.replace(old_p2_badges, new_p2_badges)

    # Project 03
    old_p3_badges = '''      <p>
        <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flutter" />
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase" />
        <img src="https://img.shields.io/badge/Cloud_Firestore-FFA611?style=for-the-badge&logo=firebase&logoColor=black" alt="Cloud Firestore" />
        <img src="https://img.shields.io/badge/Cloud_Functions-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Cloud Functions" />
        <img src="https://img.shields.io/badge/Razorpay-0C2340?style=for-the-badge&logo=razorpay&logoColor=3395FF" alt="Razorpay" />
      </p>'''
    new_p3_badges = '''      <p>
        <img src="https://img.shields.io/badge/Flutter-101B32?style=for-the-badge&logo=flutter&logoColor=02569B" alt="Flutter" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Firebase" />
        <img src="https://img.shields.io/badge/Cloud_Firestore-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Cloud Firestore" />
        <img src="https://img.shields.io/badge/Cloud_Functions-101B32?style=for-the-badge&logo=googlecloud&logoColor=4285F4" alt="Cloud Functions" />
        <img src="https://img.shields.io/badge/Razorpay-101B32?style=for-the-badge&logo=razorpay&logoColor=3395FF" alt="Razorpay" />
      </p>'''
    assert old_p3_badges in content, "Project 03 badges not found"
    content = content.replace(old_p3_badges, new_p3_badges)

    # 4. Upgrade github-readme-stats URLs in Section 06
    old_stats = 'bg_color=111522&title_color=A78BFA&text_color=F5F5F7&icon_color=22D3EE&border_color=282E44&border_radius=14&rank_icon=github'
    new_stats = 'bg_color=0D1321&title_color=8B5CF6&text_color=F5F5F7&icon_color=22D3EE&border_color=1E293B&border_radius=14&rank_icon=github'
    assert old_stats in content, "GitHub stats URL not found"
    content = content.replace(old_stats, new_stats)

    old_top_langs = 'bg_color=111522&title_color=22D3EE&text_color=F5F5F7&border_color=282E44&border_radius=14'
    new_top_langs = 'bg_color=0D1321&title_color=22D3EE&text_color=F5F5F7&border_color=1E293B&border_radius=14'
    assert old_top_langs in content, "Top langs URL not found"
    content = content.replace(old_top_langs, new_top_langs)

    # 5. Insert gradient dividers between sections
    # Divider markup
    divider = '\n<div align="center">\n  <img src="./assets/divider.svg" width="100%" height="24" alt="" />\n</div>\n\n'

    # Divider 1: between 01 Hero and 02 Workspace
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 02. DEVELOPER WORKSPACE',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 02. DEVELOPER WORKSPACE'
    )

    # Divider 2: between 02 Workspace and 03 About
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 03. ABOUT & PROFESSIONAL BACKGROUND',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 03. ABOUT & PROFESSIONAL BACKGROUND'
    )

    # Divider 3: between 03 About and 04 Technology Ecosystem
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 04. TECHNOLOGY ECOSYSTEM',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 04. TECHNOLOGY ECOSYSTEM'
    )

    # Divider 4: between 04 Technology and 05 Projects
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 05. SELECTED PROJECTS SHOWCASE',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 05. SELECTED PROJECTS SHOWCASE'
    )

    # Divider 5: between 05 Projects and 06 Analytics
    content = content.replace(
        '</table>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 06. GITHUB ANALYTICS DASHBOARD',
        '</table>\n\n' + divider + '<!-- ========================================== -->\n<!-- 06. GITHUB ANALYTICS DASHBOARD'
    )

    # Divider 6: between 06 Analytics and 07 Contribution Trajectory
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 07. CONTRIBUTION TRAJECTORY',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 07. CONTRIBUTION TRAJECTORY'
    )

    # Divider 7: between 07 Contribution and 08 Contact
    content = content.replace(
        '</div>\n\n<br/>\n\n<!-- ========================================== -->\n<!-- 08. CONTACT & SIGNATURE FOOTER',
        '</div>\n\n' + divider + '<!-- ========================================== -->\n<!-- 08. CONTACT & SIGNATURE FOOTER'
    )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("README.md updated successfully with dividers, badges, headers, and stats parameters!")

if __name__ == '__main__':
    update_readme()
