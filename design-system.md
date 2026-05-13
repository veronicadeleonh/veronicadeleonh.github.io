# Design System — veronicadeleonh.github.io

Source: `assets/css/extended/custom.css`

---

## Layout

| Token | Value |
|-------|-------|
| `--main-width` | 620px |
| `--post-width` | 620px |
| `--radius` | 0px (no border-radius) |

---

## Colors

### Base

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-bg` | `#ffffff` | Page background |
| `--color-text` | `#000000` | Primary text |
| `--color-surface` | `#f1f4f5` | Cards, hover backgrounds, borders |
| `--color-surface-hover` | `#e2e6e7` | Hover state of surface |
| `--color-surface-active` | `#d1d5d6` | Active/pressed state of surface |
| `--color-border` | `#e7eaeb` | Subtle borders |
| `--color-text-secondary` | `#777e7f` | Secondary text, captions |
| `--color-text-tertiary` | `#9b9fa0` | Tertiary text, nav, footer |

### Semantic

| Token | Hex (solid) | Background hex | Background opacity | Usage |
|-------|-------------|----------------|--------------------|-------|
| `--color-green` | `#6ab04c` | `--color-green-bg` `#bbdc58` | 17.6% (0x2d) | e-commerce tag |
| `--color-orange` | `#f0932b` | `--color-orange-bg` `#ffbf76` | 17.6% (0x2d) | SaaS tag |
| `--color-blue` | `#4834d4` | `--color-blue-bg` `#686ce0` | 17.6% (0x2d) | e-learning tag |
| `--color-purple` | `#964df6` | `--color-purple-bg` `#964df6` | 14.9% (0x26) | Available, unused in content |
| `--color-yellow` | `#f9ca24` | `--color-yellow-bg` `#f6e58d` | 25.1% (0x40) | Box notes, dot |

> **8-digit hex format** (CSS Color Level 4 RRGGBBAA): last two digits are alpha in hex.
> `2d` = 45/255 = 17.6% · `26` = 38/255 = 14.9% · `40` = 64/255 = 25.1%

---

## Typography

### Fonts

| Token | Value | Stack |
|-------|-------|-------|
| `--font-sans` | IBM Plex Sans | `"IBM Plex Sans", sans-serif` |
| `--font-mono` | IBM Plex Mono | `"IBM Plex Mono", monospace` |

Body default: `font-family: var(--font-sans)`, `font-weight: 300 (light)`

### Scale

| Token | px | Usage |
|-------|----|-------|
| `--font-size-hero` | 28px | Hero headings, first entry description |
| `--font-size-lg` | 20px | h2, intro description |
| `--font-size-md` | 16px | Body medium, nav, headings, card text |
| `--font-size-base` | 15px | Body base, paragraphs, lists |
| `--font-size-tag` | 14px | Tags, labels, dots, toc, button text |
| `--font-size-sm` | 13px | Small text, photo footnotes, ds-token |
| `--font-size-xs` | 12px | Footer, top-link |

### Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--font-weight-light` | 300 | Body text, nav links |
| `--font-weight-regular` | 400 | Mono elements, buttons |
| `--font-weight-medium` | 500 | Headings h1–h5, links, card titles |
| `--font-weight-bold` | 700 | Number badges |

---

## Spacing

| Token | px | Visual |
|-------|----|--------|
| `--space-1` | 4px | Tight padding (label-grey) |
| `--space-2` | 8px | Gap between inline elements, dots |
| `--space-3` | 16px | Post entry padding, section gaps |
| `--space-4` | 24px | Number badge size, box-note margin |
| `--space-5` | 32px | Large section margins |

---

## Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `--transition-fast` | 150ms | Hover on buttons, icons, label-grey |
| `--transition-base` | 300ms | Card hover, image scale, post entry |
| `--transition-slow` | 0.6s | Fade image slider (opacity) |

All transitions use `ease` or the default timing function unless specified.

---

## Components

### Tag

Used to label project category at the top of case study pages.

```html
<span class="tag green text-green">e-commerce</span>
<span class="tag orange text-orange">SaaS</span>
<span class="tag blue text-blue">e-learning</span>
```

| Property | Value |
|----------|-------|
| `font-size` | 14px (`--font-size-tag`) |
| `font-weight` | 500 (`--font-weight-medium`) |
| `display` | inline |
| `padding` | 0.5% 1.5% |
| `border-radius` | 0px |

| Variant | Background | Text color |
|---------|-----------|------------|
| green | `#bbdc58` at 17.6% | `#6ab04c` |
| orange | `#ffbf76` at 17.6% | `#f0932b` |
| blue | `#686ce0` at 17.6% | `#4834d4` |

---

### Label grey

Used on project cards on the homepage to display project type.

```html
<span class="label-grey">Label grey</span>
```

| Property | Value |
|----------|-------|
| `font-size` | 14px (`--font-size-tag`) |
| `color` | `#777e7f` (`--color-text-secondary`) |
| `background-color` | `#f1f4f5` (`--color-surface`) |
| `padding` | 4px 8px (`--space-1` `--space-2`) |
| `width` | fit-content |
| `border-radius` | 0px |
| `transition` | all 150ms (`--transition-fast`) |
| hover `background-color` | `#e2e6e7` (`--color-surface-hover`) |

---

### Dot

Used inline with text to indicate status or availability.

```html
<div class="dot yellow-dot"></div>
<div class="dot gray-dot"></div>
```

| Property | Value |
|----------|-------|
| `width` / `height` | 8px (`--space-2`) |
| `border-radius` | 50% (circle) |

| Variant | Color |
|---------|-------|
| `yellow-dot` | `#f9ca24` (`--color-yellow`) |
| `gray-dot` | `#e2e6e7` (`--color-surface-hover`) |

