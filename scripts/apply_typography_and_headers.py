import re

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # SECTION 02: DEVELOPER WORKSPACE
    old_s2 = '''<div align="left">
  <small><code>02 // RUNTIME &bull; DEV WORKSPACE &amp; HARDWARE</code></small>
  <h2>DEVELOPER WORKSPACE</h2>
  <p><em>"A high-performance engineering environment tailored for speed, precision, and modern full-stack workflows."</em></p>
</div>'''
    new_s2 = '''<div align="left">
  <img
    src="./assets/section-02-workspace-header.svg"
    alt="Developer Workspace - A high-performance engineering environment tailored for speed, precision, and modern full-stack workflows."
    width="100%"
  />
</div>'''
    assert old_s2 in content, "Section 02 block not found"
    content = content.replace(old_s2, new_s2)

    # SECTION 03: ABOUT & PROFESSIONAL BACKGROUND
    old_s3 = '''<div align="left">
  <small><code>03 // IDENTITY &bull; ACADEMIC RIGOR &amp; PRODUCTION ENGINEERING</code></small>
  <h2>ABOUT &amp; PROFESSIONAL BACKGROUND</h2>
  <p><em>"Merging academic computer science rigor with production full-stack engineering."</em></p>
</div>'''
    new_s3 = '''<div align="left">
  <img
    src="./assets/section-03-about-header.svg"
    alt="About &amp; Professional Background - Merging academic computer science rigor with production full-stack engineering."
    width="100%"
  />
</div>'''
    assert old_s3 in content, "Section 03 block not found"
    content = content.replace(old_s3, new_s3)

    # SECTION 04: TECHNOLOGY ECOSYSTEM
    old_s4 = '''<div align="left">
  <small><code>04 // ARCHITECTURE &bull; 5 TIERS &bull; 19 PRODUCTION TECHNOLOGIES</code></small>
  <h2>TECHNOLOGY ECOSYSTEM</h2>
  <p><em>"Official production technology stack across core languages, frontend, backend, databases, and tooling."</em></p>
</div>'''
    new_s4 = '''<div align="left">
  <img
    src="./assets/section-04-tech-header.svg"
    alt="Technology Ecosystem - Official production technology stack across core languages, frontend, backend, databases, and tooling."
    width="100%"
  />
</div>'''
    assert old_s4 in content, "Section 04 block not found"
    content = content.replace(old_s4, new_s4)

    # SECTION 05: SELECTED PROJECTS
    old_s5 = '''<div align="left">
  <small><code>05 // SHOWCASE &bull; FEATURED PRODUCTION REPOSITORIES</code></small>
  <h2>SELECTED PROJECTS</h2>
  <p><em>"Engineering ideas into robust, user-centric, and scalable digital realities."</em></p>
</div>'''
    new_s5 = '''<div align="left">
  <img
    src="./assets/section-05-projects-header.svg"
    alt="Selected Projects - Engineering ideas into robust, user-centric, and scalable digital realities."
    width="100%"
  />
</div>'''
    assert old_s5 in content, "Section 05 block not found"
    content = content.replace(old_s5, new_s5)

    # SECTION 06: GITHUB ANALYTICS
    old_s6 = '''<div align="left">
  <small><code>06 // TELEMETRY &bull; GITHUB ACTIVITY &amp; METRICS</code></small>
  <h2>GITHUB ANALYTICS</h2>
  <p><em>"An overview of my development activity, repositories, and contribution history."</em></p>
</div>'''
    new_s6 = '''<div align="left">
  <img
    src="./assets/section-06-analytics-header.svg"
    alt="GitHub Analytics - An overview of my development activity, repositories, and contribution history."
    width="100%"
  />
</div>'''
    assert old_s6 in content, "Section 06 block not found"
    content = content.replace(old_s6, new_s6)

    # SECTION 07: CONTRIBUTION TRAJECTORY
    old_s7 = '''<div align="left">
  <small><code>07 // TRAJECTORY &bull; 52-WEEK COMMIT STREAM</code></small>
  <h2>CONTRIBUTION TRAJECTORY</h2>
  <p><em>"Every contribution represents another step in my development journey."</em></p>
</div>'''
    new_s7 = '''<div align="left">
  <img
    src="./assets/section-07-trajectory-header.svg"
    alt="Contribution Trajectory - Every contribution represents another step in my development journey."
    width="100%"
  />
</div>'''
    assert old_s7 in content, "Section 07 block not found"
    content = content.replace(old_s7, new_s7)

    # PROJECT 01 TABLE
    old_p1 = '''<!-- PROJECT 01: SKILLPATH (Visual Left, Content Right) -->
<table>
  <tr>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">
        <img src="./assets/project-01-skillpath.svg" width="100%" alt="SkillPath Companion App" />
      </a>
    </td>
    <td width="52%" valign="middle">
      <small><code>CROSS-PLATFORM MOBILE &bull; LEARNING SYSTEM</code></small>
      <h3>01 &bull; SkillPath</h3>
      <p>A cross-platform mobile companion engineered with <code>React Native</code> and <code>Expo</code> to manage structured learning goals, track active streaks, and synchronize user state via <code>Firebase</code>.</p>
      <p>
        <img src="https://img.shields.io/badge/React_Native-101B32?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React Native" />
        <img src="https://img.shields.io/badge/Expo-101B32?style=for-the-badge&logo=expo&logoColor=white" alt="Expo" />
        <img src="https://img.shields.io/badge/TypeScript-101B32?style=for-the-badge&logo=typescript&logoColor=3178C6" alt="TypeScript" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Firebase" />
      </p>
      <ul>
        <li><strong>Goal Progression:</strong> Modular milestone decomposition with dynamic daily streak tracking.</li>
        <li><strong>Cloud Synchronization:</strong> Instant cross-device state persistence powered by Cloud Firestore.</li>
        <li><strong>Habit Retention:</strong> Proactive push notification workflows sustaining daily learner engagement.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-101B32?style=for-the-badge&logo=github&logoColor=22D3EE" alt="Explore Repository" />
        </a>
      </p>
    </td>
  </tr>
</table>'''

    new_p1 = '''<!-- PROJECT 01: SKILLPATH (Visual Left, Content Right) -->
<table>
  <tr>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">
        <img src="./assets/project-01-skillpath.svg" width="100%" alt="SkillPath Companion App" />
      </a>
    </td>
    <td width="52%" valign="middle">
      <a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">
        <img src="https://img.shields.io/badge/01%20//%20MOBILE%20COMPANION-LEARNING%20SYSTEM-A78BFA?style=for-the-badge&labelColor=101B32" alt="SkillPath Category" />
      </a>
      <h3><a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">01 &bull; SkillPath</a></h3>
      <p>A cross-platform mobile companion engineered with <code>React Native</code> and <code>Expo</code> to manage structured learning goals, track active streaks, and synchronize user state via <code>Firebase</code>.</p>
      <p>
        <img src="https://img.shields.io/badge/React_Native-101B32?style=for-the-badge&logo=react&logoColor=60A5FA" alt="React Native" />
        <img src="https://img.shields.io/badge/Expo-101B32?style=for-the-badge&logo=expo&logoColor=A78BFA" alt="Expo" />
        <img src="https://img.shields.io/badge/TypeScript-101B32?style=for-the-badge&logo=typescript&logoColor=60A5FA" alt="TypeScript" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=A78BFA" alt="Firebase" />
      </p>
      <ul>
        <li><strong>Goal Progression:</strong> Modular milestone decomposition with dynamic daily streak tracking.</li>
        <li><strong>Cloud Synchronization:</strong> Instant cross-device state persistence powered by Cloud Firestore.</li>
        <li><strong>Habit Retention:</strong> Proactive push notification workflows sustaining daily learner engagement.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/SkillCompanionApp" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-A78BFA?style=for-the-badge&logo=github&logoColor=white&labelColor=101B32" alt="Explore Repository" />
        </a>
      </p>
    </td>
  </tr>
</table>'''
    assert old_p1 in content, "Project 01 block not found"
    content = content.replace(old_p1, new_p1)

    # PROJECT 02 TABLE
    old_p2 = '''<!-- PROJECT 02: SENTINEL GRID (Content Left, Visual Right) -->
<table>
  <tr>
    <td width="52%" valign="middle">
      <small><code>WORKFORCE OPERATIONS &bull; FULL-STACK SECURITY</code></small>
      <h3>02 &bull; Sentinel Grid</h3>
      <p>A workforce management platform engineered with <code>React.js</code>, <code>Node.js</code>, and <code>MongoDB</code> to streamline on-site security deployments via geofenced GPS verification and biometric check-ins.</p>
      <p>
        <img src="https://img.shields.io/badge/React.js-101B32?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React.js" />
        <img src="https://img.shields.io/badge/Node.js-101B32?style=for-the-badge&logo=node.js&logoColor=5FA04E" alt="Node.js" />
        <img src="https://img.shields.io/badge/Express.js-101B32?style=for-the-badge&logo=express&logoColor=white" alt="Express.js" />
        <img src="https://img.shields.io/badge/MongoDB_Atlas-101B32?style=for-the-badge&logo=mongodb&logoColor=47A248" alt="MongoDB Atlas" />
        <img src="https://img.shields.io/badge/JWT-101B32?style=for-the-badge&logo=jsonwebtokens&logoColor=FB015B" alt="JWT" />
        <img src="https://img.shields.io/badge/Cloudinary-101B32?style=for-the-badge&logo=cloudinary&logoColor=3448C5" alt="Cloudinary" />
      </p>
      <ul>
        <li><strong>GPS Geofenced Tracking:</strong> Real-time coordinates verification at designated security checkpoints.</li>
        <li><strong>Selfie Verification:</strong> Tamper-resistant on-site photo check-ins via Cloudinary image pipelines.</li>
        <li><strong>Admin Command Center:</strong> Multi-site roster scheduling with JWT-based role separation.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-101B32?style=for-the-badge&logo=github&logoColor=22D3EE" alt="Explore Repository" />
        </a>
      </p>
    </td>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">
        <img src="./assets/project-02-sentinel.svg" width="100%" alt="Sentinel Grid" />
      </a>
    </td>
  </tr>
</table>'''

    new_p2 = '''<!-- PROJECT 02: SENTINEL GRID (Content Left, Visual Right) -->
<table>
  <tr>
    <td width="52%" valign="middle">
      <a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">
        <img src="https://img.shields.io/badge/02%20//%20WORKFORCE%20OPERATIONS-FULL--STACK%20SECURITY-22D3EE?style=for-the-badge&labelColor=101B32" alt="Sentinel Grid Category" />
      </a>
      <h3><a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">02 &bull; Sentinel Grid</a></h3>
      <p>A workforce management platform engineered with <code>React.js</code>, <code>Node.js</code>, and <code>MongoDB</code> to streamline on-site security deployments via geofenced GPS verification and biometric check-ins.</p>
      <p>
        <img src="https://img.shields.io/badge/React.js-101B32?style=for-the-badge&logo=react&logoColor=22D3EE" alt="React.js" />
        <img src="https://img.shields.io/badge/Node.js-101B32?style=for-the-badge&logo=node.js&logoColor=3B82F6" alt="Node.js" />
        <img src="https://img.shields.io/badge/Express.js-101B32?style=for-the-badge&logo=express&logoColor=22D3EE" alt="Express.js" />
        <img src="https://img.shields.io/badge/MongoDB-101B32?style=for-the-badge&logo=mongodb&logoColor=3B82F6" alt="MongoDB" />
        <img src="https://img.shields.io/badge/JWT-101B32?style=for-the-badge&logo=jsonwebtokens&logoColor=22D3EE" alt="JWT" />
        <img src="https://img.shields.io/badge/Cloudinary-101B32?style=for-the-badge&logo=cloudinary&logoColor=3B82F6" alt="Cloudinary" />
      </p>
      <ul>
        <li><strong>GPS Geofenced Tracking:</strong> Real-time coordinates verification at designated security checkpoints.</li>
        <li><strong>Selfie Verification:</strong> Tamper-resistant on-site photo check-ins via Cloudinary image pipelines.</li>
        <li><strong>Admin Command Center:</strong> Multi-site roster scheduling with JWT-based role separation.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-22D3EE?style=for-the-badge&logo=github&logoColor=101B32&labelColor=101B32" alt="Explore Repository" />
        </a>
      </p>
    </td>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/security-guard-tracking-system" target="_blank">
        <img src="./assets/project-02-sentinel.svg" width="100%" alt="Sentinel Grid" />
      </a>
    </td>
  </tr>
</table>'''
    assert old_p2 in content, "Project 02 block not found"
    content = content.replace(old_p2, new_p2)

    # PROJECT 03 TABLE
    old_p3 = '''<!-- PROJECT 03: ART BY HEAVEN (Visual Left, Content Right) -->
<table>
  <tr>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/art-of" target="_blank">
        <img src="./assets/project-03-artbyheaven.svg" width="100%" alt="Art by Heaven Mobile Store" />
      </a>
    </td>
    <td width="52%" valign="middle">
      <small><code>MOBILE E-COMMERCE &bull; FINTECH INTEGRATION</code></small>
      <h3>03 &bull; Art by Heaven</h3>
      <p>A mobile e-commerce platform built with <code>Flutter</code> and <code>Cloud Firestore</code> delivering smooth art catalog exploration, cart management, and secure payments via <code>Razorpay</code>.</p>
      <p>
        <img src="https://img.shields.io/badge/Flutter-101B32?style=for-the-badge&logo=flutter&logoColor=02569B" alt="Flutter" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Firebase" />
        <img src="https://img.shields.io/badge/Cloud_Firestore-101B32?style=for-the-badge&logo=firebase&logoColor=FFA611" alt="Cloud Firestore" />
        <img src="https://img.shields.io/badge/Cloud_Functions-101B32?style=for-the-badge&logo=googlecloud&logoColor=4285F4" alt="Cloud Functions" />
        <img src="https://img.shields.io/badge/Razorpay-101B32?style=for-the-badge&logo=razorpay&logoColor=3395FF" alt="Razorpay" />
      </p>
      <ul>
        <li><strong>Real-time Catalog:</strong> Live inventory hydration and category discovery via Cloud Firestore.</li>
        <li><strong>Cart Management:</strong> In-app subtotal calculation, quantity controls, and client persistence.</li>
        <li><strong>Razorpay Integration:</strong> End-to-end encrypted checkout supporting UPI, cards, and webhooks.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/art-of" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-101B32?style=for-the-badge&logo=github&logoColor=22D3EE" alt="Explore Repository" />
        </a>
      </p>
    </td>
  </tr>
</table>'''

    new_p3 = '''<!-- PROJECT 03: ART BY HEAVEN (Visual Left, Content Right) -->
<table>
  <tr>
    <td width="48%" align="center" valign="middle">
      <a href="https://github.com/aestheticwolf/art-of" target="_blank">
        <img src="./assets/project-03-artbyheaven.svg" width="100%" alt="Art by Heaven Mobile Store" />
      </a>
    </td>
    <td width="52%" valign="middle">
      <a href="https://github.com/aestheticwolf/art-of" target="_blank">
        <img src="https://img.shields.io/badge/03%20//%20MOBILE%20COMMERCE-FINTECH%20INTEGRATION-FB923C?style=for-the-badge&labelColor=101B32" alt="Art by Heaven Category" />
      </a>
      <h3><a href="https://github.com/aestheticwolf/art-of" target="_blank">03 &bull; Art by Heaven</a></h3>
      <p>A mobile e-commerce platform built with <code>Flutter</code> and <code>Cloud Firestore</code> delivering smooth art catalog exploration, cart management, and secure payments via <code>Razorpay</code>.</p>
      <p>
        <img src="https://img.shields.io/badge/Flutter-101B32?style=for-the-badge&logo=flutter&logoColor=FB923C" alt="Flutter" />
        <img src="https://img.shields.io/badge/Firebase-101B32?style=for-the-badge&logo=firebase&logoColor=F472B6" alt="Firebase" />
        <img src="https://img.shields.io/badge/Cloud_Firestore-101B32?style=for-the-badge&logo=firebase&logoColor=FB923C" alt="Cloud Firestore" />
        <img src="https://img.shields.io/badge/Cloud_Functions-101B32?style=for-the-badge&logo=googlecloud&logoColor=F472B6" alt="Cloud Functions" />
        <img src="https://img.shields.io/badge/Razorpay-101B32?style=for-the-badge&logo=razorpay&logoColor=FB923C" alt="Razorpay" />
      </p>
      <ul>
        <li><strong>Real-time Catalog:</strong> Live inventory hydration and category discovery via Cloud Firestore.</li>
        <li><strong>Cart Management:</strong> In-app subtotal calculation, quantity controls, and client persistence.</li>
        <li><strong>Razorpay Integration:</strong> End-to-end encrypted checkout supporting UPI, cards, and webhooks.</li>
      </ul>
      <p>
        <a href="https://github.com/aestheticwolf/art-of" target="_blank">
          <img src="https://img.shields.io/badge/EXPLORE_REPOSITORY-FB923C?style=for-the-badge&logo=github&logoColor=101B32&labelColor=101B32" alt="Explore Repository" />
        </a>
      </p>
    </td>
  </tr>
</table>'''
    assert old_p3 in content, "Project 03 block not found"
    content = content.replace(old_p3, new_p3)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("README.md successfully updated with section headers and project-specific visual identities!")

if __name__ == '__main__':
    update_readme()
