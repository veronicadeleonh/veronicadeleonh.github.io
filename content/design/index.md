---
title: "Design System"
layout: "page"
url: "/design/"
---

<style>
.ds-token { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-secondary); }
.ds-row { display: flex; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--color-surface); }
.ds-space-block { background: var(--color-surface); height: 24px; }
.ds-table { width: 100%; border-collapse: collapse; margin-top: 16px; }
.ds-table th { text-align: left; font-size: var(--font-size-sm); font-weight: var(--font-weight-medium); color: var(--color-text-tertiary); padding: 0 16px 8px 0; border-bottom: 1px solid var(--color-surface); }
.ds-table td { padding: 10px 16px 10px 0; border-bottom: 1px solid var(--color-surface); vertical-align: middle; }
.ds-table td:first-child { width: 32px; }
.ds-color-swatch { width: 24px; height: 24px; border: 1px solid var(--color-border); flex-shrink: 0; }
.ds-color-name { font-size: var(--font-size-base); font-weight: var(--font-weight-medium); }
.ds-color-var { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); }
.ds-color-hex { display: flex; align-items: center; gap: 6px; }
.ds-color-dot { width: 10px; height: 10px; flex-shrink: 0; border: 1px solid var(--color-border); }
.ds-hex-value { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-secondary); }
</style>

<p class="ds-token">assets/css/extended/custom.css</p>

---

## Colors

### Base

<table class="ds-table">
<thead><tr><th></th><th>Name</th><th>Token</th><th>Hex</th></tr></thead>
<tbody>
<tr><td><div class="ds-color-swatch" style="background:var(--color-bg)"></div></td><td><span class="ds-color-name">bg</span></td><td><span class="ds-color-var">--color-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-bg)"></div><span class="ds-hex-value">#fff</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-text)"></div></td><td><span class="ds-color-name">text</span></td><td><span class="ds-color-var">--color-text</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-text);border-color:var(--color-text)"></div><span class="ds-hex-value">#000</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-surface)"></div></td><td><span class="ds-color-name">surface</span></td><td><span class="ds-color-var">--color-surface</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-surface)"></div><span class="ds-hex-value">#f1f4f5</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-surface-hover)"></div></td><td><span class="ds-color-name">surface-hover</span></td><td><span class="ds-color-var">--color-surface-hover</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-surface-hover)"></div><span class="ds-hex-value">#e2e6e7</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-surface-active)"></div></td><td><span class="ds-color-name">surface-active</span></td><td><span class="ds-color-var">--color-surface-active</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-surface-active)"></div><span class="ds-hex-value">#d1d5d6</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-border)"></div></td><td><span class="ds-color-name">border</span></td><td><span class="ds-color-var">--color-border</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-border)"></div><span class="ds-hex-value">#e7eaeb</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-text-secondary)"></div></td><td><span class="ds-color-name">text-secondary</span></td><td><span class="ds-color-var">--color-text-secondary</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-text-secondary);border-color:var(--color-text-secondary)"></div><span class="ds-hex-value">#616768</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-text-tertiary)"></div></td><td><span class="ds-color-name">text-tertiary</span></td><td><span class="ds-color-var">--color-text-tertiary</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-text-tertiary);border-color:var(--color-text-tertiary)"></div><span class="ds-hex-value">#6d7475</span></div></td></tr>
</tbody>
</table>

### Semantic

