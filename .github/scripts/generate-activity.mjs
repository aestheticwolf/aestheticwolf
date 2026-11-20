// .github/scripts/generate-activity.mjs
// Renders assets/latest-activity.svg from your public GitHub events.
// Zero dependencies. Needs Node 18+ (built-in fetch).
//
// Env (all optional):
//   GITHUB_USERNAME  default: aestheticwolf
//   GITHUB_TOKEN     raises API rate limit (provided automatically in Actions)
//   OUTPUT           default: assets/latest-activity.svg
//   INCLUDE_PUSHES   set to 'true' to also show commit pushes (default: hidden)
//   EVENTS_FILE      path to a JSON file of events (offline testing)
//   NOW              ISO date to treat as "now" (offline testing)

import fs from 'node:fs';
import path from 'node:path';

const USER = process.env.GITHUB_USERNAME || 'aestheticwolf';
const TOKEN = process.env.GITHUB_TOKEN || '';
const OUT = process.env.OUTPUT || 'assets/latest-activity.svg';
const NOW = process.env.NOW ? new Date(process.env.NOW) : new Date();
const INCLUDE_PUSHES = process.env.INCLUDE_PUSHES === 'true'; // commits/pushes are hidden by default
const MAX_ROWS = 5;
const DAYS = 14;

async function loadEvents() {
  if (process.env.EVENTS_FILE) return JSON.parse(fs.readFileSync(process.env.EVENTS_FILE, 'utf8'));
  const res = await fetch(`https://api.github.com/users/${USER}/events/public?per_page=100`, {
    headers: {
      Accept: 'application/vnd.github+json',
      'User-Agent': 'readme-activity-generator',
      ...(TOKEN ? { Authorization: `Bearer ${TOKEN}` } : {}),
    },
  });
  if (!res.ok) throw new Error(`GitHub API responded ${res.status}`);
  return res.json();
}

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const trunc = (s, n) => (s.length > n ? s.slice(0, n - 1).trimEnd() + '…' : s);
const oneLine = (s) => String(s || '').split('\n')[0].trim();

function ago(d) {
  const s = Math.max(0, (NOW - d) / 1000);
  if (s < 3600) return `${Math.max(1, Math.round(s / 60))}m ago`;
  if (s < 86400) return `${Math.round(s / 3600)}h ago`;
  const days = Math.round(s / 86400);
  if (days < 30) return `${days}d ago`;
  return `${Math.round(days / 30)}mo ago`;
}

function describe(e) {
  const repo = (e.repo?.name || '').replace(`${USER}/`, '');
  const p = e.payload || {};
  const at = new Date(e.created_at);
  switch (e.type) {
    case 'PushEvent': {
      const n = p.size ?? p.commits?.length ?? 1;
      const msg = oneLine(p.commits?.[p.commits.length - 1]?.message);
      const branch = (p.ref || '').replace('refs/heads/', '') || 'main';
      return { kind: 'commit', repo, at, verb: `pushed ${n} commit${n > 1 ? 's' : ''}`, text: msg || `Pushed to ${branch}` };
    }
    case 'PullRequestEvent': {
      const pr = p.pull_request || {};
      return { kind: 'pr', repo, at, verb: `${pr.merged ? 'merged' : p.action || 'updated'} pull request`, text: oneLine(pr.title) || 'Pull request' };
    }
    case 'PullRequestReviewEvent':
      return { kind: 'pr', repo, at, verb: 'reviewed pull request', text: oneLine(p.pull_request?.title) || 'Pull request' };
    case 'IssuesEvent':
      return { kind: 'issue', repo, at, verb: `${p.action || 'updated'} issue`, text: oneLine(p.issue?.title) || 'Issue' };
    case 'IssueCommentEvent':
      return { kind: 'comment', repo, at, verb: 'commented on', text: oneLine(p.issue?.title) || 'Issue' };
    case 'CreateEvent':
      if (p.ref_type === 'repository') return { kind: 'new', repo, at, verb: 'created repository', text: oneLine(p.description) || repo };
      return { kind: 'new', repo, at, verb: `created ${p.ref_type || 'ref'}`, text: p.ref || repo };
    case 'WatchEvent':
      return { kind: 'star', repo, at, verb: 'starred', text: e.repo?.name || repo };
    case 'ForkEvent':
      return { kind: 'fork', repo, at, verb: 'forked', text: p.forkee?.full_name || repo };
    case 'ReleaseEvent':
      return { kind: 'release', repo, at, verb: 'published release', text: p.release?.name || p.release?.tag_name || 'Release' };
    default:
      return null;
  }
}

const STYLE = {
  commit: '#22d3ee', pr: '#a78bfa', issue: '#fbbf24', comment: '#f472b6',
  new: '#34d399', star: '#fbbf24', fork: '#22d3ee', release: '#34d399',
};

