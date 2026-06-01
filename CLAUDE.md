# CLAUDE.md — veronicadeleonh.github.io

Instructions for future Claude Code sessions working on this repo and its Figma design system.

---

## Project context

Personal portfolio site built with Hugo + PaperModX theme.
Live at: https://veronicadeleonh.github.io/
Design system page: https://veronicadeleonh.github.io/design/

**Figma file:** `ZNyqSJLxwUHDS0spShGHqj`
**Figma page node:** `4350:4965`

---

## Design system reference

`design-system.md` at the root of this repo is the **source of truth** for all tokens and components. Always read it before making changes to the Figma plugin or when adding new components.

It documents:
- All color tokens with exact hex values and opacity
- Typography (font families, scale, weights)
- Spacing tokens
- Transition tokens
- Every component with exact CSS property values

The CSS source is `assets/css/extended/custom.css`.

---

## Figma approach

We use a **local Figma plugin** — not the MCP Figma server, not the REST API.

**Reason:** the account is on the Figma Starter plan, which does not support the Dev Mode or Variables API endpoints required by MCP. The local plugin has full access to the `figma.*` scripting API with no plan restrictions.

**Plugin location:** `~/figma-design-system-plugin/`

The plugin is run manually inside Figma via Plugins → Development → your plugin name.

---

## Rules for plugin code generation

When writing or updating the Figma plugin (`code.js`), follow these rules strictly:

1. **Must finish in under 30 seconds.** Figma plugins time out on long-running operations. Keep node creation loops tight and synchronous.
2. **Must log `'done'` when complete.** Always end with `figma.ui.postMessage({ type: 'done' })` or `console.log('done')` so it's clear the plugin finished successfully.
3. **Must clear the canvas before rebuilding.** At the start of every run, remove all existing nodes on the target page to avoid duplicates: `figma.currentPage.children.forEach(n => n.remove())`.
4. **Must not use async loops that can hang.** Avoid `for...of` with `await` inside, recursive async calls, or `setTimeout` chains. Load all fonts upfront with `Promise.all` before any node creation begins.
5. **Keep font loading minimal.** Only load the exact font name + style combinations actually used. IBM Plex Sans (Light 300, Regular 400, Medium 500, Bold 700) and IBM Plex Mono (Regular 400).

---

## Goal

The Figma output should match https://veronicadeleonh.github.io/design/ as closely as possible — same sections, same visual hierarchy, same token values. The design system page is the reference; `design-system.md` is the spec.