<table class="ds-table">
<thead><tr><th></th><th>Name</th><th>Token</th><th>Hex</th></tr></thead>
<tbody>
<tr><td><div class="ds-color-swatch" style="background:var(--color-green)"></div></td><td><span class="ds-color-name">green</span></td><td><span class="ds-color-var">--color-green</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-green);border-color:var(--color-green)"></div><span class="ds-hex-value">#6ab04c</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-green-bg)"></div></td><td><span class="ds-color-name">green-bg</span></td><td><span class="ds-color-var">--color-green-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-green-bg)"></div><span class="ds-hex-value">#bbdc582d</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-orange)"></div></td><td><span class="ds-color-name">orange</span></td><td><span class="ds-color-var">--color-orange</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-orange);border-color:var(--color-orange)"></div><span class="ds-hex-value">#f0932b</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-orange-bg)"></div></td><td><span class="ds-color-name">orange-bg</span></td><td><span class="ds-color-var">--color-orange-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-orange-bg)"></div><span class="ds-hex-value">#ffbf762d</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-blue)"></div></td><td><span class="ds-color-name">blue</span></td><td><span class="ds-color-var">--color-blue</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-blue);border-color:var(--color-blue)"></div><span class="ds-hex-value">#4834d4</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-blue-bg)"></div></td><td><span class="ds-color-name">blue-bg</span></td><td><span class="ds-color-var">--color-blue-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-blue-bg)"></div><span class="ds-hex-value">#686ce02d</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-purple)"></div></td><td><span class="ds-color-name">purple</span></td><td><span class="ds-color-var">--color-purple</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-purple);border-color:var(--color-purple)"></div><span class="ds-hex-value">#964DF6</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-purple-bg)"></div></td><td><span class="ds-color-name">purple-bg</span></td><td><span class="ds-color-var">--color-purple-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-purple-bg)"></div><span class="ds-hex-value">#964df626</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-yellow)"></div></td><td><span class="ds-color-name">yellow</span></td><td><span class="ds-color-var">--color-yellow</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-yellow);border-color:var(--color-yellow)"></div><span class="ds-hex-value">#f9ca24</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-yellow-bg)"></div></td><td><span class="ds-color-name">yellow-bg</span></td><td><span class="ds-color-var">--color-yellow-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-yellow-bg)"></div><span class="ds-hex-value">#f6e58d40</span></div></td></tr>
</tbody>
</table>

### Bright accents

<p>For dark surfaces. Each one passes AA at 8:1 or more on the dark background. Used by the dark theme and by the accent light.</p>

<table class="ds-table">
<thead><tr><th></th><th>Name</th><th>Token</th><th>Hex</th></tr></thead>
<tbody>
<tr><td><div class="ds-color-swatch" style="background:var(--color-blue-bright)"></div></td><td><span class="ds-color-name">blue-bright</span></td><td><span class="ds-color-var">--color-blue-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-blue-bright);border-color:var(--color-blue-bright)"></div><span class="ds-hex-value">#6cb6ff</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-purple-bright)"></div></td><td><span class="ds-color-name">purple-bright</span></td><td><span class="ds-color-var">--color-purple-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-purple-bright);border-color:var(--color-purple-bright)"></div><span class="ds-hex-value">#c9a7ff</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-pink-bright)"></div></td><td><span class="ds-color-name">pink-bright</span></td><td><span class="ds-color-var">--color-pink-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-pink-bright);border-color:var(--color-pink-bright)"></div><span class="ds-hex-value">#ff7ad9</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-orange-bright)"></div></td><td><span class="ds-color-name">orange-bright</span></td><td><span class="ds-color-var">--color-orange-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-orange-bright);border-color:var(--color-orange-bright)"></div><span class="ds-hex-value">#ff9e57</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-yellow-bright)"></div></td><td><span class="ds-color-name">yellow-bright</span></td><td><span class="ds-color-var">--color-yellow-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-yellow-bright);border-color:var(--color-yellow-bright)"></div><span class="ds-hex-value">#ffd84d</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-green-bright)"></div></td><td><span class="ds-color-name">green-bright</span></td><td><span class="ds-color-var">--color-green-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-green-bright);border-color:var(--color-green-bright)"></div><span class="ds-hex-value">#4fe08c</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--color-grey-bright)"></div></td><td><span class="ds-color-name">grey-bright</span></td><td><span class="ds-color-var">--color-grey-bright</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:var(--color-grey-bright);border-color:var(--color-grey-bright)"></div><span class="ds-hex-value">#b0b7b8</span></div></td></tr>
</tbody>
</table>

### Dark theme

<p>Opt-in per page with <code>pageTheme: dark</code> in the front matter (sets <code>data-page-theme="dark"</code> on <code>&lt;html&gt;</code>). It redefines the base tokens below and maps the semantic accents to their bright versions (<code>--color-blue</code> → <code>--color-blue-bright</code>, and so on, plus <code>--color-pink</code> and <code>--color-grey</code>). Used by <a href="/how-i-build/">How I build</a>.</p>

