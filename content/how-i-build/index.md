---
title: "How I build with AI, so far"
layout: "page"
url: "/how-i-build/"
pageTheme: "dark"
summary: "A work in progress: how I build data apps with Claude, told through Deep Lineages"
---

<style>
/* The method as a trunk on the left; other projects join it as branches. */
:root { --hib-band: rgba(255, 255, 255, .035); --lin-accent: var(--accent-glow); --lin-tracing: var(--color-blue-bright); --lin-volcano: var(--color-orange-bright); --lin-open: var(--color-text-tertiary); --lin-x: -56px; }
.hib-wide { width: min(1028px, calc(100vw - 32px)); position: relative; left: 50%; transform: translateX(-50%); padding: var(--space-5) var(--space-5); margin: var(--space-4) 0; background: var(--hib-band); box-sizing: border-box; }
@media (max-width: 760px) { .hib-wide { padding: var(--space-4) var(--space-3); } }
.hib-kicker { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); text-transform: uppercase; letter-spacing: .04em; margin: var(--space-5) 0 var(--space-1) !important; }

.lin { position: relative; padding-bottom: 30vh; }
.lin-lines { position: absolute; left: 0; top: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 1; }
.lin-trunk-bg { stroke: var(--color-border); stroke-width: 2; fill: none; }
.lin-trunk { stroke: url(#lin-aurora); stroke-width: 2; fill: none; }
/* Spotlight: copies of the drawn lines, lit only around the pointer */
.lin-spot path { fill: none; stroke: url(#lin-spot); stroke-width: 3; stroke-linecap: round; }
.lin-branch { fill: none; stroke-width: 2; stroke-linecap: round; }
.lin-branch.tracing { stroke: var(--lin-tracing); } .lin-branch.volcano { stroke: var(--lin-volcano); }
.lin-branch.open { stroke: var(--lin-open); stroke-dasharray: 2 6; transition: opacity .5s; }
.lin-endopen { fill: var(--color-bg); stroke: var(--lin-open); stroke-width: 1.5; transition: opacity .5s; }

.lin-sec { position: relative; padding-top: 26vh; }
.lin-sec:first-of-type { padding-top: var(--space-4); }
.lin-intro { margin-bottom: var(--space-4); }
.lin-node { position: absolute; z-index: 2; left: calc(var(--lin-x) - 7px); width: 14px; height: 14px; transform: rotate(45deg); background: var(--color-bg); border: 2px solid var(--color-text-tertiary); transition: background .4s, border-color .4s, box-shadow .4s; }
.lin-node { overflow: hidden; isolation: isolate; }
.lin-sec.is-on .lin-node { border-color: var(--accent-light); }
/* Aurora inside the active node, the same light as the site's active buttons */
.lin-sec.is-on .lin-node::before { content: ""; position: absolute; inset: -60%; z-index: -1; background: var(--gradient-aurora), var(--accent-glow); animation: aurora-move 6s ease-in-out infinite alternate; }
.lin-card { position: relative; z-index: 2; opacity: .35; transform: translateY(14px); transition: opacity .6s ease, transform .6s ease; }
.lin-sec.is-on .lin-card, .lin-sec.was-on .lin-card { opacity: 1; transform: none; }
.lin-num { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); margin: 0 0 var(--space-1) !important; }
.post-content .lin h2 { margin-top: 0; }
.lin-lead { font-size: var(--font-size-lg) !important; line-height: 1.45; }
.lin-note { font-family: var(--font-mono); font-size: var(--font-size-sm) !important; color: var(--color-text-tertiary); }

.lin-froms { position: relative; z-index: 2; display: flex; flex-direction: column; gap: 16px; margin: 0 0 90px; }
.lin-from { max-width: 260px; font-family: var(--font-mono); font-size: var(--font-size-xs); line-height: 1.45; color: var(--color-text-secondary); opacity: 0; transition: opacity .5s; }
.lin-from b { display: block; font-weight: var(--font-weight-medium); font-size: var(--font-size-sm); }
.lin-from.tracing b { color: var(--lin-tracing); } .lin-from.volcano b { color: var(--lin-volcano); }
.lin-from + .lin-from { margin-left: 200px; }
.lin-from.is-on { opacity: 1; }
/* focus: the section being read stays bright, the rest step back */
.lin-sec > .lin-card, .lin-sec > .lin-wide, .lin-sec > .lin-froms { transition: opacity .6s ease, transform .6s ease; }
.lin-sec.was-on:not(.is-current) > .lin-card, .lin-sec.was-on:not(.is-current) > .lin-wide, .lin-sec.was-on:not(.is-current) > .lin-froms { opacity: .45 !important; }
.lin-sec.was-on:not(.is-current) .lin-node { border-color: var(--color-text-tertiary); }

.lin-compare { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-3); margin: var(--space-4) 0 var(--space-3); }
.lin-cmp { position: relative; border: 1px solid var(--color-border); padding: var(--space-3); --x: 50%; --y: 50%; }
/* Spotlight on the cards, as on the How I build entry: a violet light around the border that follows the pointer */
.lin-cmp::before, .lin-cmp::after { content: ""; position: absolute; pointer-events: none; opacity: 0; transition: opacity var(--transition-base) ease; }
.lin-cmp::before { inset: -1px; padding: 1px; background: radial-gradient(160px circle at var(--x) var(--y), var(--accent-light), var(--accent-glow) 40%, transparent 70%); -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; }
.lin-cmp::after { inset: 0; z-index: -1; background: radial-gradient(240px circle at var(--x) var(--y), color-mix(in srgb, var(--accent-glow) 22%, transparent), transparent 70%); }
.lin-cmp:hover::before, .lin-cmp:hover::after { opacity: 1; }
.lin-cmp .who { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); text-transform: uppercase; letter-spacing: .04em; }
.lin-cmp .big { font-family: var(--font-mono); font-size: 34px; font-weight: var(--font-weight-medium); line-height: 1.1; margin: 8px 0 2px; }
.lin-cmp.tracing .big { color: var(--lin-tracing); } .lin-cmp.deep .big { color: var(--lin-accent); }
.lin-cmp p { font-size: var(--font-size-sm) !important; color: var(--color-text-secondary); margin: 0 !important; }
.lin-skills { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-3); margin-top: var(--space-2); }
.lin-skill { border-top: 1px solid var(--color-border); padding-top: var(--space-2); }
.lin-skill code { font-size: var(--font-size-sm); color: var(--lin-accent); background: none; padding: 0; }
.lin-skill p { font-size: var(--font-size-sm) !important; color: var(--color-text-secondary); margin: 6px 0 0 !important; }
.lin-task { margin: var(--space-4) 0 0 !important; }
.lin-task + .lin-compare { margin-top: var(--space-2); }
.lin-tool { display: block; text-decoration: none; color: inherit; box-shadow: none !important; }
.lin-tool .big { font-size: 22px; color: var(--lin-accent); }
a.lin-tool:hover .who { color: var(--accent-light); }
.lin-vs { margin: var(--space-4) 0 0; }
.lin-vs-grid { display: grid; grid-template-columns: 108px 150px 24px 150px minmax(0,1fr); column-gap: 10px; margin-top: var(--space-2); }
.lin-vs-head, .lin-vs-row { grid-column: 1 / -1; display: grid; grid-template-columns: subgrid; align-items: center; }
.lin-vs-head span:nth-child(2), .lin-vs-head span:nth-child(4) { text-align: center; }
.lin-vs-head { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); padding-bottom: 8px; border-bottom: 1px solid var(--color-border); }
.lin-vs-row { padding: 14px 0; border-bottom: 1px solid var(--color-border); }
.lin-vs-who { font-weight: var(--font-weight-medium); font-size: var(--font-size-sm); }
.lin-vs-row.tracing .lin-vs-who { color: var(--lin-tracing); } .lin-vs-row.deep .lin-vs-who { color: var(--lin-accent); }
.lin-order { grid-column: 2 / span 3; display: grid; grid-template-columns: subgrid; list-style: none; margin: 0 !important; padding: 0 !important; font-family: var(--font-mono); font-size: var(--font-size-xs); }
.lin-order::before { content: "→"; grid-column: 2; grid-row: 1; align-self: center; justify-self: center; color: var(--color-text-tertiary); }
.lin-order li { margin: 0 !important; border: 1px solid var(--color-border); padding: 6px 4px; color: var(--color-text-tertiary); text-align: center; font-size: 12px; white-space: nowrap; }
.lin-order li:first-child { grid-column: 1; } .lin-order li:last-child { grid-column: 3; }
.lin-vs-row.tracing .lin-order li.on { color: var(--lin-tracing); border-color: var(--lin-tracing); } .lin-vs-row.deep .lin-order li.on { color: var(--lin-accent); border-color: var(--lin-accent); }
.lin-vs-bar p { margin: 0 0 6px !important; line-height: 1; }
.lin-vs-bar b { font-family: var(--font-mono); font-size: 22px; font-weight: var(--font-weight-medium); }
.lin-vs-row.tracing .lin-vs-bar b { color: var(--lin-tracing); } .lin-vs-row.deep .lin-vs-bar b { color: var(--lin-accent); }
.lin-vs-bar small { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.lin-vs-bar i { display: block; height: 6px; background: var(--color-border); }
.lin-vs-bar i span { display: block; height: 100%; width: var(--w); }
.lin-vs-row.tracing .lin-vs-bar span { background: var(--lin-tracing); } .lin-vs-row.deep .lin-vs-bar span { background: var(--lin-accent); }
.lin-tools { display: grid; gap: var(--space-3); margin-top: var(--space-2); }
.lin-labwrap { margin-top: var(--space-2); }
.lin-labnote { font-size: var(--font-size-sm) !important; color: var(--color-text-secondary); }
.lin-labnote b { color: var(--lin-accent); font-family: var(--font-mono); font-weight: var(--font-weight-medium); }
.lin-lab { display: grid; grid-template-columns: 1fr 340px; border: 1px solid var(--color-border); --l-bg: #eef2f4; --l-surface: #ffffff; --l-text: #18222b; --l-text-2: #4a5763; --l-text-3: #7d8a96; --l-tri: #a99ee6; --l-jur: #7467d0; --l-cre: #40349a; }
.lin-lab-preview { background: var(--l-bg); padding: 20px; display: flex; align-items: center; font-family: "IBM Plex Sans", system-ui, sans-serif; }
.lp-card { background: var(--l-surface); padding: 16px; width: 100%; border: 1px solid #d8e0e5; border-radius: 8px; }
.lp-k { font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--l-text-3); }
.lp-h { font-size: 20px; font-weight: 600; color: var(--l-text); margin: 2px 0; }
.lp-t2 { font-size: 13px; color: var(--l-text-2); }
.lp-t3 { font-size: 12px; color: var(--l-text-3); margin-top: 6px; }
.lp-small { margin-top: 4px; font-size: 11px; }
.lp-bars { display: flex; gap: 3px; margin-top: 12px; height: 10px; }
.lp-bars span { flex: 1; border-radius: 2px; } .lp-tri { background: var(--l-tri); } .lp-jur { background: var(--l-jur); } .lp-cre { background: var(--l-cre); }
.lin-lab-panel { font: 12px/1.35 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; color: #18222b; background: #fff; display: flex; flex-direction: column; }
.ll-head { display: flex; align-items: center; gap: 8px; padding: 10px 12px 6px; font-size: 13px; }
.ll-dim { color: #5b6773; font-size: 11px; }
.ll-btn { margin-left: auto; font: inherit; color: #18222b; background: #f1f4f6; border: 1px solid #c9d2d9; border-radius: 6px; padding: 3px 8px; cursor: pointer; }
.ll-list { padding: 4px 6px; border-top: 1px solid #e3e8ec; border-bottom: 1px solid #e3e8ec; }
.ll-row { display: flex; align-items: center; gap: 8px; padding: 6px; border-radius: 6px; }
.ll-row.changed { background: #fbeefb; }
.ll-sw { position: relative; width: 26px; height: 26px; flex: none; border-radius: 5px; border: 1px solid #c9d2d9; overflow: hidden; cursor: pointer; }
.ll-sw input { position: absolute; inset: 0; opacity: 0; width: 100%; height: 100%; cursor: pointer; }
.ll-mid { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; }
.ll-mid code { font-family: ui-monospace, Menlo, monospace; font-size: 11px; font-weight: 600; background: none; padding: 0; color: #18222b; }
.ll-mid input { font-family: ui-monospace, Menlo, monospace; font-size: 11px; padding: 1px 4px; border: 1px solid transparent; border-radius: 4px; background: #f6f8f9; color: #18222b; width: 100%; }
.ll-cr { display: flex; flex-direction: column; gap: 2px; align-items: flex-end; min-width: 70px; }
.ll-badge { font-size: 10px; font-weight: 700; border-radius: 4px; padding: 0 5px; white-space: nowrap; font-variant-numeric: tabular-nums; }
.ll-badge.ok { background: #dcf3e8; color: #0b5c40; } .ll-badge.no { background: #fbe1e6; color: #8f1538; }
.ll-foot { margin: 0 !important; padding: 6px 12px 10px; color: #5b6773; font-size: 11px !important; line-height: 1.35; }
.lin-dirs { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-3); }
.lin-dir-top { display: flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-size: var(--font-size-sm); margin-bottom: 8px; }
.lin-dir-top b { font-weight: var(--font-weight-medium); }
.lin-dir-top span { font-size: var(--font-size-xs); color: var(--lin-accent); border: 1px solid var(--lin-accent); padding: 0 6px; }
.lin-dir-sw { display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: 64px 22px; gap: 0; border: 1px solid var(--color-border); }
.lin-dir.kept .lin-dir-sw { border-color: var(--lin-accent); }
.lin-dir-sw .aa { grid-column: 1 / -1; margin: 10px; display: flex; align-items: baseline; gap: 10px; padding: 6px 10px; font-family: "IBM Plex Sans", system-ui, sans-serif; font-size: 18px; }
.lin-dir-sw .aa i { font-style: normal; font-weight: 600; }
.lin-dir-final { font-family: var(--font-mono); color: var(--color-text-tertiary) !important; display: flex; align-items: center; gap: 6px; }
.sw-mini { display: inline-block; width: 12px; height: 12px; }
.lin-dir p { font-size: var(--font-size-xs) !important; color: var(--color-text-secondary); margin: 8px 0 0 !important; }
.lin-dir-legend { font-family: var(--font-mono); font-size: var(--font-size-xs) !important; color: var(--color-text-tertiary); margin: var(--space-3) 0 var(--space-2) !important; }
.lin-real { margin-top: var(--space-5); padding-top: var(--space-3); border-top: 1px solid var(--color-border); }

.lin-qs { list-style: none; margin: var(--space-3) 0 0; padding: 0; display: grid; gap: 10px; }
.lin-qs li { border-left: 2px dotted var(--lin-open); padding: 2px 0 2px 12px; color: var(--color-text-secondary); }
.lin-qs li b { color: var(--color-text); font-weight: var(--font-weight-medium); }
.lin-fan { position: relative; height: 260px; }
.lin-fan span { position: absolute; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); white-space: nowrap; opacity: 0; transition: opacity .4s; }
.lin-fan span.is-on { opacity: 1; }
.lin-end { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); margin-left: calc(var(--lin-x) - 4px); position: relative; z-index: 2; }
.lin-end span { background: var(--color-bg); padding: 2px 6px; }


@media (max-width: 760px) {
  :root { --lin-x: -22px; }
  .lin { padding-left: 26px; }
  .lin-from + .lin-from { margin-left: 40px; }
  .lin-compare, .lin-skills { grid-template-columns: 1fr; }
  .lin-vs-grid { grid-template-columns: 140px 24px 140px; row-gap: 8px; }
  .lin-vs-head { display: none; }
  .lin-vs-who, .lin-vs-bar { grid-column: 1 / -1; }
  .lin-order { grid-column: 1 / -1; }
  .lin-vs-row { row-gap: 10px; }
  .lin-lab { grid-template-columns: 1fr; }
  .lin-dirs { grid-template-columns: 1fr 1fr; }
  .lin-fan { height: 320px; }
}
@media (prefers-reduced-motion: reduce) {
  .lin-card, .lin-node, .lin-from { transition: none; }
  .lin-sec.is-on .lin-node::before { animation: none; }
  .lin-sec > .lin-card, .lin-sec > .lin-wide, .lin-sec > .lin-froms { transition: none; }
  .lin-card, .lin-from { opacity: 1; transform: none; }
}
</style>

<div class="lin-intro">
<p class="hib-kicker" style="margin-top:0 !important">Tiny Data Adventures · a work in progress</p>
<p class="lin-lead">I'm a product designer learning, project by project, how to build data apps with Claude. This is what has worked for me so far, told through Deep Lineages, the project where it came together.</p>
<p class="lin-note">The line below is the method; branches show where each lesson came from.</p>
</div>

<div class="lin" id="lin">
<svg class="lin-lines" id="lin-lines" aria-hidden="true"></svg>

<section class="lin-sec lin-wide-sec" data-sec="mess">
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">01</p>
<h2>From a raw export to something anyone can explore</h2>
<p>Real rows from the Paleobiology Database, cleaned, all at once, then the design I made of them.</p>
</div>
<div class="hib-wide lin-wide">
{{< hib-mess >}}
</div>
</section>

<section class="lin-sec" data-sec="directions" data-branches="volcano,tracing">
<div class="lin-froms">
<div class="lin-from volcano" data-from="volcano"><b>Volcano Explorer</b>May 2026 · straight to code: Claude proposed fonts, colors and radii, I edited them. A redesign came in September.</div>
<div class="lin-from tracing" data-from="tracing"><b>Tracing Origins</b>Summer 2026 · straight to code too, and it stayed close to that first proposal.</div>
</div>
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">02</p>
<h2>Look at directions before building one</h2>
<p>My first two projects went with whatever Claude proposed first. In Deep Lineages I asked for four directions, rendered in code on the real app, the same three views each. Lead grey lasted a few minutes; Museum became the base. I kept its palette with a few small changes, the biggest one the accent: from violet to amber.</p>
</div>
<div class="hib-wide lin-wide"><div id="lin-directions"></div></div>
</section>

<section class="lin-sec" data-sec="tokens" data-branches="tracing,volcano">
<div class="lin-froms">
<div class="lin-from tracing" data-from="tracing"><b>Tracing Origins</b>8 Oct 2026 · my first WCAG audit, contrast fixed before any tokens</div>
<div class="lin-from volcano" data-from="volcano"><b>Volcano Explorer</b>11 Oct 2026 · tokens from one tokens.json first, the WCAG audit right after, the same day</div>
</div>
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">03</p>
<h2>Tokens first, then the audit</h2>
<p>The lesson that changed my process most. In Tracing Origins I fixed accessibility first and tokenized afterwards. Three days later, in Volcano Explorer, I flipped the order. Deep Lineages started from tokens and a lab to test them, and the contrast fixes took a fraction of the work.</p>
<div class="lin-vs" role="group" aria-label="The same contrast fix in both projects">
<p class="lin-num lin-task">Same fix in both: make every text color pass WCAG contrast</p>
<div class="lin-vs-grid">
<div class="lin-vs-head" aria-hidden="true"><span></span><span>First</span><span></span><span>Then</span><span>Lines changed</span></div>
<div class="lin-vs-row tracing">
<b class="lin-vs-who">Tracing Origins</b>
<ol class="lin-order"><li class="on">Contrast fixes</li><li>Tokens</li></ol>
<div class="lin-vs-bar"><p><b>~90</b> <small>in App.css</small></p><i><span style="--w:100%"></span></i></div>
</div>
<div class="lin-vs-row deep">
<b class="lin-vs-who">Deep Lineages</b>
<ol class="lin-order"><li>Tokens + lab</li><li class="on">Contrast fixes</li></ol>
<div class="lin-vs-bar"><p><b>5</b> <small>in global.css</small></p><i><span style="--w:5.6%"></span></i></div>
</div>
</div>
</div>

<div class="lin-real"><p class="lin-num">Deep Lineages' tokens</p><div id="lin-tokens"></div></div>
<div class="lin-real"><p class="lin-num">Two tools to check tokens live, in the browser</p>
<div class="lin-tools">
<a class="lin-cmp lin-tool" href="https://deep-lineages.vercel.app/#tokens" target="_blank" rel="noopener"><div class="who">In the app · /#tokens ↗</div><div class="big">/#tokens</div><p>Every token with its live value, contrast per color role, where each one is used, and any value still written by hand.</p></a>
<div class="lin-labwrap">
<p class="lin-labnote"><b>Token Lab</b>, dev only: a floating panel over the app to change tokens and see the WCAG contrast update before anything goes into global.css. Below, a small working copy with three of Deep Lineages' real colors, set to the values they had before the audit. Try fixing them.</p>
<div class="lin-lab">
<div class="lin-lab-preview" id="lab-preview" aria-label="Preview">
<div class="lp-card"><div class="lp-k">Late Cretaceous</div><div class="lp-h">Tyrannosaurus</div><div class="lp-t2">Tyrannosauridae · North America</div><div class="lp-t3">Theropod · meat-eater</div>
<div class="lp-bars"><span class="lp-tri"></span><span class="lp-jur"></span><span class="lp-cre"></span></div><div class="lp-t3 lp-small">Triassic · Jurassic · Cretaceous</div></div>
</div>
<aside class="lin-lab-panel" aria-label="Token lab, a small copy">
<div class="ll-head"><b>🎨 Token lab</b><span class="ll-dim">a small copy</span><button type="button" class="ll-btn" id="lab-reset">Reset</button></div>
<div class="ll-list" id="lab-list"></div>
<p class="ll-foot">Pick a color or type a value and press Enter. Text needs 4.5:1, graphics 3:1; the badge shows the worst pair.</p>
</aside>
</div>
</div>
</div></div>
</div>
</section>

<section class="lin-sec" data-sec="context" data-branches="tracing">
<div class="lin-froms">
<div class="lin-from tracing" data-from="tracing"><b>Tracing Origins</b>Aug 2026 · the CLAUDE.md became a dated decision log, and kept growing.</div>
</div>
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">04</p>
<h2>Context, not prompts</h2>
<p>I talk to Claude like a coworker. The precision lives in two places: a CLAUDE.md in each repo, its memory, and skills, routines that travel between projects.</p>
<div class="lin-real"><p class="lin-num">Three skills distilled from the audits</p>
<div class="lin-skills">
<div class="lin-skill"><code>visual-consistency-qa</code><p>Aligns radius, color roles, spacing and type, so they can become tokens.</p></div>
<div class="lin-skill"><code>design-tokens-system</code><p>Fixes contrast and sizes in one place, and holds each project's visual identity.</p></div>
<div class="lin-skill"><code>wcag-audit-learning</code><p>"Learning" because I check every case by hand and talk each fix through.</p></div>
</div></div>
</div>
</section>

<section class="lin-sec" data-sec="learn">
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">05</p>
<h2>Run the audit myself</h2>
<p>I run the tests and talk each fix through before it's applied, so I understand it instead of just collecting it. Deep Lineages' colors, checked live: contrast, and how they read with color blindness.</p>
<div class="lin-real"><div id="lin-access"></div></div>
</div>
</section>

<section class="lin-sec" data-sec="open" data-open="4">
<span class="lin-node"></span>
<div class="lin-card">
<p class="lin-num">06</p>
<h2>What I haven't figured out yet</h2>
<p>Open branches. If you've solved any of these, I'd like to hear how.</p>
<ul class="lin-qs">
<li><b>Memory that grows.</b> A CLAUDE.md reached 44,000 words and contradicts itself.</li>
<li><b>"It's fixed."</b> I still verify every fix in the browser before I believe it.</li>
<li><b>Real users.</b> It passes my audit, and the apps get a little traffic (I can see it in Vercel Analytics). What I can't see is whether anyone using a screen reader has tried them, or how it went.</li>
<li><b>A team.</b> How does this loop work with engineers and a shared codebase?</li>
</ul>
</div>
<div class="lin-fan" aria-hidden="true"><span data-q="0">Memory that grows</span><span data-q="1">"It's fixed"</span><span data-q="2">Real users</span><span data-q="3">A team</span></div>
</section>

<p class="lin-end"><span>to be continued</span></p>
</div>


<canvas id="lin-field" aria-hidden="true"></canvas>
<style>
/* background: quiet traces, like a seismograph at rest; a click sends a slow swell along them */
#lin-field { position: fixed; inset: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; opacity: 0; transition: opacity 1.2s ease; }
#lin-field.on { opacity: 1; }
/* quieter behind the reading column, so the text always wins */
#lin-field { -webkit-mask-image: linear-gradient(90deg, #000 0, #000 calc(50% - 460px), rgba(0,0,0,.25) calc(50% - 320px), rgba(0,0,0,.25) calc(50% + 320px), #000 calc(50% + 460px), #000 100%); mask-image: linear-gradient(90deg, #000 0, #000 calc(50% - 460px), rgba(0,0,0,.25) calc(50% - 320px), rgba(0,0,0,.25) calc(50% + 320px), #000 calc(50% + 460px), #000 100%); }
@media (max-width: 760px) { #lin-field { -webkit-mask-image: none; mask-image: none; } #lin-field.on { opacity: .6; } }
header.header, main.main, footer.footer { position: relative; z-index: 1; }
.top-link { z-index: 2; }
</style>
<script>
(function () {
  var cv = document.getElementById("lin-field"), ctx = cv && cv.getContext("2d");
  if (!ctx) return;
  // live at the top of <body>, behind header, main and footer (inside the post it would cover the text)
  document.body.insertBefore(cv, document.body.firstChild);
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var css = getComputedStyle(document.documentElement);
  var BG = css.getPropertyValue("--color-bg").trim() || "#111214", ACC = css.getPropertyValue("--accent-glow").trim() || "#c9a7ff";
  var W = 0, H = 0, DPR = Math.min(devicePixelRatio || 1, 2);
  function size() { W = innerWidth; H = innerHeight; cv.width = W * DPR; cv.height = H * DPR; ctx.setTransform(DPR, 0, 0, DPR, 0, 0); }

  // smooth value noise, enough for a calm field
  var P = []; for (var i = 0; i < 512; i++) P[i] = Math.random();
  function h(x, y) { return P[((x * 73856093) ^ (y * 19349663)) & 511]; }
  function sm(t) { return t * t * (3 - 2 * t); }
  function noise(x, y) { var xi = Math.floor(x), yi = Math.floor(y), xf = sm(x - xi), yf = sm(y - yi);
    var a = h(xi, yi), b = h(xi + 1, yi), c = h(xi, yi + 1), d = h(xi + 1, yi + 1); return a + (b - a) * xf + (c - a) * yf + (a - b - c + d) * xf * yf; }

  var rips = []; // {x, y, t}
  addEventListener("click", function (e) {
    if (e.target.closest("a, button, input, select, label, textarea, iframe, .lin-lab")) return;
    rips.push({ x: e.clientX, y: e.clientY, t: performance.now() }); if (rips.length > 5) rips.shift();
    if (reduce) frame(performance.now());
  });

  // SEISMO: a few quiet traces, like a seismograph or a signal monitor; a click sends a pulse along them
  function seismo(now) {
    ctx.clearRect(0, 0, W, H);
    var n = Math.max(7, Math.round(H / 95)), t = now / 1000, gap = H / (n + 1);
    for (var j = 1; j <= n; j++) {
      var y0 = j * gap, hot = 0;
      ctx.beginPath();
      for (var x = 0; x <= W; x += 4) {
        var y = y0 + (noise(x * .006 + t * .15, j * 3.1) - .5) * 14 + Math.sin(x * .02 + t * .8 + j) * 1.2;
        for (var k = 0; k < rips.length; k++) { var r = rips[k], age = (now - r.t) / 1000; if (age > 5) continue;
          var dy = y0 - r.y, dx = x - r.x, front = age * 170, w = Math.abs(dx) - front, fall = 1 - age / 5;
          // a single rounded crest, wide and low, that rolls away from the click and settles
          var amp = Math.exp(-w * w / 14000) * Math.exp(-Math.abs(dy) / 220) * fall * fall; y -= 16 * amp; hot = Math.max(hot, amp); }
        x ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
      }
      ctx.lineWidth = 1; ctx.strokeStyle = hot > .15 ? ACC : "rgba(160,166,176,1)"; ctx.globalAlpha = hot > .15 ? .16 + hot * .22 : .16; ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  function frame(now) { rips = rips.filter(function (r) { return now - r.t < 5000; }); seismo(now); }
  var running = !reduce;
  function loop(now) { if (!running) return; frame(now); requestAnimationFrame(loop); }
  addEventListener("resize", function () { size(); if (reduce) frame(performance.now()); });
  document.addEventListener("visibilitychange", function () { running = !document.hidden && !reduce; if (running) requestAnimationFrame(loop); });
  size();
  if (reduce) frame(0); else requestAnimationFrame(loop);
  cv.classList.add("on");
})();
</script>

{{< hib-evidence >}}
{{< hib-data >}}

<script>
(function () {
  var NS = "http://www.w3.org/2000/svg", story = document.getElementById("lin"), svg = document.getElementById("lin-lines");
  var secs = [].slice.call(story.querySelectorAll(".lin-sec"));
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var trunk, trunkLen = 0, y0 = 0, branches = [], spot, spotG;
  function el(t, a) { var n = document.createElementNS(NS, t); for (var k in a) n.setAttribute(k, a[k]); return n; }
  function narrow() { return innerWidth <= 760; }

  // a real artifact in the column: Deep Lineages' contrast + color-blindness evidence
  try { var D = JSON.parse(document.getElementById("hib-data").textContent), ev = D.projects[0].evidence.access;
    document.getElementById("lin-access").innerHTML = HIB_EV.render(ev, null);
    document.getElementById("lin-tokens").innerHTML = HIB_EV.render(D.projects[0].evidence.polish, null);
    document.getElementById("lin-directions").innerHTML = directions(D.projects[0].evidence.design); } catch (e) { console.log(e); }

  // the four directions as their real palettes: flat swatches, no drawings
  function directions(ev) {
    var keys = [["page", "page"], ["card", "card"], ["ocean", "ocean"], ["land", "land"], ["accent", "accent"], ["ink", "ink"]];
    var h = '<div class="lin-dirs">' + ev.items.map(function (it) {
      return '<div class="lin-dir' + (it.kept ? " kept" : "") + '"><div class="lin-dir-top"><b>' + it.name + '</b>' + (it.kept ? '<span>Kept</span>' : "") + '</div>' +
        '<div class="lin-dir-sw" style="background:' + it.page + '"><span class="aa" style="color:' + it.ink + ';background:' + it.card + '">Aa <i style="color:' + it.number + '">150</i></span>' +
        keys.slice(1).map(function (k) { return '<span class="sw" title="' + k[1] + " " + it[k[0]] + '" style="background:' + it[k[0]] + '"></span>'; }).join("") + '</div>' +
        '<p>' + it.note + '</p>' +
        // what changed after picking it: the accent (amber-600 in Deep Lineages' global.css)
        (it.kept ? '<p class="lin-dir-final">Then: accent <span class="sw-mini" style="background:' + it.accent + '"></span> → <span class="sw-mini" style="background:#b57500"></span> amber</p>' : "") + '</div>';
    }).join("") + '</div>';
    h += '<p class="lin-dir-legend">Swatches: page with text and the big number · card · ocean · land · accent · ink. Each direction was applied to the same 3 views: ' + ev.views.join(", ") + '.</p>';
    return h;
  }

  // the small token lab: real Deep Lineages colors, starting from their pre-audit values
  (function () {
    var lab = document.querySelector(".lin-lab"); if (!lab) return;
    var BG = { "--bg": "#eef2f4", "--surface": "#ffffff" };
    var T = [
      { name: "--text-3", v: "#7d8a96", fixed: "#5f6b76", need: 4.5, on: ["--bg", "--surface"], role: "text", css: "--l-text-3" },
      { name: "--text-2", v: "#4a5763", fixed: "#4a5763", need: 4.5, on: ["--bg", "--surface"], role: "text", css: "--l-text-2" },
      { name: "--period-tri", v: "#a99ee6", fixed: "#9284dc", need: 3, on: ["--surface"], role: "graphic", css: "--l-tri" }
    ];
    T.forEach(function (t) { t.start = t.v; });
    function lum(hex) { var c = hex.replace("#", ""); if (c.length === 3) c = c.replace(/./g, "$&$&"); return [0, 2, 4].map(function (i) { var x = parseInt(c.substr(i, 2), 16) / 255; return x <= .03928 ? x / 12.92 : Math.pow((x + .055) / 1.055, 2.4); }).reduce(function (a, x, i) { return a + x * [.2126, .7152, .0722][i]; }, 0); }
    function ratio(a, b) { var A = lum(a), B = lum(b); return (Math.max(A, B) + .05) / (Math.min(A, B) + .05); }
    var list = document.getElementById("lab-list");
    function draw() {
      list.innerHTML = T.map(function (t, i) {
        var worst = Math.min.apply(null, t.on.map(function (b) { return ratio(t.v, BG[b]); })), ok = worst >= t.need;
        lab.style.setProperty(t.css, t.v);
        return '<div class="ll-row' + (t.v !== t.start ? " changed" : "") + '"><label class="ll-sw" style="background:' + t.v + '" title="Pick a color"><input type="color" data-i="' + i + '" value="' + t.v + '" aria-label="' + t.name + '"></label>' +
          '<div class="ll-mid"><code>' + t.name + '</code><input data-i="' + i + '" value="' + t.v + '" aria-label="' + t.name + ' value"></div>' +
          '<div class="ll-cr"><span class="ll-badge ' + (ok ? "ok" : "no") + '">' + worst.toFixed(1) + (ok ? " ✓" : " ✗") + '</span><span class="ll-dim">' + t.role + ', ' + t.need + ':1</span></div></div>';
      }).join("");
    }
    function set(i, v) { v = v.trim(); if (!/^#([0-9a-f]{3}|[0-9a-f]{6})$/i.test(v)) return; if (v.length === 4) v = "#" + v.slice(1).replace(/./g, "$&$&"); T[i].v = v.toLowerCase(); draw(); }
    list.addEventListener("input", function (e) { if (e.target.type === "color") set(+e.target.dataset.i, e.target.value); });
    list.addEventListener("keydown", function (e) { if (e.key === "Enter" && e.target.type === "text") set(+e.target.dataset.i, e.target.value); });
    list.addEventListener("change", function (e) { if (e.target.type === "text") set(+e.target.dataset.i, e.target.value); });
    document.getElementById("lab-reset").addEventListener("click", function () { T.forEach(function (t) { t.v = t.start; }); draw(); });
    draw();
  })();

  function build() {
    svg.innerHTML = '<defs>' +
      // Aurora along the trunk: white and violet sliding slowly down the line
      '<linearGradient id="lin-aurora" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="700" spreadMethod="reflect">' +
      '<stop offset="0" style="stop-color:var(--accent-glow)"/><stop offset=".5" style="stop-color:var(--accent-light)"/><stop offset="1" style="stop-color:var(--accent-glow)"/>' +
      (reduce ? "" : '<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="0 1400" dur="12s" repeatCount="indefinite"/>') + '</linearGradient>' +
      '<radialGradient id="lin-spot" gradientUnits="userSpaceOnUse" cx="-999" cy="-999" r="190">' +
      '<stop offset="0" style="stop-color:var(--accent-light)"/><stop offset=".4" style="stop-color:var(--accent-glow)"/><stop offset="1" style="stop-color:var(--accent-glow);stop-opacity:0"/></radialGradient></defs>';
    spot = el("g", { class: "lin-spot" }); branches = [];
    var box = story.getBoundingClientRect(), nodes = secs.map(function (s) { var r = s.querySelector(".lin-node"); var b = r.getBoundingClientRect(); return { x: b.left + b.width / 2 - box.left, y: b.top + b.height / 2 - box.top }; });
    // place each node beside its section's first line
    secs.forEach(function (s) { var c = s.querySelector(".lin-card"), n = s.querySelector(".lin-node"); n.style.top = (c.offsetTop + 6) + "px"; });
    nodes = secs.map(function (s) { var b = s.querySelector(".lin-node").getBoundingClientRect(); return { x: b.left + b.width / 2 - box.left, y: b.top + b.height / 2 - box.top }; });
    var x = nodes[0].x; y0 = nodes[0].y;
    var y1 = story.querySelector(".lin-end").getBoundingClientRect().top - box.top + 10;
    // the trunk stops where a full-width block starts and picks up after it
    var gaps = [].slice.call(story.querySelectorAll(".lin-wide")).map(function (w) { var r = w.getBoundingClientRect(); return [r.top - box.top - 16, r.bottom - box.top + 16]; });
    var d = "", y = y0;
    gaps.forEach(function (g) { d += "M" + x + " " + y + "V" + g[0]; y = g[1]; });
    d += "M" + x + " " + y + "V" + y1;
    svg.appendChild(el("path", { class: "lin-trunk-bg", d: d }));
    trunk = el("path", { class: "lin-trunk", d: d }); svg.appendChild(trunk);
    trunkLen = trunk.getTotalLength(); trunk.style.strokeDasharray = trunkLen + " " + trunkLen; trunk.style.strokeDashoffset = trunkLen;
    trunk._gaps = gaps; trunk._y1 = y1;
    trunk._spot = el("path", { d: d }); spot.appendChild(trunk._spot);

    secs.forEach(function (s, i) {
      var n = nodes[i];
      (s.dataset.branches || "").split(",").filter(Boolean).forEach(function (kind) {
        var lab = s.querySelector('[data-from="' + kind + '"]'), lr = lab.getBoundingClientRect(), ly = lr.top + 9 - box.top, sx = lr.left - box.left - 8;
        var p = el("path", { class: "lin-branch " + kind, d: "M" + sx + " " + ly + " C" + (n.x + (sx - n.x) * .25) + " " + ly + " " + n.x + " " + (ly + (n.y - ly) * .45) + " " + n.x + " " + n.y });
        svg.appendChild(p); var L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L;
        var sp = el("path", { d: p.getAttribute("d") }); spot.appendChild(sp);
        branches.push({ p: p, L: L, sec: s, lab: lab, sp: sp });
      });
      var k = +s.dataset.open || 0, fan = s.querySelector(".lin-fan");
      if (!fan) return;
      var fr = fan.getBoundingClientRect(), fy = fr.top - box.top;
      for (var j = 0; j < k; j++) {
        var reach = narrow() ? 46 + (k - 1 - j) * 22 : 90 + (k - 1 - j) * 150, sy = fy + 10 + j * 26, ex = n.x + reach, ey = fy + (narrow() ? 70 + j * 62 : 80 + j * 46);
        var q = el("path", { class: "lin-branch open", d: "M" + n.x + " " + sy + " C" + n.x + " " + (sy + 55) + " " + ex + " " + (ey - 55) + " " + ex + " " + ey });
        var c = el("circle", { class: "lin-endopen", cx: ex, cy: ey, r: 4 }); svg.appendChild(q); svg.appendChild(c);
        var lab2 = fan.querySelector('[data-q="' + j + '"]'); lab2.style.top = (ey - fy - 8) + "px"; lab2.style.left = (ex - (fr.left - box.left) + 10) + "px";
        branches.push({ p: q, sec: s, end: c, lab: lab2, open: true, idx: j, anchor: fan });
      }
    });
    svg.appendChild(spot); spotG = svg.querySelector("#lin-spot");
    update();
  }

  // the spotlight follows the pointer over the lines and over the comparison cards
  addEventListener("pointermove", function (e) {
    if (spotG) { var b = story.getBoundingClientRect(); spotG.setAttribute("cx", e.clientX - b.left); spotG.setAttribute("cy", e.clientY - b.top); }
    var c = e.target.closest && e.target.closest(".lin-cmp");
    if (c) { var r = c.getBoundingClientRect(); c.style.setProperty("--x", (e.clientX - r.left) + "px"); c.style.setProperty("--y", (e.clientY - r.top) + "px"); }
  }, { passive: true });

  var lastH = 0;
  function update() {
    // anything above changed height (the mess block steps, fonts, the iframe): redraw from the new layout
    if (story.offsetHeight !== lastH) { lastH = story.offsetHeight; build(); return; }
    var vh = innerHeight, line = vh * 0.55, box = story.getBoundingClientRect();
    if (trunk) {
      // length drawn = distance from the trunk's top to the reading line, minus the gaps above it
      var target = line - box.top, drawn = target - y0;
      trunk._gaps.forEach(function (g) { if (target > g[1]) drawn -= g[1] - g[0]; else if (target > g[0]) drawn -= target - g[0]; });
      drawn = reduce ? trunkLen : Math.max(0, Math.min(trunkLen, drawn));
      trunk.style.strokeDashoffset = trunkLen - drawn;
      trunk._spot.style.strokeDasharray = trunkLen + " " + trunkLen; trunk._spot.style.strokeDashoffset = trunkLen - drawn;
    }
    var cur = secs[0];
    secs.forEach(function (s) { var r = s.querySelector(".lin-node").getBoundingClientRect(), on = r.top < line + 40 && r.top > -vh * .2; s.classList.toggle("is-on", on); if (r.top < line) { s.classList.add("was-on"); cur = s; } });
    // one section in focus at a time: the one whose node last crossed the reading line
    secs.forEach(function (s) { s.classList.toggle("is-current", s === cur); });
    branches.forEach(function (b) {
      var r = (b.anchor || b.sec.querySelector(".lin-node")).getBoundingClientRect();
      var t = reduce ? 1 : Math.max(0, Math.min(1, (vh * .95 - r.top) / (vh * .4) - (b.open ? b.idx * .15 : 0)));
      if (b.open) { b.p.style.opacity = t > .2 ? 1 : 0; b.end.style.opacity = t > .2 ? 1 : 0; } else { b.p.style.strokeDashoffset = b.L * (1 - t); b.sp.style.strokeDasharray = b.L; b.sp.style.strokeDashoffset = b.L * (1 - t); }
      if (b.lab) b.lab.classList.toggle("is-on", t > (b.open ? .2 : .15));
    });
  }

  var raf = 0; addEventListener("scroll", function () { if (!raf) raf = requestAnimationFrame(function () { raf = 0; update(); }); }, { passive: true });
  var rt; addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(build, 150); });
  // the mess block changes height as it steps: rebuild when it does
  if (window.ResizeObserver) new ResizeObserver(function () { requestAnimationFrame(update); }).observe(story);
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () { setTimeout(build, 300); });
})();
</script>