const ICONS = {
  commit: '<circle cx="8" cy="8" r="3"/><path d="M.5 8H5M11 8h4.5"/>',
  pr: '<circle cx="4" cy="3.5" r="1.8"/><circle cx="4" cy="12.5" r="1.8"/><circle cx="12" cy="12.5" r="1.8"/><path d="M4 5.3v5.4M12 10.7V6.5Q12 4.5 10 4.5H8"/>',
  issue: '<circle cx="8" cy="8" r="6"/><circle cx="8" cy="8" r=".8"/>',
  comment: '<path d="M2 3h12v7H8l-3 3v-3H2z"/>',
  new: '<path d="M8 2v12M2 8h12"/>',
  star: '<path d="M8 1.8l1.9 4.1 4.4.5-3.3 3 .9 4.4L8 11.6l-3.9 2.2.9-4.4-3.3-3 4.4-.5z"/>',
  fork: '<circle cx="4" cy="3" r="1.8"/><circle cx="12" cy="3" r="1.8"/><circle cx="8" cy="13" r="1.8"/><path d="M4 4.8V6q0 2 4 2t4-2V4.8M8 8v3.2"/>',
  release: '<path d="M2 8l6-6h6v6l-6 6z"/><circle cx="10.5" cy="5.5" r="1"/>',
};