<table class="ds-table">
<thead><tr><th></th><th>Name</th><th>Token</th><th>Hex</th></tr></thead>
<tbody>
<tr><td><div class="ds-color-swatch" style="background:#0e1011"></div></td><td><span class="ds-color-name">bg</span></td><td><span class="ds-color-var">--color-bg</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#0e1011;border-color:#0e1011"></div><span class="ds-hex-value">#0e1011</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#f1f4f5"></div></td><td><span class="ds-color-name">text</span></td><td><span class="ds-color-var">--color-text</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#f1f4f5;border-color:#f1f4f5"></div><span class="ds-hex-value">#f1f4f5</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#1a1d1f"></div></td><td><span class="ds-color-name">surface</span></td><td><span class="ds-color-var">--color-surface</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#1a1d1f;border-color:#1a1d1f"></div><span class="ds-hex-value">#1a1d1f</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#24282a"></div></td><td><span class="ds-color-name">surface-hover</span></td><td><span class="ds-color-var">--color-surface-hover</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#24282a;border-color:#24282a"></div><span class="ds-hex-value">#24282a</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#3a3f41"></div></td><td><span class="ds-color-name">surface-active</span></td><td><span class="ds-color-var">--color-surface-active</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#3a3f41;border-color:#3a3f41"></div><span class="ds-hex-value">#3a3f41</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#2a2e30"></div></td><td><span class="ds-color-name">border</span></td><td><span class="ds-color-var">--color-border</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#2a2e30;border-color:#2a2e30"></div><span class="ds-hex-value">#2a2e30</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#b4babb"></div></td><td><span class="ds-color-name">text-secondary</span></td><td><span class="ds-color-var">--color-text-secondary</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#b4babb;border-color:#b4babb"></div><span class="ds-hex-value">#b4babb</span></div></td></tr>
<tr><td><div class="ds-color-swatch" style="background:#8d9495"></div></td><td><span class="ds-color-name">text-tertiary</span></td><td><span class="ds-color-var">--color-text-tertiary</span></td><td><div class="ds-color-hex"><div class="ds-color-dot" style="background:#8d9495;border-color:#8d9495"></div><span class="ds-hex-value">#8d9495</span></div></td></tr>
</tbody>
</table>

### Accent light

<table class="ds-table">
<thead><tr><th></th><th>Name</th><th>Token</th><th>Value</th></tr></thead>
<tbody>
<tr><td><div class="ds-color-swatch" style="background:var(--accent-light)"></div></td><td><span class="ds-color-name">accent-light</span></td><td><span class="ds-color-var">--accent-light</span></td><td><span class="ds-hex-value">#ffffff</span></td></tr>
<tr><td><div class="ds-color-swatch" style="background:var(--accent-glow)"></div></td><td><span class="ds-color-name">accent-glow</span></td><td><span class="ds-color-var">--accent-glow</span></td><td><span class="ds-hex-value">var(--color-purple-bright)</span></td></tr>
</tbody>
</table>

<div style="position:relative;overflow:hidden;height:56px;margin:16px 0 8px;border:1px solid var(--color-border)"><div style="position:absolute;inset:-40%;background:var(--gradient-aurora),#ffffff;animation:aurora-move 6s ease-in-out infinite alternate"></div></div>
<p class="ds-token">--gradient-aurora · three soft radial lights (light · glow · light), animated with <code>aurora-move</code></p>

<p>The "Mono + violet" accent light has two uses, both as overlays, so the element never changes size:</p>
<ul>
<li><strong>Spotlight</strong> (hover and keyboard focus): a radial light from <code>--accent-light</code> to <code>--accent-glow</code> follows the cursor along a 1px border ring, with a faint glow inside. A small script writes the cursor position to <code>--x</code> and <code>--y</code>. Also the hover of the home "How I build these" entry, which stays dark.</li>
<li><strong>Aurora</strong> (active, selected elements): an oversized <code>::before</code> (<code>inset: -40%</code>) filled with <code>--gradient-aurora</code>, drifting with <code>aurora-move</code> (6s, ease-in-out, alternate).</li>
</ul>
<p>Both stop animating with <code>prefers-reduced-motion</code>.</p>

