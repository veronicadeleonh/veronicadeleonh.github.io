---
title: "How I build Tiny Data Adventures"
layout: "page"
url: "/how-i-build/"
pageTheme: "dark"
summary: "Me × Claude Code: the loop, the context and the commits behind my data projects"
---

<style>
/* Dark theme and bright accents come from the design system: custom.css, `pageTheme: dark` */
/* Bands (.hib-wide): the translucent band marks what you use (pick, hover, try); reading stays on the plain page (.hib-wide--plain). */
.hib-lead { font-size: var(--font-size-lg) !important; line-height: 1.4em; color: var(--color-text-secondary); }
.hib-kicker { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); text-transform: uppercase; letter-spacing: .04em; margin: var(--space-5) 0 var(--space-1) !important; }
.post-content h2.hib-h2 { margin-top: 0; }
.hib-wide { width: min(980px, calc(100vw - 32px)); position: relative; left: 50%; transform: translateX(-50%); }
/* full-bleed translucent band behind the wide sections; box-shadow paints past the edges without causing horizontal scroll */
:root { --hib-band: rgba(255, 255, 255, .035); }
.hib-wide { padding: var(--space-5) 0; margin: var(--space-4) 0; background: var(--hib-band); box-shadow: 0 0 0 100vmax var(--hib-band); clip-path: inset(0 -100vmax); }
.hib-wide--plain { padding: var(--space-2) 0 0; background: none; box-shadow: none; clip-path: none; }
/* owner glyphs */
/* lanes: yellow = me, purple = Claude Code */
:root { --hib-me: var(--color-yellow); --hib-ai: var(--color-purple); }
.own { display: inline-block; flex-shrink: 0; width: 10px; height: 10px; vertical-align: middle; margin-right: 6px; }
.own--me { background: var(--hib-me); }
.own--ai { background: var(--hib-ai); }
.own--both { background: linear-gradient(90deg, var(--hib-me) 50%, var(--hib-ai) 50%); }
.hib-owners { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-3); font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-secondary); margin-bottom: var(--space-3); }
.hib-owners-label { color: var(--color-text-tertiary); text-transform: uppercase; letter-spacing: .04em; font-size: var(--font-size-xs); }
/* the loop as two lanes */
.hib-lanes { display: grid; grid-template-columns: 96px repeat(7, minmax(0, 1fr)); column-gap: var(--space-2); row-gap: 4px; }
.hib-lane-labels { grid-column: 1; grid-row: 1 / 5; display: grid; grid-template-rows: subgrid; }
.hib-lane-label { display: flex; align-items: center; align-self: start; padding-top: var(--space-2); line-height: 1.45; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-secondary); }
.hib-timeaxis { grid-column: 2 / -1; grid-row: 1; position: relative; height: 1px; margin: 0 0 var(--space-3); background: linear-gradient(90deg, var(--color-border), var(--color-text-tertiary)); }
.hib-timeaxis::after { content: ""; position: absolute; right: -1px; top: -3px; border: 3.5px solid transparent; border-left: 6px solid var(--color-text-tertiary); border-right: 0; }
.hib-axis-dot { position: absolute; top: -3px; left: 0; width: 7px; height: 7px; background: var(--color-text); animation: hib-slide 12s linear infinite; }
@keyframes hib-slide { from { left: 0; } to { left: calc(100% - 7px); } }
.hib-col { grid-row: 2 / 5; display: grid; grid-template-rows: subgrid; }
.hib-node { position: relative; padding: 8px 10px; margin-bottom: var(--space-1); background: linear-gradient(var(--hib-band), var(--hib-band)), var(--color-bg); border: 1px solid var(--color-text); font-family: var(--font-mono); font-size: var(--font-size-xs); line-height: 1.35; text-align: left; cursor: pointer; color: var(--color-text); transition: background var(--transition-fast), color var(--transition-fast); }
.hib-node .n { display: block; color: var(--color-text-tertiary); }
.hib-node .l { display: block; font-size: var(--font-size-sm); font-family: var(--font-sans); font-weight: var(--font-weight-medium); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.hib-node:hover { background: var(--color-surface); }
.hib-node[aria-pressed="true"] { background: var(--color-text); color: var(--color-bg); }
.hib-node[aria-pressed="true"] .n { color: var(--color-surface-active); }
.hib-cell { padding: var(--space-2); font-size: var(--font-size-sm); line-height: 1.45; color: var(--color-text-secondary); transition: background var(--transition-fast), color var(--transition-fast); }
.hib-cell--me { background: color-mix(in srgb, var(--hib-me) 11%, transparent); border-top: 2px solid var(--hib-me); }
.hib-cell--ai { background: color-mix(in srgb, var(--hib-ai) 12%, transparent); border-top: 2px solid var(--hib-ai); }
.hib-col.is-active .hib-cell { color: var(--color-text); }
.hib-col.is-active .hib-cell--me { background: color-mix(in srgb, var(--hib-me) 22%, transparent); }
.hib-col.is-active .hib-cell--ai { background: color-mix(in srgb, var(--hib-ai) 24%, transparent); }
.hib-back { grid-column: 5 / 8; grid-row: 5; position: relative; height: 14px; margin-top: var(--space-2); border: 1px dashed var(--color-text-tertiary); border-top: 0; }
.hib-back::before { content: ""; position: absolute; left: -4.5px; top: -7px; border: 4px solid transparent; border-bottom: 6px solid var(--color-text-tertiary); border-top: 0; }
.hib-back-label { grid-column: 5 / 8; grid-row: 6; text-align: center; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); margin: 4px 0 0 !important; }
.hib-next-label { grid-column: 8; grid-row: 5 / 7; align-self: start; text-align: center; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); margin: var(--space-2) 0 0 !important; }
.hib-core { grid-column: 1 / -1; grid-row: 7; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: var(--space-3); margin-top: var(--space-4); padding: var(--space-3); border: 1px dashed var(--color-border); }
.hib-core p { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-secondary); margin: 0 !important; }
.hib-core button { font-family: var(--font-mono); font-size: var(--font-size-xs); padding: 6px 12px; background: var(--color-surface); border: 1px dashed var(--color-text-tertiary); color: var(--color-text); cursor: pointer; }
.hib-core button:hover { background: var(--color-surface-hover); }
.hib-core button[aria-pressed="true"] { background: var(--color-text); color: var(--color-bg); border-style: solid; border-color: var(--color-text); }
.hib-panel { max-width: var(--main-width, 620px); margin: var(--space-5) auto 0; border-top: 1px solid var(--color-text); padding-top: var(--space-3); }
.hib-panel .hib-step { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); margin: 0 !important; }
.post-content .hib-panel h3 { margin: var(--space-1) 0 var(--space-2); font-size: var(--font-size-lg); }
.hib-panel p { font-size: var(--font-size-base); margin-bottom: var(--space-3) !important; }
.hib-note { background: var(--color-surface); padding: var(--space-3); }
.hib-note-row { padding: var(--space-2) 0; border-top: 1px solid var(--color-border); }
.hib-note-row:first-of-type { border-top: 0; padding-top: 0; }
.hib-note-row:last-child { padding-bottom: 0; }
.hib-note-proj { display: block; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-secondary); margin-bottom: 2px; }
.hib-note-label { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); display: block; margin-bottom: var(--space-1); }
.hib-note p { margin: 0 !important; }
.hib-note ul { margin: 0; padding-left: var(--space-3); }
.hib-note li { font-size: var(--font-size-base); margin-bottom: var(--space-2); }
.hib-hint { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
/* project tabs under the loop: which project(s) the step panel shows */
.hib-tabs { max-width: var(--main-width, 620px); margin: var(--space-5) auto 0; display: flex; border: 1px solid var(--color-text); overflow-x: auto; scrollbar-width: none; }
.hib-tabs button { flex: 1 0 auto; background: none; border: 0; border-left: 1px solid var(--color-text); padding: 7px 10px; min-height: 32px; font-family: var(--font-sans); font-size: var(--font-size-tag); color: var(--color-text-secondary); cursor: pointer; white-space: nowrap; transition: background var(--transition-fast), color var(--transition-fast); }
.hib-tabs button:first-child { border-left: 0; }
.hib-tabs button:hover { background: var(--color-surface); color: var(--color-text); }
.hib-tabs button[aria-selected="true"] { background: var(--color-text); color: var(--color-bg); }
.hib-tabs .short { display: none; }
.hib-tabs + .hib-panel { margin-top: var(--space-3); }
/* skills */
.hib-skills { display: flex; flex-direction: column; gap: var(--space-2); margin-top: var(--space-3); }
.hib-skill { border: 1px solid var(--color-border); padding: var(--space-3); display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: var(--space-1) var(--space-3); align-items: baseline; }
.hib-skill p { grid-column: 2; }
.hib-skill code { grid-row: 1; }
.hib-skill code { font-family: var(--font-mono); font-size: var(--font-size-sm); background: none; padding: 0; color: var(--color-text); }
.hib-skill p { font-size: var(--font-size-base); margin: 0 !important; }
/* Spotlight (hover): a light follows the cursor along the border and inside.
   Aurora (active): selected elements fill with a slow, liquid light. Both "Mono + violet".
   Overlays only: the element itself never changes size, and the loop lines can't show through. */
.hib-spot { --x: 50%; --y: 50%; position: relative; isolation: isolate; }
.hib-spot::before { content: ""; position: absolute; inset: -1px; padding: 1px; pointer-events: none; opacity: 0; transition: opacity var(--transition-base) ease;
  background: radial-gradient(150px circle at var(--x) var(--y), var(--accent-light), var(--accent-glow) 40%, transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; }
.hib-spot:not(.hib-cell)::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: 0; transition: opacity var(--transition-base) ease;
  background: radial-gradient(200px circle at var(--x) var(--y), color-mix(in srgb, var(--accent-glow) 20%, transparent), transparent 70%); }
.hib-spot:is(:hover, :focus-visible)::before, .hib-spot:not(.hib-cell):is(:hover, :focus-visible)::after { opacity: 1; }
.hib-spot:is(:hover, :focus-visible):not([aria-pressed="true"]):not(.hib-cell) { border-color: var(--color-border); }
.hib-spot[aria-pressed="true"]::before, .hib-spot[aria-pressed="true"]::after { display: none; }
.hib-aurora { isolation: isolate; overflow: hidden; } /* parent must already be positioned */
.hib-aurora::before { content: ""; position: absolute; inset: -40%; z-index: -1; pointer-events: none; background: var(--gradient-aurora), var(--color-text); animation: aurora-move 6s ease-in-out infinite alternate; }
.hib-node[aria-pressed="true"], .hib-core button[aria-pressed="true"] { position: relative; isolation: isolate; overflow: hidden; }
.hib-node[aria-pressed="true"]::after, .hib-core button[aria-pressed="true"]::after { content: ""; position: absolute; inset: -40%; z-index: -1; pointer-events: none; display: block; opacity: 1; background: var(--gradient-aurora), var(--color-text); animation: aurora-move 6s ease-in-out infinite alternate; }
/* lane cells share the steps' motion: spotlight in the lane's color on hover, aurora in the lane's color when the step is active */
.hib-cell { position: relative; isolation: isolate; overflow: hidden; }
.hib-cell--me { --accent-glow: var(--hib-me); }
.hib-cell--ai { --accent-glow: var(--hib-ai); }
.hib-cell.hib-spot::before { inset: 0; padding: 0; -webkit-mask: none; mask: none; z-index: -1; background: radial-gradient(170px circle at var(--x) var(--y), color-mix(in srgb, var(--accent-glow) 38%, transparent), transparent 70%); }
.hib-col.is-active .hib-cell::after { content: ""; position: absolute; inset: -40%; z-index: -1; pointer-events: none; opacity: .32; background: radial-gradient(40% 50% at 30% 40%, var(--accent-glow), transparent 70%), radial-gradient(35% 45% at 70% 65%, color-mix(in srgb, var(--accent-glow) 60%, #fff), transparent 70%); animation: aurora-move 6s ease-in-out infinite alternate; }
.hib-col.is-active .hib-cell.hib-spot:hover::after { opacity: .45; }
/* "In each project": rows rise in, one after another, whenever the step or the tab changes */
@keyframes hib-rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
.hib-panel > div:first-child { animation: hib-rise .35s ease both; }
.hib-note { position: relative; overflow: hidden; }
.hib-note::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(var(--accent-light), var(--accent-glow)); transform-origin: top; animation: hib-grow .6s ease both; }
@keyframes hib-grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
.hib-note-row { animation: hib-rise .45s ease both; animation-delay: calc(var(--i, 0) * 80ms + 80ms); }
.hib-callout { border-left: 2px solid var(--color-text); padding: var(--space-1) 0 var(--space-1) var(--space-3); color: var(--color-text-secondary); }
.hib-callout strong { color: var(--color-text); }
/* the shared portfolio intro (tag, description, details) on this dark page: light icons */
.intro-details .fi { filter: invert(1); opacity: .75; }
.hib-sys-intro { margin-top: var(--space-4) !important; }
.hib-syslinks { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-2); margin-top: var(--space-2); }
.post-content .hib-syslinks a { position: relative; isolation: isolate; display: flex; flex-direction: column; gap: 2px; padding: var(--space-2) var(--space-3); border: 1px solid var(--color-border); color: var(--color-text); text-decoration: none; box-shadow: none; font-weight: var(--font-weight-regular); font-size: var(--font-size-sm); }
.post-content .hib-syslinks a code { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); background: none; padding: 0; margin: 0; box-shadow: none; border: 0; text-decoration: none; }
.post-content h3.hib-h3 { margin: var(--space-5) 0 var(--space-2); font-size: var(--font-size-lg); }
/* section 03: milestone marks over the commit rows, and the monthly mix of phases under them */
.hib-chart { position: relative; --lab: 150px; }
.hib-marks, .hib-mix { display: grid; grid-template-columns: var(--lab) 1fr; gap: var(--space-3); align-items: end; }
.hib-marks-track { position: relative; height: 74px; }
.hib-mark { position: absolute; bottom: 0; transform: translateX(-4px); display: flex; flex-direction: column; align-items: flex-start; gap: 3px; background: none; border: 0; padding: 0; cursor: default; color: var(--color-text-secondary); font-family: var(--font-mono); font-size: var(--font-size-xs); white-space: nowrap; }
.hib-mark span { position: absolute; left: 0; bottom: calc(14px + var(--lv, 0) * 20px); }
.hib-mark.is-left span { left: auto; right: 0; }
.hib-mark::after { content: ""; width: 9px; height: 9px; transform: rotate(45deg); background: var(--color-bg); border: 1px solid var(--color-text); }
.hib-mark:hover, .hib-mark:focus-visible, .hib-mark.is-current { color: var(--color-text); outline: none; }
.hib-mark:hover::after, .hib-mark:focus-visible::after, .hib-mark.is-current::after { background: var(--color-text); box-shadow: 0 0 10px var(--accent-glow); }
.hib-mark-line { position: absolute; top: 74px; bottom: 16px; width: 0; border-left: 1px dashed var(--color-text-tertiary); opacity: .45; pointer-events: none; transition: opacity var(--transition-fast); }
.hib-mark-line.is-current { opacity: 1; border-left-color: var(--color-text); }
.hib-mix { margin-top: var(--space-3); }
.hib-mix .hib-row-label { color: var(--color-text-tertiary); font-size: var(--font-size-xs); font-family: var(--font-mono); }
.hib-mix-track { position: relative; height: 56px; }
.hib-mix-col { position: absolute; bottom: 0; top: 0; display: flex; flex-direction: column-reverse; padding: 0 1px; }
.hib-mix-col span { display: block; transition: opacity var(--transition-fast); }
.hib-mix-col span.is-off { opacity: .12; }
/* project cards (section 04) */
.hib-cards { display: grid; grid-template-columns: repeat(var(--hib-n, 3), minmax(0, 1fr)); gap: var(--space-3); }
.hib-card { position: relative; display: flex; flex-direction: column; padding: 0; text-align: left; font: inherit; color: var(--color-text); background: var(--color-bg); border: 1px solid var(--color-border); cursor: pointer; overflow: hidden; transition: opacity var(--transition-base), border-color var(--transition-fast); }
.hib-card-img { display: block; overflow: hidden; border-bottom: 1px solid var(--color-border); }
.hib-card-img img { display: block; width: 100%; aspect-ratio: 16 / 9; object-fit: cover; object-position: top; transition: transform .6s cubic-bezier(.2, .7, .2, 1); }
.hib-card:hover .hib-card-img img, .hib-card.is-active .hib-card-img img { transform: scale(1.04); }
.hib-card-body { display: flex; flex-direction: column; gap: var(--space-1); padding: var(--space-3); }
.hib-card time { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.hib-card-name { font-size: var(--font-size-md); font-weight: var(--font-weight-medium); }
.hib-card-lesson { font-size: var(--font-size-sm); line-height: 1.5; color: var(--color-text-secondary); margin-bottom: var(--space-1); }
.post-content .hib-takeaways { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-4) var(--space-3); }
.post-content .hib-takeaways li { position: relative; display: flex; flex-direction: column; gap: var(--space-1); margin: 0; padding: var(--space-3) 0 0; border-top: 1px solid var(--color-border); }
.hib-tk-n { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.post-content .hib-takeaways h3 { margin: 0; font-size: var(--font-size-lg); font-weight: var(--font-weight-medium); line-height: 1.25; color: var(--color-text); }
.post-content .hib-takeaways p { margin: 0; font-size: var(--font-size-sm); line-height: 1.55; color: var(--color-text-secondary); }
.post-content .hib-takeaways li::before { content: ""; position: absolute; left: 0; right: 0; top: -1px; height: 1px; background: linear-gradient(90deg, var(--accent-light), var(--accent-glow) 40%, transparent); transform: scaleX(0); transform-origin: left; transition: transform .6s cubic-bezier(.2, .7, .2, 1); }
.post-content .hib-takeaways li:hover::before { transform: scaleX(1); }
.post-content .hib-takeaways li:hover p { color: var(--color-text); }
@media (max-width: 860px) { .post-content .hib-takeaways { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 600px) { .post-content .hib-takeaways { grid-template-columns: 1fr; gap: var(--space-3); } .post-content .hib-takeaways h3 { font-size: var(--font-size-md); } }
@media (prefers-reduced-motion: reduce) { .post-content .hib-takeaways li::before { transition: none; } }
.hib-flow { display: flex; flex-direction: column; gap: var(--space-1); margin: var(--space-1) 0; padding: var(--space-2) 0 0; border-top: 1px solid var(--color-border); font-size: var(--font-size-sm); line-height: 1.45; color: var(--color-text-secondary); }
.hib-flow-row { display: flex; flex-direction: column; gap: 1px; }
.hib-flow-row.is-to { color: var(--color-text); }
.hib-flow-k { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.hib-flow-row.is-to .hib-flow-k::before { content: "→ "; color: var(--accent-glow); }
.hib-tags { display: flex; flex-wrap: wrap; gap: 4px; }
.hib-tags span { font-family: var(--font-mono); font-size: var(--font-size-xs); padding: 1px 6px; border: 1px solid var(--color-border); color: var(--color-text-secondary); }
.hib-card-bar { position: absolute; left: 0; right: 0; top: 0; height: 3px; z-index: 2; opacity: 0; background: linear-gradient(90deg, var(--accent-glow), var(--accent-light), var(--accent-glow)); background-size: 200% 100%; transition: opacity var(--transition-base); animation: hib-bar 3s linear infinite; }
@keyframes hib-bar { from { background-position: 0% 0; } to { background-position: 200% 0; } }
.hib-card.is-active { border-color: var(--color-text); }
.hib-card.is-active .hib-card-bar { opacity: 1; }
.hib-card.is-active .hib-card-lesson { color: var(--color-text); }
.hib-cards.has-active .hib-card:not(.is-active) { opacity: .5; }
.hib-cards.has-active .hib-card:not(.is-active):hover { opacity: .85; }
.hib-story { margin-top: var(--space-4); border-top: 1px solid var(--color-text); padding-top: var(--space-3); animation: hib-rise .4s ease both; }
.hib-story-head h3 { margin: var(--space-1) 0 var(--space-1) !important; font-size: var(--font-size-lg); }
/* commits */
.hib-legend { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-3); }
.hib-legend button { display: inline-flex; align-items: center; gap: 6px; font-family: var(--font-mono); font-size: var(--font-size-xs); padding: 4px 8px; background: var(--color-bg); border: 1px solid var(--color-border); cursor: pointer; color: var(--color-text); }
.hib-legend button[aria-pressed="false"] { opacity: .45; text-decoration: line-through; }
.hib-legend i, .hib-dot { display: inline-block; width: 8px; height: 8px; box-shadow: inset 0 0 0 1px rgba(255,255,255,.18); }
.hib-rows { display: flex; flex-direction: column; gap: var(--space-3); }
.hib-syslinks .is-next { display: flex; flex-direction: column; gap: 2px; padding: var(--space-2) var(--space-3); border: 1px dashed var(--color-border); color: var(--color-text-secondary); font-size: var(--font-size-sm); }
.hib-syslinks .is-next code { font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); background: none; padding: 0; margin: 0; border: 0; }
.hib-card-img { position: relative; }
.hib-status { position: absolute; top: 8px; left: 8px; z-index: 1; display: inline-flex; align-items: center; gap: 6px; padding: 2px 8px; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text); background: rgba(14, 16, 17, .82); border: 1px solid var(--color-text); }
.hib-status::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--accent-glow); animation: hib-pulse 1.6s ease-in-out infinite; }
@keyframes hib-pulse { 50% { opacity: .25; } }
.hib-next { display: inline-block; margin-right: 6px; padding: 0 6px; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-secondary); border: 1px dashed var(--color-text-tertiary); vertical-align: 1px; }
.hib-note-row.is-next p { color: var(--color-text-secondary); }
@media (min-width: 761px) and (max-width: 1040px) { .hib-cards, .hib-syslinks { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.hib-row { display: grid; grid-template-columns: 150px 1fr; gap: var(--space-3); align-items: end; transition: opacity var(--transition-base); }
.hib-row.is-dim { opacity: .25; }
.hib-row-label { font-size: var(--font-size-sm); padding-bottom: 2px; }
.hib-row-label small { display: block; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.hib-track { position: relative; border-bottom: 1px solid var(--color-text); }
.hib-dot { position: absolute; width: 6px; height: 6px; transition: opacity var(--transition-fast); }
.hib-dot.is-off { opacity: .06; }
.hib-axis { display: grid; grid-template-columns: 150px 1fr; gap: var(--space-3); margin-top: 4px; }
.hib-axis div { position: relative; height: 16px; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); }
.hib-axis span { position: absolute; white-space: nowrap; transform: translateX(-50%); }
.hib-readout { display: flex; align-items: flex-start; gap: var(--space-2); font-family: var(--font-mono); font-size: var(--font-size-sm); line-height: 1.6; color: var(--color-text-secondary); margin-top: var(--space-3) !important; min-height: 2.8em; }
.hib-readout-dot { flex-shrink: 0; width: 10px; height: 10px; margin-top: calc((1.6em - 10px) / 2); border: 1px dashed var(--color-text-tertiary); transition: background var(--transition-fast), transform var(--transition-fast); }
.hib-readout.has-commit .hib-readout-dot { border: 0; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .18); transform: scale(1.2); }
.hib-readout.has-commit { color: var(--color-text); }
.hib-dot { transition: opacity var(--transition-fast), transform var(--transition-fast), box-shadow var(--transition-fast); }
.hib-dot:hover, .hib-dot.is-current { transform: scale(1.9); z-index: 2; box-shadow: 0 0 0 1px var(--color-bg), 0 0 10px color-mix(in srgb, var(--accent-glow) 60%, transparent); }
.hib-datanote { background: var(--color-surface); padding: var(--space-3); margin-top: var(--space-3); }
.hib-datanote p { font-size: var(--font-size-sm) !important; color: var(--color-text-secondary); margin: 0 0 var(--space-1) !important; }
.hib-datanote p:last-child { margin-bottom: 0 !important; }
/* stories */
.hib-story-meta { font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); margin-bottom: var(--space-2) !important; }
.post-content .hib-story dl { display: grid; grid-template-columns: 140px 1fr; gap: var(--space-2) var(--space-3); margin: var(--space-3) 0; }
.post-content .hib-story dt { width: auto; margin: 0; white-space: nowrap; font-weight: var(--font-weight-regular); font-family: var(--font-mono); font-size: var(--font-size-sm); color: var(--color-text-tertiary); padding-top: 2px; }
.post-content .hib-story dd { width: auto; margin: 0; padding-inline-start: 0; font-size: var(--font-size-base); }
.post-content .hib-story dt ~ dt, .post-content .hib-story dd ~ dd { margin-top: 0; }
@media (max-width: 760px) {
  .hib-lanes { display: block; }
  .hib-lane-labels, .hib-timeaxis, .hib-back { display: none; }
  .hib-next-label { text-align: left; margin: 0 !important; }
  .hib-col { display: grid; gap: 4px; margin-bottom: var(--space-2); }
  .hib-col:not(.is-active) .hib-cell { display: none; }
  .hib-cell::before { content: attr(data-lane); display: block; font-family: var(--font-mono); font-size: var(--font-size-xs); color: var(--color-text-tertiary); margin-bottom: 2px; }
  .hib-back-label { text-align: left; margin: var(--space-1) 0 0 !important; }
  .hib-core { margin-top: var(--space-3); justify-content: flex-start; gap: var(--space-2); }
  .hib-core p { flex-basis: 100%; }
}
@media (max-width: 860px) {
}
@media (max-width: 600px) {
  .hib-skill { grid-template-columns: 1fr; }
  .hib-skill p, .hib-skill code { grid-column: 1; grid-row: auto; }
  .hib-syslinks, .hib-cards { grid-template-columns: 1fr; }
  .hib-card { flex-direction: row; }
  .hib-card-img { width: 38%; flex-shrink: 0; border-bottom: 0; border-right: 1px solid var(--color-border); }
  .hib-card-img img { height: 100%; aspect-ratio: auto; }
  .hib-card-body { padding: var(--space-2); }
  .hib-card .hib-tags { display: none; }
  .hib-row, .hib-axis, .hib-marks, .hib-mix { grid-template-columns: 1fr; gap: var(--space-1); }
  .hib-chart { --lab: 0px; }
  .hib-marks > .hib-row-label { display: none; }
  .hib-mark span { display: none; } .hib-marks-track { height: 18px; } .hib-mark-line { top: 18px; }
  .hib-axis > div:first-child { display: none; }
  .post-content .hib-story dl { grid-template-columns: 1fr; gap: 0; }
  .post-content .hib-story dd { margin-bottom: var(--space-2); }
}
@media (max-width: 600px) { .hib-tabs .full { display: none; } .hib-tabs .short { display: inline; } .hib-tabs button { padding: 7px 6px; } }
@media (prefers-reduced-motion: reduce) { .hib-orbit, .hib-wide *, .hib-wide *::before, .hib-wide *::after, .hib-aurora::before, .hib-node::after, .hib-core button::after { animation: none !important; } }
</style>
<div class="intro-info">
<p><span class="tag blue text-blue">personal data projects</span></p>
<p class="intro-description">Tiny Data Adventures take big, messy datasets (fossil records, museum catalogs, eruption reports, reef surveys) and make them accessible to everyone: easy to read for someone new to the data, and usable with a keyboard, a screen reader or without color.</p>
<div class="intro-details-wrapper">
<p class="intro-details no-margin-bottom"><span class="fi" style="background-image: url(/images/mouse.svg)"></span> Design and build, with Claude Code</p>
<p class="intro-details no-margin-bottom"><span class="fi" style="background-image: url(/images/document.svg)"></span> 4 projects, 1 in progress</p>
<p class="intro-details no-margin-bottom"><span class="fi" style="background-image: url(/images/calendar.svg)"></span> 2025 – 2026</p>
</div>
</div>
<div class="hib-wide">
{{< hib-mess >}}
</div>
<p>I'm a product designer and a data enthusiast, not a data engineer. Claude Code gets me from a dataset to a working visualization fast; my eye and judgment decide what ships. Outside these solo projects, this is how I'd bring it to a team: running prototypes people can react to instead of static mocks, and small, well-scoped changes made directly in the codebase alongside engineers.</p>
<p class="hib-callout"><strong>No Figma file, no design system up front.</strong> I designed these apps directly in code, because I wanted to see the data first. The system came out of the code afterwards, which is why so much of the work below is consistency and accessibility audits.</p>
<p class="hib-kicker">01 · The loop</p>
<h2 class="hib-h2" id="loop">Same loop, different lessons</h2>
<p>Seven steps from messy data to something anyone can explore. Claude Code is in every step; what changes is what each of us brings. Pick a step, then a project in the tabs below it.</p>
<div class="hib-wide">
<div class="hib-lanes" id="hib-ring">
<div class="hib-lane-labels" aria-hidden="true"><span></span><span></span><span class="hib-lane-label"><span class="own own--me"></span>Me</span><span class="hib-lane-label"><span class="own own--ai"></span>Claude Code</span></div>
<div class="hib-timeaxis" aria-hidden="true"><span class="hib-axis-dot"></span></div>
<div class="hib-back" aria-hidden="true"></div>
<p class="hib-back-label">↺ 05–06 send fixes back to 04</p>
<p class="hib-next-label">↺ starts the next version</p>
<div class="hib-core"><p>Underneath every step:</p><button type="button" data-node="context" aria-pressed="false">CLAUDE.md</button><button type="button" data-node="skills" aria-pressed="false">Skills</button></div>
</div>
<div class="hib-tabs" id="hib-tabs" role="tablist" aria-label="Show the step for"></div>
<div class="hib-panel" id="hib-panel" role="tabpanel" aria-live="polite"></div>
</div>
<p class="hib-kicker">02 · Context, not prompts</p>
<h2 class="hib-h2" id="skills">Memory and know-how</h2>
<p>A <strong>CLAUDE.md</strong> in each repo is its memory; <strong>skills</strong> are routines that travel between projects.</p>
<p class="hib-callout"><strong>Memory needs maintenance too.</strong> Tracing Origins' CLAUDE.md grew to about 44,000 words, full of reversals, and all of it loads every session. Treat it like code: keep it short, archive the history, delete what's superseded.</p>
<p>The three skills I distilled from these projects:</p>
<div class="hib-skills">
<div class="hib-skill"><code>visual-consistency-qa</code><p>Aligns radius, color roles, spacing and type, so they can become tokens.</p></div>
<div class="hib-skill"><code>wcag-audit-learning</code><p>"Learning" because I check every case by hand and talk each fix through before it's applied.</p></div>
<div class="hib-skill"><code>design-tokens-system</code><p>Fixes contrast and sizes in one place, and holds each project's visual identity.</p></div>
</div>
<p class="hib-sys-intro">Each project's tokens page shows what is tokenized and what isn't yet.</p>
{{< hib-syslinks >}}
<p class="hib-kicker">03 · Over time</p>
<h2 class="hib-h2" id="time">What my commits say about how I work</h2>
<p>Every commit from the four repos, one square each, placed by date. The marks are the moments my way of working changed; the band below shows what the commits were about, month by month. Before all this: a 2024–25 bootcamp, seismic-agent written with ChatGPT, and a coral project that stalled.</p>
<div class="hib-wide">
<div class="hib-legend" id="hib-legend" role="group" aria-label="Filter by phase"></div>
<div class="hib-chart" id="hib-chart">
<div class="hib-marks" id="hib-marks"><div class="hib-row-label">What changed</div><div class="hib-marks-track" role="list" aria-label="Moments the way of working changed"></div></div>
<div class="hib-rows" id="hib-rows"></div>
<div class="hib-mix" id="hib-mix"><div class="hib-row-label">What the commits<br>were about</div><div class="hib-mix-track" aria-hidden="true"></div></div>
<div class="hib-axis"><div></div><div id="hib-axis"></div></div>
</div>
<p class="hib-readout" id="hib-readout" aria-live="polite"><i class="hib-readout-dot" aria-hidden="true"></i><span>Hover a square or a mark to read it.</span></p>
<div class="hib-datanote"><span class="hib-note-label">About this data</span><p><span id="hib-source"></span> Phases are tagged automatically from commit messages, so a few may be off.</p></div>
</div>
<p class="hib-kicker">04 · The projects</p>
<h2 class="hib-h2" id="projects">What each one taught me</h2>
<p>Same loop, a different kind of mess each time. Pick a project to read its story.</p>
<div class="hib-wide">
<div class="hib-cards" id="hib-cards"></div>
<div class="hib-story" id="hib-story" aria-live="polite"></div>
</div>
<p class="hib-kicker">05 · Takeaways</p>
<h2 class="hib-h2">What I've learned working this way</h2>
<div class="hib-wide hib-wide--plain">
<ol class="hib-takeaways">
<li><span class="hib-tk-n" aria-hidden="true">01</span><h3>Context over prompts</h3><p>I talk to Claude like a coworker. The CLAUDE.md and the skills carry the precision.</p></li>
<li><span class="hib-tk-n" aria-hidden="true">02</span><h3>Verify everything</h3><p>Audits, data and every "it's fixed" get checked in the browser before I believe them.</p></li>
<li><span class="hib-tk-n" aria-hidden="true">03</span><h3>Learn the fixes</h3><p>I run the tests myself, so I understand each fix instead of just collecting it.</p></li>
</ol>
</div>
{{< hib-evidence >}}
{{< hib-data >}}
<script>
(function () {
  /* all content comes from data/how_i_build.yaml (see the hib-data shortcode) */
  var D = JSON.parse(document.getElementById("hib-data").textContent);
  var ORDER = D.projects.map(function (p) { return p.id; });
  var PROJECTS = {}, STORIES = {}, CARDS = {}, REPOS = {}, EVID = {};
  D.projects.forEach(function (p) {
    EVID[p.id] = p.evidence || {};
    PROJECTS[p.id] = { name: p.name, short: p.short, emoji: p.emoji, url: p.url, repo: p.repo, meta: p.meta, status: p.status, next: p.next || [] };
    STORIES[p.id] = (p.story || []).map(function (r) { return [r.label, r.text]; });
    CARDS[p.id] = p.card; REPOS[p.id] = p.github;
  });
  var NODES = D.steps.map(function (st) {
    var nd = {}; for (var key in st) nd[key] = st[key];
    nd.n = st.num; /* "n" alone is a boolean in YAML, so the data file uses "num" */
    nd.p = {}; D.projects.forEach(function (p) { nd.p[p.id] = (p.steps || {})[st.id] || ""; });
    return nd;
  });
  var PHASES = [["data", "Data & research", "var(--color-blue)"], ["ui", "UI & features", "var(--color-orange)"], ["tokens", "Tokens", "var(--color-pink)"], ["a11y", "Accessibility", "var(--color-green)"], ["docs", "Docs & ship", "var(--color-grey)"]];
  var state = { project: "all", tab: "all", node: "question", phases: { data: 1, ui: 1, tokens: 1, a11y: 1, docs: 1 } };
  var ring = document.getElementById("hib-ring"), panel = document.getElementById("hib-panel");
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  /* ring nodes */
  NODES.slice(0, 7).forEach(function (nd, i) {
    var col = document.createElement("div");
    col.className = "hib-col"; col.dataset.node = nd.id; col.style.gridColumn = String(i + 2);
    col.innerHTML = '<button type="button" class="hib-node" data-node="' + nd.id + '" aria-pressed="false"><span class="n">' + nd.n + '</span><span class="l">' + nd.label + '</span></button>' +
      '<div class="hib-cell hib-cell--me" data-lane="Me">' + esc(nd.me) + '</div>' +
      '<div class="hib-cell hib-cell--ai" data-lane="Claude Code">' + esc(nd.ai) + '</div>';
    ring.insertBefore(col, ring.querySelector(".hib-back"));
  });
  ring.addEventListener("click", function (e) { var b = e.target.closest("[data-node]"); if (b) { state.node = b.dataset.node; render(); } });
  function renderPanel() {
    var nd = NODES.filter(function (x) { return x.id === state.node; })[0], html = '<div><p class="hib-step">' + (nd.n === "CORE" ? "Underneath every step" : "Step " + nd.n + " · " + nd.label) + '</p><h3>' + esc(nd.title) + '</h3><p>' + esc(nd.text) + '</p></div>';
    if (state.tab === "all") {
      html += '<div class="hib-note"><span class="hib-note-label">In each project</span>' + ORDER.map(function (k, i) { return '<div class="hib-note-row' + nextCls(k) + '" style="--i:' + i + '"><span class="hib-note-proj">' + PROJECTS[k].emoji + ' ' + PROJECTS[k].name + '</span>' + stepBody(k, nd) + '</div>'; }).join("") + '</div>';
    } else {
      var P = PROJECTS[state.tab];
      html += '<div class="hib-note"><span class="hib-note-label">In ' + P.emoji + ' ' + P.name + '</span><div class="hib-note-row' + nextCls(state.tab) + '">' + stepBody(state.tab, nd) + '</div></div>';
    }
    panel.innerHTML = html;
  }
  function isNext(k) { return PROJECTS[k].next.indexOf(state.node) > -1; }
  function nextCls(k) { return isNext(k) ? " is-next" : ""; }
  // a project's evidence for this step (hib-evidence.html) replaces its text; the text stays behind "The story"
  function stepBody(k, nd) {
    var ev = (EVID[k] || {})[nd.id];
    if (!isNext(k) && window.HIB_EV && HIB_EV.has(ev)) return HIB_EV.render(ev, nd.p[k]);
    return '<p>' + stepText(k, nd) + '</p>';
  }
  function stepText(k, nd) { return (isNext(k) ? '<span class="hib-next">Next</span>' : "") + esc(nd.p[k]); }
  /* commit chart */
  var rows = document.getElementById("hib-rows"), legend = document.getElementById("hib-legend"), readout = document.getElementById("hib-readout"), axis = document.getElementById("hib-axis"), color = {};
  PHASES.forEach(function (ph) {
    color[ph[0]] = ph[2];
    var b = document.createElement("button"); b.type = "button"; b.dataset.phase = ph[0]; b.setAttribute("aria-pressed", "true");
    b.innerHTML = '<i style="background:' + ph[2] + '"></i>' + ph[1]; legend.appendChild(b);
  });
  legend.addEventListener("click", function (e) { var b = e.target.closest("[data-phase]"); if (!b) return; var k = b.dataset.phase; state.phases[k] = state.phases[k] ? 0 : 1; b.setAttribute("aria-pressed", state.phases[k] ? "true" : "false"); paintDots(); });
  var labelOf = {}; PHASES.forEach(function (p) { labelOf[p[0]] = p[1]; });
  function drawChart(data) {
    var all = [].concat.apply([], ORDER.map(function (k) { return data[k] || []; })).map(function (c) { return Date.parse(c[0]); });
    var day = 864e5, from = D.chart_from ? Date.parse(D.chart_from) : -Infinity, t0 = Math.max(Math.min.apply(null, all), from) - 7 * day, t1 = Math.max(Date.now(), Math.max.apply(null, all)) + 7 * day, span = t1 - t0;
    for (var m = new Date(t0); m.getTime() < t1; m.setMonth(m.getMonth() + 1)) {
      var tick = new Date(m.getFullYear(), m.getMonth() + 1, 1); if (tick.getTime() >= t1) break;
      var s = document.createElement("span"); s.style.left = ((tick - t0) / span * 100) + "%";
      s.textContent = tick.toLocaleString("en", { month: "short" }) + (tick.getMonth() === 0 ? " " + tick.getFullYear() : ""); axis.appendChild(s);
    }
    ORDER.forEach(function (k) {
      var full = data[k] || [], list = full.filter(function (c) { return Date.parse(c[0]) >= from; }), before = full.length - list.length, perDay = {}, max = 0;
      list.forEach(function (c) { perDay[c[0]] = (perDay[c[0]] || 0) + 1; if (perDay[c[0]] > max) max = perDay[c[0]]; });
      var row = document.createElement("div"); row.className = "hib-row"; row.dataset.project = k;
      row.innerHTML = '<div class="hib-row-label">' + PROJECTS[k].emoji + ' ' + PROJECTS[k].name + '<small>' + full.length + ' commits</small>' + (before ? '<small>+' + before + ' before ' + new Date(from).toLocaleString("en", { month: "short" }) + '</small>' : '') + '</div><div class="hib-track" style="height:' + (max * 7 + 4) + 'px"></div>';
      var track = row.lastChild, seen = {};
      list.forEach(function (c) {
        var i = seen[c[0]] = (seen[c[0]] || 0) + 1, d = document.createElement("span");
        d.className = "hib-dot"; d.dataset.phase = c[1]; d.style.background = color[c[1]];
        d.style.left = "calc(" + ((Date.parse(c[0]) - t0) / span * 100) + "% - 3px)"; d.style.bottom = ((i - 1) * 7 + 2) + "px";
        d.dataset.info = c[0] + " · " + labelOf[c[1]] + " · " + c[2];
        track.appendChild(d);
      });
      track.addEventListener("mouseover", function (e) {
        var d = e.target; if (!d.dataset.info) return;
        document.querySelectorAll("#hib-chart .is-current").forEach(function (x) { x.classList.remove("is-current"); });
        d.classList.add("is-current");
        readout.classList.add("has-commit");
        readout.querySelector(".hib-readout-dot").style.background = d.style.background;
        readout.querySelector("span").textContent = PROJECTS[k].emoji + " " + d.dataset.info;
      });
      rows.appendChild(row);
    });
    /* milestone marks: a diamond with a short label, and a dashed line down through the rows */
    var chart = document.getElementById("hib-chart"), mt = chart.querySelector(".hib-marks-track");
    var xOf = function (t) { return (t - t0) / span; };
    var lineAt = function (f) { return "calc(var(--lab) + var(--space-3) + (100% - var(--lab) - var(--space-3)) * " + f.toFixed(4) + ")"; };
    (D.milestones || []).forEach(function (m, i) {
      var f = xOf(Date.parse(m.date)), b = document.createElement("button"), line = document.createElement("i");
      b.type = "button"; b.className = "hib-mark"; b.setAttribute("role", "listitem");
      b.style.left = (f * 100) + "%"; b.innerHTML = "<span>" + esc(m.label) + "</span>";
      b.setAttribute("aria-label", new Date(m.date).toLocaleString("en", { month: "short", year: "numeric" }) + ": " + m.label + ". " + m.text);
      line.className = "hib-mark-line"; line.style.left = lineAt(f); chart.appendChild(line);
      var show = function () {
        chart.querySelectorAll(".is-current").forEach(function (x) { x.classList.remove("is-current"); });
        b.classList.add("is-current"); line.classList.add("is-current");
        readout.classList.remove("has-commit"); readout.querySelector(".hib-readout-dot").style.background = "";
        readout.querySelector("span").textContent = new Date(m.date).toLocaleString("en", { month: "short", year: "numeric" }) + " · " + m.label + ". " + m.text;
      };
      b.addEventListener("mouseenter", show); b.addEventListener("focus", show);
      mt.appendChild(b);
    });
    // labels: open to the left near the right edge, then take the lowest of three levels that doesn't overlap
    function placeMarks() {
      var placed = [[], [], []], W = mt.clientWidth;
      mt.querySelectorAll(".hib-mark").forEach(function (b) {
        var lab = b.querySelector("span"), w = lab.offsetWidth, x = b.offsetLeft + 4, left = x + w > W;
        b.classList.toggle("is-left", left);
        var a0 = left ? x - w : x, a1 = left ? x : x + w, lv = 0;
        while (lv < 2 && placed[lv].some(function (r) { return a0 < r[1] + 12 && r[0] < a1 + 12; })) lv++;
        placed[lv].push([a0, a1]); b.style.setProperty("--lv", lv);
      });
    }
    placeMarks(); window.addEventListener("resize", placeMarks);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(placeMarks);
    /* monthly mix: one column per month, stacked by phase share */
    var mix = chart.querySelector(".hib-mix-track"), months = {};
    ORDER.forEach(function (k) { (data[k] || []).forEach(function (c) { var t = Date.parse(c[0]); if (t < from) return; var key = c[0].slice(0, 7); (months[key] = months[key] || { n: 0 })[c[1]] = (months[key][c[1]] || 0) + 1; months[key].n++; }); });
    Object.keys(months).forEach(function (key) {
      var a0 = Math.max(Date.parse(key + "-01"), t0), d1 = new Date(key + "-01"); d1.setMonth(d1.getMonth() + 1);
      var a1 = Math.min(d1.getTime(), t1), col = document.createElement("div"), M = months[key];
      col.className = "hib-mix-col"; col.style.left = (xOf(a0) * 100) + "%"; col.style.width = ((a1 - a0) / span * 100) + "%";
      col.title = new Date(key + "-01").toLocaleString("en", { month: "long" }) + ": " + M.n + " commits";
      PHASES.forEach(function (ph) { if (!M[ph[0]]) return; var sp = document.createElement("span"); sp.dataset.phase = ph[0]; sp.style.background = ph[2]; sp.style.height = (M[ph[0]] / M.n * 100) + "%"; col.appendChild(sp); });
      mix.appendChild(col);
    });
    var note = document.querySelector(".hib-datanote");
    if (note && !note.dataset.filled) { note.dataset.filled = 1; ORDER.forEach(function (k) { var t = D.projects[ORDER.indexOf(k)].chart_note; if (t) { var q = document.createElement("p"); q.textContent = PROJECTS[k].emoji + " " + PROJECTS[k].name + ": " + t; note.appendChild(q); } }); }
    paintDots();
  }
  function paintDots() { document.querySelectorAll("#hib-rows .hib-dot, #hib-mix span[data-phase]").forEach(function (d) { d.classList.toggle("is-off", !state.phases[d.dataset.phase]); }); }
  function dimRows() { rows.querySelectorAll(".hib-row").forEach(function (r) { r.classList.toggle("is-dim", state.project !== "all" && r.dataset.project !== state.project); }); }
  /* commits: live from GitHub (cached 1h per visitor), snapshot JSON as fallback */
  var RULES = [["a11y", /a11y|accessib|wcag|contrast|keyboard|focus|wave\b|axe\b|lighthouse|aria|reflow|screen reader|color blind|without colou?r|reduced.motion|teclado|foco|sr-only|landmark|skip link|zoom/i], ["tokens", /token|styleguide|design system|type scale|spacing scale|escala|radii/i], ["data", /data|dataset|pipeline|fetch|scraper|geocod|geograph|\bapi\b|louvre|\bmet\b|\bbm\b|quai|piezas|pbdb|fossil|volcanoes|eruption|csv|json|translat|traduc|layer [123]|investig|batch|ronda|research|wikidata|tavily|provenance|hallazgo/i], ["docs", /readme|seo|metadata|screenshot|image|\bog\b|analytics|docs|credits|cr[eé]dit/i]];
  function phaseOf(msg) { for (var i = 0; i < RULES.length; i++) if (RULES[i][1].test(msg)) return RULES[i][0]; return "ui"; }
  function repoCommits(repo) {
    function page(n, acc) {
      return fetch("https://api.github.com/repos/veronicadeleonh/" + repo + "/commits?per_page=100&page=" + n).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (list) {
        acc = acc.concat(list); return list.length === 100 && n < 10 ? page(n + 1, acc) : acc;
      });
    }
    return page(1, []).then(function (list) {
      return list.reverse().map(function (c) { var msg = (c.commit.message || "").split("\n")[0]; return [c.commit.author.date.slice(0, 10), phaseOf(msg), msg.slice(0, 140)]; });
    });
  }
  var CACHE = "hib-commits-" + ORDER.join("-"), source = document.getElementById("hib-source");
  function fromCache() { try { var c = JSON.parse(localStorage.getItem(CACHE)); if (c && Date.now() - c.t < 36e5) return c.data; } catch (e) {} return null; }
  function live() {
    var keys = Object.keys(REPOS);
    return Promise.all(keys.map(function (k) { return repoCommits(REPOS[k]); })).then(function (lists) {
      var data = {}; keys.forEach(function (k, i) { data[k] = lists[i]; });
      try { localStorage.setItem(CACHE, JSON.stringify({ t: Date.now(), data: data })); } catch (e) {}
      return data;
    });
  }
  var cached = fromCache();
  (cached ? Promise.resolve(cached) : live()).then(function (data) { if (source) source.textContent = "Live from GitHub."; drawChart(data); }).catch(function () {
    fetch("/data/how-i-build-commits.json").then(function (r) { return r.json(); }).then(function (data) { if (source) source.textContent = "Snapshot of the repos (GitHub was unreachable)."; drawChart(data); }).catch(function () { readout.querySelector("span").textContent = "Commit data couldn't load."; });
  });
  /* stories */
  var story = document.getElementById("hib-story");
  var cardsEl = document.getElementById("hib-cards");
  cardsEl.style.setProperty("--hib-n", ORDER.length);
  ORDER.forEach(function (k) {
    var P = PROJECTS[k], C = CARDS[k], b = document.createElement("button");
    b.type = "button"; b.className = "hib-card"; b.dataset.project = k; b.setAttribute("aria-pressed", "false");
    b.innerHTML = '<span class="hib-card-bar" aria-hidden="true"></span><span class="hib-card-img">' + (P.status ? '<span class="hib-status">' + esc(P.status) + '</span>' : '') + '<img src="' + C.img + '" alt="" loading="lazy"></span><span class="hib-card-body"><span class="hib-card-name">' + P.emoji + ' ' + P.name + '</span><span class="hib-card-lesson">' + esc(C.lesson) + '</span>' + (C.mess ? '<span class="hib-flow"><span class="hib-flow-row"><span class="hib-flow-k">The mess</span>' + esc(C.mess) + '</span><span class="hib-flow-row is-to"><span class="hib-flow-k">Made accessible</span>' + esc(C.access) + '</span></span>' : '') + '<span class="hib-tags">' + C.tags.map(function (t) { return '<span>' + t + '</span>'; }).join("") + '</span></span>';
    cardsEl.appendChild(b);
  });
  cardsEl.addEventListener("click", function (e) { var b = e.target.closest("[data-project]"); if (b) { state.project = state.project === b.dataset.project ? "all" : b.dataset.project; render(); } });
  function renderStory() {
    cardsEl.classList.toggle("has-active", state.project !== "all");
    cardsEl.querySelectorAll(".hib-card").forEach(function (c) { var on = c.dataset.project === state.project; c.classList.toggle("is-active", on); c.setAttribute("aria-pressed", on ? "true" : "false"); });
    if (state.project === "all") { story.innerHTML = ""; story.hidden = true; return; }
    var P = PROJECTS[state.project]; story.hidden = false;
    story.innerHTML = '<div class="hib-story-head"><span class="hib-note-label">What it taught me</span><h3>' + P.emoji + ' ' + P.name + '</h3><p class="hib-story-meta">' + P.meta + ' · ' + (P.url ? '<a href="' + P.url + '" target="_blank" rel="noopener">Live</a>' : 'Not live yet') + ' · <a href="' + P.repo + '" target="_blank" rel="noopener">Code</a></p></div><dl>' + STORIES[state.project].filter(function (r) { return r[0] !== "Practiced"; }).map(function (r) { return '<dt>' + r[0] + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join("") + '</dl>';
  }
  /* project tabs under the loop (WAI-ARIA tabs: arrows move, Home/End jump) */
  var tabs = document.getElementById("hib-tabs");
  ["all"].concat(ORDER).forEach(function (k) {
    var b = document.createElement("button"); b.type = "button"; b.setAttribute("role", "tab"); b.dataset.tab = k; b.id = "hib-tab-" + k;
    b.innerHTML = k === "all" ? "All" : PROJECTS[k].emoji + ' <span class="full">' + PROJECTS[k].name + '</span><span class="short">' + (PROJECTS[k].short || PROJECTS[k].name) + "</span>";
    tabs.appendChild(b);
  });
  tabs.addEventListener("click", function (e) { var b = e.target.closest("[data-tab]"); if (b) { state.tab = b.dataset.tab; render(); } });
  tabs.addEventListener("keydown", function (e) {
    var list = [].slice.call(tabs.querySelectorAll("[role=tab]")), i = list.indexOf(document.activeElement), n = list.length, to = null;
    if (e.key === "ArrowRight") to = (i + 1) % n; else if (e.key === "ArrowLeft") to = (i - 1 + n) % n; else if (e.key === "Home") to = 0; else if (e.key === "End") to = n - 1;
    if (to === null || i < 0) return; e.preventDefault(); state.tab = list[to].dataset.tab; render(); list[to].focus();
  });
  function render() {
    tabs.querySelectorAll("[role=tab]").forEach(function (b) { var on = b.dataset.tab === state.tab; b.setAttribute("aria-selected", on ? "true" : "false"); b.tabIndex = on ? 0 : -1; });
    panel.setAttribute("aria-labelledby", "hib-tab-" + state.tab);
    document.querySelectorAll("#hib-ring button[data-node]").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.node === state.node ? "true" : "false"); });
    document.querySelectorAll("#hib-ring .hib-col").forEach(function (c) { c.classList.toggle("is-active", c.dataset.node === state.node); });
    renderPanel(); renderStory();
  }
  /* spotlight: tag hoverable elements and track the cursor inside them */
  document.querySelectorAll(".hib-node, .hib-cell, .hib-core button, .hib-legend button, .hib-skill, .hib-syslinks a, .hib-card").forEach(function (el) { el.classList.add("hib-spot"); });
  document.addEventListener("pointermove", function (e) {
    var el = e.target.closest && e.target.closest(".hib-spot"); if (!el) return;
    var r = el.getBoundingClientRect(); el.style.setProperty("--x", (e.clientX - r.left) + "px"); el.style.setProperty("--y", (e.clientY - r.top) + "px");
  }, { passive: true });
  render();
})();
</script>