Container: `display: flex; gap: 8px; align-items: center`

---

### Numbering

Used in case studies for step-by-step lists.

```html
<div class="numbering">
  <div class="numbers">1</div>
  <span class="numbers-label">Label text</span>
</div>
```

**.numbers** (badge)

| Property | Value |
|----------|-------|
| `width` / `height` | 24px (`--space-4`) |
| `background-color` | `#000000` (`--color-text`) |
| `color` | `#ffffff` (`--color-bg`) |
| `border-radius` | 50% (circle) |
| `font-size` | 14px (`--font-size-tag`) |
| `font-weight` | 700 (`--font-weight-bold`) |
| `display` | flex, centered |

**.numbers-label**

| Property | Value |
|----------|-------|
| `font-size` | 16px (`--font-size-md`) |
| `width` | 95% |

**.numbering** (row)

| Property | Value |
|----------|-------|
| `display` | flex |
| `gap` | 8px (`--space-2`) |
| `align-items` | center |
| `padding-bottom` | 8px (`--space-2`) |

---

### Box note

Used in case studies to highlight key metrics and research findings.

```html
<div class="box-notes yellow-background yellow-border">
  Content here
</div>
```

| Property | Value |
|----------|-------|
| `border` | 1px solid `#f9ca24` (`--color-yellow`) |
| `background-color` | `#f6e58d` at 25.1% (`--color-yellow-bg`) |
| `padding` | 3% |
| `font-size` | 16px (`--font-size-md`) |
| `border-radius` | 0px |

---

### Icons — UI (`class="fi"`)

Inline icons used with text inside project intro and about sections.

```html
<span class="fi" style="background-image: url(/images/mouse.svg)"></span>
```

| Property | Value |
|----------|-------|
| `display` | inline-block |
| `width` / `height` | 1em (scales with font-size) |
| `line-height` | 1em |
| `vertical-align` | middle |
| `background-size` | contain |
| `background-position` | 50% |
| `background-repeat` | no-repeat |

| File | Usage |
|------|-------|
| `mouse.svg` | Role / position (all project intros) |
| `calendar.svg` | Date / period (all project intros) |
| `location.svg` | Location (eyeem, basecase) |
| `globe.svg` | Remote / worldwide (mondly, eyeem) |
| `ext-link.svg` | External links |
| `arrow-right.svg` | Navigation CTA buttons |
| `arrow-bottom.svg` | Scroll / download (available, unused) |

All icons: 24×24px viewBox, `fill="black"`, stored in `/static/images/`.

---

### Icons — Social (`class="fip"`)

Used inside `.btn-connect.circled` buttons on home and about pages.

```html
<a class="btn-connect circled" href="...">
  <span class="fip" style="background-image: url(/images/linkedin.svg)"></span>
</a>
```

| Property | Value |
|----------|-------|
| `display` | inline-block |
| `width` / `height` | 20px |
| `line-height` | 1em |
| `vertical-align` | middle |
| `background-size` | contain |
| `background-repeat` | no-repeat |
| `background-position` | center |

| File | Usage |
|------|-------|
| `linkedin.svg` | LinkedIn profile link |
| `github.svg` | GitHub profile link |
| `instagram.svg` | Instagram profile link |
| `readcv.svg` | Read.cv profile link |

---

### Button — Circled (`btn-connect circled`)

Icon-only circular button for social links.

```html
<a class="btn-connect circled" href="...">
  <span class="fip" style="background-image: url(...)"></span>
</a>
```

| Property | Value |
|----------|-------|
| `display` | flex |
| `align-items` | center |
| `justify-content` | center |
| `width` / `height` | 45px |
| `border-radius` | 300px (pill/circle) |
| `transition` | all 150ms (`--transition-fast`) |
| hover `background-color` | `#f1f4f5` (`--color-surface`) |

---

### Button — Rounded (`btn-connect rounded`)

Text button with optional trailing icon, used for CTAs.

```html
<a class="btn-connect rounded arrow" href="...">
  Read more <span class="fi" style="background-image: url(/images/arrow-right.svg)"></span>
</a>
```

| Property | Value |
|----------|-------|
| `display` | flex |
| `align-items` | center |
| `gap` | 8px (`--space-2`) |
| `padding` | 1% 2% |
| `border-radius` | 0px (overrides btn-connect's 300px via `--radius`) |
| `font-size` | 15px (`--font-size-base`) |
| `font-weight` | 400 (`--font-weight-regular`) |
| `line-height` | 35px |
| `transition` | all 150ms (`--transition-fast`) |
| hover `background-color` | `#f1f4f5` (`--color-surface`) |
| hover arrow | `translateX(4px)` |

---

### Intro details

Mono-style metadata row used in project case study headers.

```html
<p class="intro-details no-margin-bottom">
  <span class="fi" style="background-image: url(/images/mouse.svg)"></span>
  Senior Product Designer
</p>
```

| Property | Value |
|----------|-------|
| `font-family` | IBM Plex Mono (`--font-mono`) |
| `font-weight` | 400 (`--font-weight-regular`) |
| `font-size` | 15px (`--font-size-base`) |

---

## Utility classes

| Class | Effect |
|-------|--------|
| `flex-wrap` | `display: flex; flex-wrap: wrap; gap: 8px` |
| `flex-column` | `display: flex; flex-direction: column` |
| `gap-8` | `gap: 8px` |
| `gap-16` | `gap: 16px` |
| `no-margin-bottom` | `margin-bottom: 0 !important` |
| `photo-footnote` | Right-aligned caption, 13px, margin-top: -16px |