---

## Typography

### Fonts

<div class="ds-row">
<span class="ds-token" style="width:160px">--font-sans</span>
<span style="font-family: var(--font-sans); font-size: var(--font-size-md)">IBM Plex Sans — The quick brown fox</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-mono</span>
<span style="font-family: var(--font-mono); font-size: var(--font-size-md)">IBM Plex Mono — The quick brown fox</span>
</div>

### Scale

<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-hero</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">28px</span>
<span style="font-size: var(--font-size-hero)">Heading hero</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-lg</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">20px</span>
<span style="font-size: var(--font-size-lg)">Heading large</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-md</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">16px</span>
<span style="font-size: var(--font-size-md)">Body medium</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-base</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">15px</span>
<span style="font-size: var(--font-size-base)">Body base</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-tag</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">14px</span>
<span style="font-size: var(--font-size-tag)">Tag / label</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-sm</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">13px</span>
<span style="font-size: var(--font-size-sm)">Small / footnote</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--font-size-xs</span>
<span style="width:40px; font-size: var(--font-size-base); color: var(--color-text-secondary)">12px</span>
<span style="font-size: var(--font-size-xs)">Extra small / footer</span>
</div>

### Weights

<table class="ds-table">
<thead><tr><th>Token</th><th>Value</th><th>Preview</th><th>Usage</th></tr></thead>
<tbody>
<tr><td><span class="ds-token">--font-weight-light</span></td><td><span style="font-size: var(--font-size-base); color: var(--color-text-secondary)">300</span></td><td><span style="font-weight: var(--font-weight-light); font-size: var(--font-size-md)">The quick brown fox</span></td><td><span class="ds-token">body text, nav</span></td></tr>
<tr><td><span class="ds-token">--font-weight-regular</span></td><td><span style="font-size: var(--font-size-base); color: var(--color-text-secondary)">400</span></td><td><span style="font-weight: var(--font-weight-regular); font-size: var(--font-size-md)">The quick brown fox</span></td><td><span class="ds-token">mono elements</span></td></tr>
<tr><td><span class="ds-token">--font-weight-medium</span></td><td><span style="font-size: var(--font-size-base); color: var(--color-text-secondary)">500</span></td><td><span style="font-weight: var(--font-weight-medium); font-size: var(--font-size-md)">The quick brown fox</span></td><td><span class="ds-token">headings, links</span></td></tr>
<tr><td><span class="ds-token">--font-weight-bold</span></td><td><span style="font-size: var(--font-size-base); color: var(--color-text-secondary)">700</span></td><td><span style="font-weight: var(--font-weight-bold); font-size: var(--font-size-md)">The quick brown fox</span></td><td><span class="ds-token">numbered labels</span></td></tr>
</tbody>
</table>

---

## Spacing

<div style="margin-top: 16px; display: flex; flex-direction: column; gap: 12px;">

<div style="display: flex; align-items: center; gap: 16px;">
<span class="ds-token" style="width:160px">--space-1 · 4px</span>
<div class="ds-space-block" style="width: var(--space-1)"></div>
</div>

<div style="display: flex; align-items: center; gap: 16px;">
<span class="ds-token" style="width:160px">--space-2 · 8px</span>
<div class="ds-space-block" style="width: var(--space-2)"></div>
</div>

<div style="display: flex; align-items: center; gap: 16px;">
<span class="ds-token" style="width:160px">--space-3 · 16px</span>
<div class="ds-space-block" style="width: var(--space-3)"></div>
</div>

<div style="display: flex; align-items: center; gap: 16px;">
<span class="ds-token" style="width:160px">--space-4 · 24px</span>
<div class="ds-space-block" style="width: var(--space-4)"></div>
</div>

<div style="display: flex; align-items: center; gap: 16px;">
<span class="ds-token" style="width:160px">--space-5 · 32px</span>
<div class="ds-space-block" style="width: var(--space-5)"></div>
</div>

</div>

---