function render(items, spark, stats) {
  const maxSpark = Math.max(1, ...spark);
  const rows = items.map((it, i) => {
    const y = 106 + i * 54;
    const c = STYLE[it.kind];
    return `
    <g class="up" style="animation-delay:${(0.25 + i * 0.12).toFixed(2)}s">
      <rect x="56" y="${y}" width="738" height="46" rx="12" fill="#fff" fill-opacity=".045" stroke="#fff" stroke-opacity=".09"/>
      <rect x="56" y="${y + 9}" width="4" height="28" rx="2" fill="${c}"/>
      <use href="#i-${it.kind}" x="76" y="${y + 15}" width="16" height="16" stroke="${c}" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="sans" x="108" y="${y + 20}" font-size="14.5" font-weight="700" fill="#f8fafc">${esc(trunc(it.text, 62))}</text>
      <text class="mono" x="108" y="${y + 37}" font-size="11.5"><tspan fill="${c}">${esc(it.verb)}</tspan><tspan fill="#64748b">  ·  </tspan><tspan fill="#cbd5e1">${esc(trunc(it.repo, 34))}</tspan></text>
      <text class="mono" x="778" y="${y + 28}" text-anchor="end" font-size="12" fill="#94a3b8">${esc(ago(it.at))}</text>
    </g>`;
  }).join('');

  const empty = items.length
    ? ''
    : `<text class="sans" x="425" y="240" text-anchor="middle" font-size="16" fill="#94a3b8">No public activity yet. Time to ship something.</text>`;

  const bars = spark.map((n, i) => {
    const h = Math.max(4, Math.round((n / maxSpark) * 96));
    const x = 858 + i * 20.5;
    const last = i === spark.length - 1;
    return `<rect class="bar" x="${x.toFixed(1)}" y="${344 - h}" width="13" height="${h}" rx="4" fill="${last ? 'url(#hot)' : 'url(#bar)'}" style="animation-delay:${(0.4 + i * 0.05).toFixed(2)}s"/>`;
  }).join('\n      ');

  const stamp = NOW.toISOString().slice(0, 10);
  const symbols = Object.entries(ICONS).map(([k, v]) => `<symbol id="i-${k}" viewBox="0 0 16 16">${v}</symbol>`).join('\n    ');

  return `<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1200 430" width="1200" height="430" role="img" aria-label="Latest GitHub activity for ${esc(USER)}">
  <defs>
    <linearGradient id="neon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#a78bfa"/></linearGradient>
    <linearGradient id="hot" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
    <linearGradient id="bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#6d28d9"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#243055" stroke-width="1" opacity=".5"/></pattern>
    <radialGradient id="fade" cx=".5" cy=".5" r=".65"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>
    <mask id="gm"><rect width="1200" height="430" fill="url(#fade)"/></mask>
    <filter id="blur60" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    ${symbols}
  </defs>
  <style>
    .mono{font-family:'JetBrains Mono','Fira Code',ui-monospace,'SFMono-Regular',Consolas,'Courier New',monospace}
    .sans{font-family:Inter,'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif}
    text{white-space:pre}
    .lbl{font-size:11px;letter-spacing:3px;font-weight:700}
    .up{animation:up .7s cubic-bezier(.2,.8,.2,1) both}
    .bar{transform-box:fill-box;transform-origin:bottom center;animation:grow .9s cubic-bezier(.2,.8,.2,1) both}
    .a1{animation:drift 15s ease-in-out infinite alternate}
    .a2{animation:drift 20s ease-in-out infinite alternate-reverse}
    .ring{transform-box:fill-box;transform-origin:center;animation:ring 2.2s ease-out infinite}
    .sweep{animation:sweep 10s linear infinite}
    .tw{animation:tw 3s ease-in-out infinite}
    @keyframes up{from{opacity:0;transform:translateX(-16px)}to{opacity:1;transform:translateX(0)}}
    @keyframes grow{from{transform:scaleY(.05);opacity:0}to{transform:scaleY(1);opacity:1}}
    @keyframes drift{from{transform:translate(0,0)}to{transform:translate(70px,36px)}}
    @keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(3);opacity:0}}
    @keyframes sweep{from{stroke-dashoffset:0}to{stroke-dashoffset:-1000}}
    @keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
    @media (prefers-reduced-motion:reduce){*{animation:none!important}}
  </style>

  <rect width="1200" height="430" fill="#070b18"/>
  <g filter="url(#blur60)">
    <circle class="a1" cx="240" cy="80" r="160" fill="#7c3aed" opacity=".4"/>
    <circle class="a2" cx="1010" cy="380" r="180" fill="#0891b2" opacity=".36"/>
  </g>
  <rect width="1200" height="430" fill="url(#grid)" mask="url(#gm)"/>
  <g stroke="#22d3ee" stroke-width="2" fill="none" opacity=".6" stroke-linecap="round">
    <path d="M14 38V14H38"/><path d="M1162 14H1186V38"/><path d="M14 392V416H38"/><path d="M1162 416H1186V392"/>
  </g>
  <g fill="#fbbf24"><circle class="tw" cx="800" cy="36" r="2.5"/><circle class="tw" cx="1180" cy="215" r="2.5" style="animation-delay:1.4s"/></g>

  <circle cx="46" cy="48" r="6" fill="#34d399" filter="url(#glow)"/>
  <circle class="ring" cx="46" cy="48" r="6" fill="none" stroke="#34d399" stroke-width="2"/>
  <text class="mono lbl" x="64" y="52" fill="#22d3ee">// LATEST ACTIVITY</text>
  <text class="mono" x="1160" y="52" text-anchor="end" font-size="12.5" fill="#94a3b8">github.com/<tspan fill="#c4b5fd" font-weight="700">${esc(USER)}</tspan></text>

  <!-- feed panel -->
  <rect x="40" y="84" width="770" height="300" rx="20" fill="#0f1530" fill-opacity=".93" stroke="#2a3566" stroke-width="1.5"/>
  ${rows}${empty}
  <rect x="40" y="84" width="770" height="300" rx="20" fill="none" stroke="url(#neon)" stroke-width="2" pathLength="1000" stroke-dasharray="80 920" class="sweep"/>

  <!-- pulse panel -->
  <rect x="830" y="84" width="330" height="300" rx="20" fill="#0f1530" fill-opacity=".93" stroke="#2a3566" stroke-width="1.5"/>
  <text class="mono lbl" x="854" y="116" fill="#a78bfa">// PULSE · ${DAYS} DAYS</text>
  <text class="sans" x="854" y="170" font-size="52" font-weight="800" fill="url(#neon)">${stats.events}</text>
  <text class="sans" x="${854 + String(stats.events).length * 30 + 10}" y="170" font-size="16" fill="#cbd5e1">events</text>
  <text class="mono" x="854" y="194" font-size="12.5" fill="#94a3b8">across <tspan fill="#f8fafc" font-weight="700">${stats.repos}</tspan> repositor${stats.repos === 1 ? 'y' : 'ies'}</text>
  <g>
      ${bars}
  </g>
  <line x1="850" y1="346" x2="1140" y2="346" stroke="#2a3566"/>
  <text class="mono" x="854" y="366" font-size="10.5" fill="#64748b">${DAYS}d ago</text>
  <text class="mono" x="1136" y="366" text-anchor="end" font-size="10.5" fill="#f9a8d4">today</text>
  <rect x="830" y="84" width="330" height="300" rx="20" fill="none" stroke="url(#hot)" stroke-width="2" pathLength="1000" stroke-dasharray="80 920" class="sweep" style="animation-delay:-5s"/>

  <text class="mono" x="40" y="414" font-size="11" fill="#64748b">auto-updated daily via GitHub Actions  ·  generated ${stamp}</text>
</svg>
`;
}

async function main() {
  const raw = (await loadEvents()).filter((e) => INCLUDE_PUSHES || e.type !== 'PushEvent');
  const all = raw.map(describe).filter(Boolean);

  // one push row per repo, so a busy day doesn't flood the feed
  const seen = new Set();
  const items = [];
  for (const it of all) {
    if (it.kind === 'commit') {
      if (seen.has(it.repo)) continue;
      seen.add(it.repo);
    }
    items.push(it);
    if (items.length >= MAX_ROWS) break;
  }

  const spark = new Array(DAYS).fill(0);
  const repos = new Set();
  let events = 0;
  for (const e of raw) {
    const age = Math.floor((NOW - new Date(e.created_at)) / 86400000);
    if (age >= 0 && age < DAYS) {
      spark[DAYS - 1 - age] += 1;
      events += 1;
      if (e.repo?.name) repos.add(e.repo.name);
    }
  }

  const svg = render(items, spark, { events, repos: repos.size });
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, svg);
  console.log(`Wrote ${OUT} (${items.length} rows, ${events} events in ${DAYS}d)`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1); // keep the previous SVG if anything fails
});