## Transitions

<div class="ds-row">
<span class="ds-token" style="width:160px">--transition-fast · 150ms</span>
<div style="width: 32px; height: 32px; background: var(--color-surface); transition: background var(--transition-fast); cursor: pointer;" onmouseover="this.style.background='var(--color-text)'" onmouseout="this.style.background='var(--color-surface)'"></div>
<span class="ds-token">hover me</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--transition-base · 300ms</span>
<div style="width: 32px; height: 32px; background: var(--color-surface); transition: background var(--transition-base); cursor: pointer;" onmouseover="this.style.background='var(--color-text)'" onmouseout="this.style.background='var(--color-surface)'"></div>
<span class="ds-token">hover me</span>
</div>
<div class="ds-row">
<span class="ds-token" style="width:160px">--transition-slow · 0.6s</span>
<div style="width: 32px; height: 32px; background: var(--color-surface); transition: background var(--transition-slow); cursor: pointer;" onmouseover="this.style.background='var(--color-text)'" onmouseout="this.style.background='var(--color-surface)'"></div>
<span class="ds-token">hover me</span>
</div>

---

## Components

### Tags

<div class="flex-wrap" style="margin-top: 16px">
<span class="tag green text-green">Green</span>
<span class="tag orange text-orange">Orange</span>
<span class="tag blue text-blue">Blue</span>
</div>

### Label

<div style="margin-top: 16px">
<span class="label-grey">Label grey</span>
</div>

### Dots

<div class="dot-container" style="margin-top: 16px">
<div class="dot yellow-dot"></div>
<span class="ds-token">yellow-dot</span>
</div>
<div class="dot-container" style="margin-top: 8px">
<div class="dot gray-dot"></div>
<span class="ds-token">gray-dot</span>
</div>

### Numbering

<div class="numbering" style="margin-top: 16px">
<div class="numbers">1</div>
<span class="numbers-label">Numbered list item example</span>
</div>
<div class="numbering">
<div class="numbers">2</div>
<span class="numbers-label">Another numbered item</span>
</div>

### Box notes

<div class="box-notes yellow-background yellow-border" style="margin-top: 16px">
This is a box note — used for callouts or highlighted information.
</div>

### Icons

<style>
.ds-icon-row { display: flex; align-items: center; gap: 16px; padding: 10px 0; border-bottom: 1px solid var(--color-surface); }
.ds-icon-wrap { width: 32px; display: flex; align-items: center; justify-content: center; }
.ds-icon-label { font-size: var(--font-size-base); }
</style>

#### UI — `class="fi"`

<div style="margin-top: 16px">
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/mouse.svg)"></span></div><span class="ds-token">mouse.svg</span><span class="ds-icon-label">Role / position</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/calendar.svg)"></span></div><span class="ds-token">calendar.svg</span><span class="ds-icon-label">Date / period</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/location.svg)"></span></div><span class="ds-token">location.svg</span><span class="ds-icon-label">Location</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/globe.svg)"></span></div><span class="ds-token">globe.svg</span><span class="ds-icon-label">Remote / worldwide</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/ext-link.svg)"></span></div><span class="ds-token">ext-link.svg</span><span class="ds-icon-label">External link</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/arrow-right.svg)"></span></div><span class="ds-token">arrow-right.svg</span><span class="ds-icon-label">Navigation / CTA</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fi" style="background-image: url(/images/arrow-bottom.svg)"></span></div><span class="ds-token">arrow-bottom.svg</span><span class="ds-icon-label">Scroll / download</span></div>
</div>

#### Social — `class="fip"`

<div style="margin-top: 16px">
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fip" style="background-image: url(/images/linkedin.svg)"></span></div><span class="ds-token">linkedin.svg</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fip" style="background-image: url(/images/github.svg)"></span></div><span class="ds-token">github.svg</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fip" style="background-image: url(/images/instagram.svg)"></span></div><span class="ds-token">instagram.svg</span></div>
<div class="ds-icon-row"><div class="ds-icon-wrap"><span class="fip" style="background-image: url(/images/readcv.svg)"></span></div><span class="ds-token">readcv.svg</span></div>
</div>
