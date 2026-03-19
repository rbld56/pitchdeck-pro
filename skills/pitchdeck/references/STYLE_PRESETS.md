# Style Presets Reference

> **Version:** 2.0 | **Updated:** 2026-03-19
> **Target:** Fixed 16:9 slides (1920x1080px), PDF-first rendering
> **Font Sizing:** All values in `px` (no `clamp()`, no viewport units)

This file contains 15 curated visual style presets optimized for pitch decks. Each preset includes exact CSS custom properties, font pairings, signature decorative elements (CSS-only), and recommended audience/industry fit.

**Important constraints applied to all presets:**
- Slide canvas is always 1920x1080px (16:9 fixed)
- Font sizes are in `px` for deterministic PDF rendering
- No external image dependencies for signature elements
- All colors use hex values (no `oklch`, no `color-mix` for PDF compatibility)

## How to Apply a Preset

1. **Copy the preset's ENTIRE `:root` block** into your HTML `<style>` — do NOT cherry-pick variables
2. **Copy the font `@import` URL** into the `<style>` header — use BOTH Display and Body fonts
3. **Use ONLY `--color-*` variables** in your CSS — never hardcoded hex values in HTML attributes
4. **Apply the preset's signature elements** to at least the Cover and Ask slides (gradient mesh, decorative shapes, etc.)
5. **VERIFY:** The generated deck uses the preset's exact colors, fonts, and atmosphere — not generic defaults
6. **DEFAULT PRESET:** If the user doesn't choose, use **Muted Sophistication (#7)** — it works for any audience

---

## Preset Index

| # | Name | Tone | Primary Audience |
|---|------|------|------------------|
| 1 | Bold Signal | Confident, bold | VC, SaaS |
| 2 | Dark Botanical | Elegant, premium | Consumer, Premium |
| 3 | Notebook Tabs | Editorial, organized | Education, Creative |
| 4 | Swiss Modern | Clean, Bauhaus | Design, Architecture |
| 5 | Paper & Ink | Literary, editorial | Media, Publishing |
| 6 | Terminal Green | Developer, hacker | DevTools, Infrastructure |
| 7 | Muted Sophistication | Professional, restrained | VC Series A-C |
| 8 | Dark Premium | Modern, elevated | SaaS, DevTools, AI/ML |
| 9 | Cloud Dancer | Calm, mindful | Wellness, Sustainability |
| 10 | Fintech Trust | Stable, precise | Fintech, Banking |
| 11 | HealthTech Clean | Clinical, compliant | MedTech, Pharma |
| 12 | AI Frontier | Innovative, forward | AI/ML, Deep Tech |
| 13 | DACH Enterprise | Formal, institutional | EU/DACH B2B |
| 14 | Board Executive | Conservative, data-heavy | C-Level, Board |
| 15 | Startup Bold | Energetic, brand-forward | Consumer, D2C |

---

## 1. Bold Signal

**Vibe:** High-conviction energy. A founder who knows their numbers and isn't afraid to take up space.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Archivo Black | 400 (Black is the family) | Google Fonts | H1: 72px, H2: 48px, H3: 36px |
| Body | Space Grotesk | 400, 500 | Google Fonts | Body: 24px, Caption: 18px, Label: 14px |

### CSS Custom Properties

```css
:root {
  /* -- Bold Signal -- */
  --preset-name: "bold-signal";

  /* Surface */
  --color-bg: #1a1a1a;
  --color-surface: #242424;
  --color-surface-elevated: #2e2e2e;
  --color-card: #FF5722;
  --color-card-alt: #E64A19;

  /* Text */
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #B0B0B0;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #787878;

  /* Accent */
  --color-accent: #FF5722;
  --color-accent-hover: #E64A19;
  --color-accent-muted: rgba(255, 87, 34, 0.15);

  /* Border & Dividers */
  --color-border: rgba(255, 255, 255, 0.08);
  --color-divider: rgba(255, 255, 255, 0.06);

  /* Typography */
  --font-display: 'Archivo Black', sans-serif;
  --font-body: 'Space Grotesk', sans-serif;
  --font-size-h1: 72px;
  --font-size-h2: 48px;
  --font-size-h3: 36px;
  --font-size-body: 24px;
  --font-size-caption: 18px;
  --font-size-label: 14px;
  --line-height-display: 1.1;
  --line-height-body: 1.5;
  --letter-spacing-display: -0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 40px;
  --border-radius: 12px;
  --border-radius-sm: 6px;

  /* Shadows */
  --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.4);
  --shadow-elevated: 0 16px 48px rgba(0, 0, 0, 0.5);
}
```

### Signature Elements

**Colored accent card** — A full-bleed accent-colored card floated to one side of the slide, containing white text. Creates visual weight and confidence.

```css
/* Signature: Accent card panel */
.slide-accent-panel {
  position: absolute;
  right: 0;
  top: 0;
  width: 45%;
  height: 100%;
  background: var(--color-accent);
  clip-path: polygon(8% 0, 100% 0, 100% 100%, 0 100%);
}

/* Signature: Bold number highlight */
.metric-highlight {
  font-family: var(--font-display);
  font-size: 120px;
  line-height: 1;
  color: var(--color-accent);
  text-shadow: 0 0 60px rgba(255, 87, 34, 0.3);
}

/* Signature: Horizontal accent rule */
.accent-rule {
  width: 80px;
  height: 6px;
  background: var(--color-accent);
  border-radius: 3px;
  margin-bottom: 24px;
}
```

### Recommended For

- **Audience:** VC seed to Series B, angel investors, accelerator demo days
- **Industry:** SaaS, marketplace platforms, B2B software
- **When to use:** When you want to project confidence and have strong metrics to showcase
- **Avoid when:** Presenting to conservative institutions, healthcare, or government

---

## 2. Dark Botanical

**Vibe:** Luxury whispered, not shouted. Evening light through a greenhouse window.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Cormorant | 600, 700 | Google Fonts | H1: 64px, H2: 44px, H3: 32px |
| Body | IBM Plex Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Dark Botanical -- */
  --preset-name: "dark-botanical";

  /* Surface */
  --color-bg: #0f0f0f;
  --color-surface: #181818;
  --color-surface-elevated: #222222;

  /* Text */
  --color-text-primary: #F2EDE8;
  --color-text-secondary: #A89E94;
  --color-text-on-accent: #0f0f0f;
  --color-text-muted: #6B6460;

  /* Accent */
  --color-accent-gold: #D4A574;
  --color-accent-pink: #E8B4B8;
  --color-accent-sage: #8B9E7E;
  --color-accent-gold-muted: rgba(212, 165, 116, 0.12);
  --color-accent-pink-muted: rgba(232, 180, 184, 0.12);

  /* Border & Dividers */
  --color-border: rgba(212, 165, 116, 0.12);
  --color-divider: rgba(255, 255, 255, 0.05);

  /* Typography */
  --font-display: 'Cormorant', serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-size-h1: 64px;
  --font-size-h2: 44px;
  --font-size-h3: 32px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --line-height-display: 1.15;
  --line-height-body: 1.6;
  --letter-spacing-display: 0.01em;
  --font-style-display: italic; /* Cormorant shines in italic for emphasis */

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 100px;
  --content-gap: 48px;
  --border-radius: 20px;
  --border-radius-sm: 10px;

  /* Shadows */
  --shadow-card: 0 12px 40px rgba(0, 0, 0, 0.5);
  --shadow-glow-gold: 0 0 80px rgba(212, 165, 116, 0.08);
  --shadow-glow-pink: 0 0 80px rgba(232, 180, 184, 0.08);
}
```

### Signature Elements

**Soft gradient circles** — Abstract, out-of-focus gradient orbs that float in the background, evoking organic warmth without literal botanical imagery.

```css
/* Signature: Floating gradient orb (top-right) */
.gradient-orb-primary {
  position: absolute;
  top: -120px;
  right: -80px;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background: radial-gradient(
    circle at 40% 40%,
    rgba(212, 165, 116, 0.18),
    rgba(232, 180, 184, 0.08),
    transparent 70%
  );
  filter: blur(60px);
  pointer-events: none;
}

/* Signature: Secondary orb (bottom-left) */
.gradient-orb-secondary {
  position: absolute;
  bottom: -100px;
  left: -60px;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: radial-gradient(
    circle at 60% 60%,
    rgba(139, 158, 126, 0.15),
    rgba(212, 165, 116, 0.06),
    transparent 70%
  );
  filter: blur(50px);
  pointer-events: none;
}

/* Signature: Thin gold separator */
.gold-separator {
  width: 60px;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--color-accent-gold),
    transparent
  );
  margin: 32px 0;
}
```

### Recommended For

- **Audience:** Consumer brand investors, luxury market, premium product launches
- **Industry:** Beauty, fashion, wellness, premium F&B, lifestyle brands
- **When to use:** When the brand identity is aspirational, elegant, or sensory
- **Avoid when:** B2B enterprise, developer tools, financial compliance

---

## 3. Notebook Tabs

**Vibe:** A well-curated Moleskine. Information feels hand-organized, intentional, and approachable.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Bodoni Moda | 700, 800 | Google Fonts | H1: 60px, H2: 42px, H3: 30px |
| Body | DM Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Notebook Tabs -- */
  --preset-name: "notebook-tabs";

  /* Surface */
  --color-bg: #2d2d2d;
  --color-surface: #f8f6f1;
  --color-surface-elevated: #FFFFFF;
  --color-page: #f8f6f1;

  /* Text */
  --color-text-primary: #2d2d2d;
  --color-text-secondary: #5c5c5c;
  --color-text-on-dark: #f8f6f1;
  --color-text-muted: #8a8a8a;

  /* Tabs — a palette of distinct tab colors */
  --color-tab-red: #E74C3C;
  --color-tab-blue: #3498DB;
  --color-tab-green: #27AE60;
  --color-tab-yellow: #F1C40F;
  --color-tab-purple: #9B59B6;
  --color-tab-orange: #E67E22;

  /* Border & Dividers */
  --color-border: #D5D0C8;
  --color-divider: #E8E4DC;
  --color-rule: #C4BFB5;

  /* Typography */
  --font-display: 'Bodoni Moda', serif;
  --font-body: 'DM Sans', sans-serif;
  --font-size-h1: 60px;
  --font-size-h2: 42px;
  --font-size-h3: 30px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --line-height-display: 1.15;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.01em;
  --letter-spacing-label: 0.08em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 36px;
  --border-radius: 8px;
  --border-radius-sm: 4px;
  --tab-height: 48px;
  --tab-width: 160px;

  /* Shadows */
  --shadow-page: 0 2px 12px rgba(0, 0, 0, 0.08);
  --shadow-tab: 0 -2px 8px rgba(0, 0, 0, 0.06);
}
```

### Signature Elements

**Colored section tabs** — Protruding tab elements at the top or side of content blocks that categorize information like dividers in a physical notebook.

```css
/* Signature: Tab element */
.section-tab {
  display: inline-block;
  padding: 8px 24px;
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: var(--letter-spacing-label);
  color: #FFFFFF;
  background: var(--color-tab-blue); /* rotate per section */
  border-radius: var(--border-radius) var(--border-radius) 0 0;
  position: relative;
  top: -1px;
}

/* Signature: Notebook page with cream surface */
.notebook-page {
  background: var(--color-page);
  border-radius: var(--border-radius);
  padding: 48px;
  box-shadow: var(--shadow-page);
  border: 1px solid var(--color-border);
}

/* Signature: Ruled lines (subtle) */
.ruled-background {
  background-image: repeating-linear-gradient(
    to bottom,
    transparent,
    transparent 31px,
    var(--color-divider) 31px,
    var(--color-divider) 32px
  );
  background-position: 0 8px;
}

/* Signature: Margin line */
.margin-line {
  border-left: 2px solid rgba(231, 76, 60, 0.25);
  padding-left: 32px;
  margin-left: 60px;
}
```

### Recommended For

- **Audience:** Education investors, creative teams, editorial pitch reviews
- **Industry:** EdTech, publishing, creative agencies, content platforms
- **When to use:** When the deck needs to feel organized yet approachable, with clear sections
- **Avoid when:** High-growth SaaS metrics-heavy decks, deeply technical audiences

---

## 4. Swiss Modern

**Vibe:** Bauhaus-meets-Zurich. Nothing unnecessary exists. Every pixel has a purpose.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Archivo | 800 | Google Fonts | H1: 68px, H2: 48px, H3: 34px |
| Body | Nunito | 400, 600 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Swiss Modern -- */
  --preset-name: "swiss-modern";

  /* Surface */
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-black: #111111;

  /* Text */
  --color-text-primary: #111111;
  --color-text-secondary: #555555;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #999999;

  /* Accent */
  --color-accent: #FF3300;
  --color-accent-hover: #E62E00;
  --color-accent-muted: rgba(255, 51, 0, 0.08);

  /* Border & Dividers */
  --color-border: #111111;
  --color-border-light: #DDDDDD;
  --color-divider: #EEEEEE;
  --color-grid: rgba(17, 17, 17, 0.06);

  /* Typography */
  --font-display: 'Archivo', sans-serif;
  --font-body: 'Nunito', sans-serif;
  --font-size-h1: 68px;
  --font-size-h2: 48px;
  --font-size-h3: 34px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 800;
  --line-height-display: 1.05;
  --line-height-body: 1.5;
  --letter-spacing-display: -0.03em;
  --letter-spacing-label: 0.12em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 40px;
  --border-radius: 0px; /* No rounding. Swiss. */
  --border-radius-sm: 0px;
  --grid-columns: 12;
  --grid-gutter: 24px;

  /* Shadows (minimal) */
  --shadow-card: none;
  --shadow-elevated: 0 1px 3px rgba(0, 0, 0, 0.08);
}
```

### Signature Elements

**Visible grid** — A 12-column grid overlay that is faintly visible on the slide, reinforcing the systematic approach. Bold geometric color blocks.

```css
/* Signature: Visible grid overlay */
.grid-overlay {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--grid-gutter);
  padding: 0 var(--slide-padding);
  pointer-events: none;
}
.grid-overlay > div {
  background: var(--color-grid);
  height: 100%;
}

/* Signature: Red accent block */
.accent-block {
  width: 100%;
  height: 8px;
  background: var(--color-accent);
}

/* Signature: Geometric divider (black square + line) */
.swiss-divider {
  display: flex;
  align-items: center;
  gap: 16px;
}
.swiss-divider::before {
  content: '';
  width: 12px;
  height: 12px;
  background: var(--color-black);
}
.swiss-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--color-black);
}

/* Signature: Asymmetric headline placement */
.headline-swiss {
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
  font-size: var(--font-size-h1);
  line-height: var(--line-height-display);
  letter-spacing: var(--letter-spacing-display);
  text-transform: uppercase;
  max-width: 60%;
}
```

### Recommended For

- **Audience:** Design-savvy investors, architecture firms, design studios
- **Industry:** Design, architecture, industrial design, creative technology
- **When to use:** When precision and intentionality are the brand values
- **Avoid when:** Warm consumer brands, healthcare, anything needing approachability

---

## 5. Paper & Ink

**Vibe:** A long-form essay in the Sunday edition. Words matter here, and they look beautiful doing it.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Cormorant Garamond | 600, 700 | Google Fonts | H1: 64px, H2: 44px, H3: 32px |
| Body | Source Serif 4 | 400, 600 | Google Fonts | Body: 22px, Caption: 17px, Label: 14px |

### CSS Custom Properties

```css
:root {
  /* -- Paper & Ink -- */
  --preset-name: "paper-and-ink";

  /* Surface */
  --color-bg: #FAF9F7;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-paper: #F5F3EF;

  /* Text */
  --color-text-primary: #2C2C2C;
  --color-text-secondary: #5A5A5A;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #8C8C8C;

  /* Accent */
  --color-accent: #C41E3A;
  --color-accent-hover: #A31830;
  --color-accent-muted: rgba(196, 30, 58, 0.08);

  /* Border & Dividers */
  --color-border: #D8D4CE;
  --color-divider: #E8E4DD;
  --color-rule: #2C2C2C;

  /* Typography */
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'Source Serif 4', serif;
  --font-size-h1: 64px;
  --font-size-h2: 44px;
  --font-size-h3: 32px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 14px;
  --line-height-display: 1.15;
  --line-height-body: 1.65;
  --letter-spacing-display: 0em;
  --letter-spacing-label: 0.06em;

  /* Drop cap */
  --drop-cap-size: 4.5em;
  --drop-cap-line-height: 0.85;
  --drop-cap-margin-right: 8px;
  --drop-cap-color: var(--color-accent);

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 120px; /* Generous margins, editorial */
  --content-gap: 40px;
  --border-radius: 4px;
  --border-radius-sm: 2px;
  --column-width: 680px; /* Optimal reading measure */

  /* Shadows */
  --shadow-card: 0 1px 4px rgba(0, 0, 0, 0.06);
  --shadow-elevated: 0 4px 16px rgba(0, 0, 0, 0.08);
}
```

### Signature Elements

**Drop caps** — Oversized initial letters in the accent color, styled in the display serif. Paired with fine typographic rules.

```css
/* Signature: Drop cap */
.drop-cap::first-letter {
  font-family: var(--font-display);
  font-size: var(--drop-cap-size);
  font-weight: 700;
  line-height: var(--drop-cap-line-height);
  float: left;
  margin-right: var(--drop-cap-margin-right);
  color: var(--drop-cap-color);
}

/* Signature: Fine typographic rule */
.editorial-rule {
  width: 100%;
  height: 0;
  border: none;
  border-top: 1px solid var(--color-rule);
  margin: 40px 0;
}

/* Signature: Pull quote */
.pull-quote {
  font-family: var(--font-display);
  font-size: 36px;
  font-style: italic;
  line-height: 1.3;
  color: var(--color-text-primary);
  border-left: 3px solid var(--color-accent);
  padding-left: 32px;
  margin: 48px 0;
}

/* Signature: Column layout for text-heavy slides */
.two-column-editorial {
  columns: 2;
  column-gap: 64px;
  column-rule: 1px solid var(--color-divider);
}
```

### Recommended For

- **Audience:** Media investors, publishing industry, literary-adjacent brands
- **Industry:** Media, publishing, journalism, content platforms, podcasts
- **When to use:** When narrative and storytelling are the primary vehicle
- **Avoid when:** Data-heavy decks, developer tools, fast-growth SaaS metrics

---

## 6. Terminal Green

**Vibe:** SSH into the future. This deck runs on caffeine and kernel patches.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | JetBrains Mono | 700, 800 | Google Fonts | H1: 56px, H2: 40px, H3: 28px |
| Body | JetBrains Mono | 400, 500 | Google Fonts | Body: 20px, Caption: 16px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Terminal Green -- */
  --preset-name: "terminal-green";

  /* Surface */
  --color-bg: #0D1117;
  --color-surface: #161B22;
  --color-surface-elevated: #1C2128;
  --color-terminal: #0D1117;

  /* Text */
  --color-text-primary: #C9D1D9;
  --color-text-secondary: #8B949E;
  --color-text-on-accent: #0D1117;
  --color-text-muted: #484F58;

  /* Accent */
  --color-accent: #39D353;
  --color-accent-hover: #2EA043;
  --color-accent-dim: #238636;
  --color-accent-muted: rgba(57, 211, 83, 0.1);

  /* Contribution graph colors (for data viz) */
  --color-graph-0: #161B22;
  --color-graph-1: #0E4429;
  --color-graph-2: #006D32;
  --color-graph-3: #26A641;
  --color-graph-4: #39D353;

  /* Border & Dividers */
  --color-border: #30363D;
  --color-divider: #21262D;

  /* Typography */
  --font-display: 'JetBrains Mono', monospace;
  --font-body: 'JetBrains Mono', monospace;
  --font-size-h1: 56px;
  --font-size-h2: 40px;
  --font-size-h3: 28px;
  --font-size-body: 20px;
  --font-size-caption: 16px;
  --font-size-label: 13px;
  --line-height-display: 1.2;
  --line-height-body: 1.6;
  --letter-spacing-display: -0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 32px;
  --border-radius: 8px;
  --border-radius-sm: 4px;

  /* Shadows */
  --shadow-card: 0 4px 16px rgba(0, 0, 0, 0.3);
  --shadow-glow: 0 0 20px rgba(57, 211, 83, 0.15);
}
```

### Signature Elements

**Scan lines and terminal prompt** — CRT-style horizontal scan lines across the background. Text prefixed with terminal prompt characters.

```css
/* Signature: CRT scan lines */
.scanlines {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    to bottom,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.15) 2px,
    rgba(0, 0, 0, 0.15) 4px
  );
  pointer-events: none;
  opacity: 0.4;
}

/* Signature: Terminal prompt prefix */
.terminal-prompt::before {
  content: '$ ';
  color: var(--color-accent);
  font-weight: 700;
}

/* Signature: Blinking cursor */
.cursor-blink::after {
  content: '_';
  color: var(--color-accent);
  animation: blink 1s step-end infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

/* Signature: Code block container */
.code-block {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  padding: 24px;
  font-family: var(--font-body);
  font-size: var(--font-size-body);
  line-height: var(--line-height-body);
  position: relative;
}
.code-block::before {
  content: '';
  position: absolute;
  top: 12px;
  left: 12px;
  width: 48px;
  height: 12px;
  background:
    radial-gradient(circle at 6px 6px, #FF5F56 5px, transparent 5px),
    radial-gradient(circle at 24px 6px, #FFBD2E 5px, transparent 5px),
    radial-gradient(circle at 42px 6px, #27C93F 5px, transparent 5px);
}

/* Signature: GitHub-style contribution grid for metrics */
.contribution-grid {
  display: grid;
  grid-template-columns: repeat(52, 14px);
  grid-template-rows: repeat(7, 14px);
  gap: 3px;
}
.contribution-cell {
  border-radius: 2px;
  background: var(--color-graph-0);
}
```

### Recommended For

- **Audience:** Technical investors, developer community, open-source
- **Industry:** DevTools, infrastructure, developer platforms, cybersecurity
- **When to use:** When the audience writes code and appreciates the aesthetic
- **Avoid when:** Non-technical audiences, consumer brands, anything requiring warmth

---

## 7. Muted Sophistication

**Vibe:** The deck that raised a Series B at a coffee meeting. Confidence through restraint.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Satoshi | 700, 800 | Fontshare | H1: 64px, H2: 44px, H3: 32px |
| Body | DM Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Muted Sophistication -- */
  --preset-name: "muted-sophistication";

  /* Surface */
  --color-bg: #FAFAF8;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-muted: #F2F1EE;

  /* Text */
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #6B6B6B;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #9B9B9B;

  /* Accent — single blue, used sparingly */
  --color-accent: #2D5BFF;
  --color-accent-hover: #1A45E0;
  --color-accent-muted: #D4DFFF;
  --color-accent-subtle: rgba(45, 91, 255, 0.06);

  /* Border & Dividers */
  --color-border: #E5E3DF;
  --color-divider: #EEEDEA;

  /* Typography */
  --font-display: 'Satoshi', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-size-h1: 64px;
  --font-size-h2: 44px;
  --font-size-h3: 32px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 700;
  --line-height-display: 1.12;
  --line-height-body: 1.6;
  --letter-spacing-display: -0.025em;
  --letter-spacing-label: 0.04em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 120px; /* Generous — whitespace is the design */
  --content-gap: 48px;
  --border-radius: 12px;
  --border-radius-sm: 6px;
  --whitespace-ratio: 0.4; /* Target: 40%+ whitespace per slide */

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.04), 0 4px 12px rgba(0, 0, 0, 0.03);
  --shadow-elevated: 0 2px 8px rgba(0, 0, 0, 0.04), 0 8px 24px rgba(0, 0, 0, 0.06);
}
```

### Signature Elements

**Generous whitespace and editorial left-alignment** — The defining characteristic is what is NOT on the slide. One accent color used only for CTAs and key metrics.

```css
/* Signature: Left-aligned editorial layout (content hugs left, right breathes) */
.editorial-layout {
  display: grid;
  grid-template-columns: 55% 1fr;
  gap: var(--content-gap);
  align-items: start;
  padding: var(--slide-padding);
}

/* Signature: Accent dot indicator */
.accent-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-accent);
  margin-right: 12px;
  vertical-align: middle;
}

/* Signature: Subtle metric highlight */
.metric-card {
  padding: 32px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-card);
}
.metric-card .value {
  font-family: var(--font-display);
  font-size: 56px;
  font-weight: 800;
  color: var(--color-text-primary);
  letter-spacing: -0.03em;
}
.metric-card .label {
  font-family: var(--font-body);
  font-size: var(--font-size-caption);
  color: var(--color-text-secondary);
  margin-top: 8px;
}

/* Signature: Thin bottom progress bar */
.slide-progress {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  background: var(--color-accent);
  /* width set dynamically per slide */
}
```

### Recommended For

- **Audience:** VC Series A through C, institutional investors, PE firms
- **Industry:** General fundraising, B2B SaaS, platform companies
- **When to use:** Default choice when unsure. This is the safest, most universally professional preset
- **Avoid when:** When you need strong brand personality or visual excitement

---

## 8. Dark Premium

**Vibe:** The dashboard you pay $299/month for. Polished dark surfaces with light that lives inside the UI.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | General Sans | 700, 800 | Fontshare | H1: 64px, H2: 44px, H3: 32px |
| Body | General Sans | 400, 500 | Fontshare | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Dark Premium -- */
  --preset-name: "dark-premium";

  /* Surface */
  --color-bg: #0A0A0A;
  --color-surface: #141414;
  --color-surface-elevated: #1E1E1E;
  --color-surface-hover: #262626;

  /* Text */
  --color-text-primary: #F5F5F5;
  --color-text-secondary: #8A8A8A;
  --color-text-on-accent: #0A0A0A;
  --color-text-muted: #525252;

  /* Accent */
  --color-accent: #818CF8;
  --color-accent-hover: #6366F1;
  --color-accent-glow: rgba(129, 140, 248, 0.15);
  --color-accent-muted: rgba(129, 140, 248, 0.08);

  /* Border & Dividers */
  --color-border: rgba(255, 255, 255, 0.06);
  --color-border-hover: rgba(255, 255, 255, 0.1);
  --color-divider: rgba(255, 255, 255, 0.04);

  /* Typography */
  --font-display: 'General Sans', sans-serif;
  --font-body: 'General Sans', sans-serif;
  --font-size-h1: 64px;
  --font-size-h2: 44px;
  --font-size-h3: 32px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 700;
  --line-height-display: 1.1;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.025em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 32px;
  --border-radius: 16px;
  --border-radius-sm: 8px;

  /* Shadows & Glow */
  --shadow-card: 0 0 0 1px var(--color-border), 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-elevated: 0 0 0 1px var(--color-border), 0 8px 32px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 40px var(--color-accent-glow);
  --shadow-glow-strong: 0 0 80px rgba(129, 140, 248, 0.25);
}
```

### Signature Elements

**Subtle glow effects and barely-there borders** — Cards feel like they float on darkness. Accent color creates a soft ambient glow behind key elements.

```css
/* Signature: Glowing card */
.glow-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  padding: 32px;
  position: relative;
  box-shadow: var(--shadow-card);
}
.glow-card::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: var(--border-radius);
  background: linear-gradient(
    135deg,
    rgba(129, 140, 248, 0.1),
    transparent 40%
  );
  z-index: -1;
  pointer-events: none;
}

/* Signature: Ambient glow behind metrics */
.metric-glow {
  position: relative;
}
.metric-glow::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle,
    var(--color-accent-glow),
    transparent 60%
  );
  pointer-events: none;
  z-index: -1;
}

/* Signature: Elevated surface stack */
.surface-stack {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-sm);
  padding: 24px;
  box-shadow: var(--shadow-elevated);
}

/* Signature: Gradient text for hero numbers */
.gradient-number {
  font-family: var(--font-display);
  font-size: 80px;
  font-weight: 800;
  background: linear-gradient(135deg, var(--color-accent), #C4B5FD);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### Recommended For

- **Audience:** Tech-forward investors, product demos, SaaS showcase
- **Industry:** SaaS, DevTools, AI/ML, analytics platforms
- **When to use:** When the product itself has a dark UI, or when targeting technical audiences
- **Avoid when:** Healthcare, finance (unless fintech), traditional enterprise

---

## 9. Cloud Dancer

**Vibe:** A deep breath before the big meeting. Calm conviction powered by Pantone's 2026 Color of the Year.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Fraunces | 700, 900 | Google Fonts | H1: 64px, H2: 44px, H3: 32px |
| Body | Work Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Cloud Dancer -- */
  --preset-name: "cloud-dancer";

  /* Surface — based on Pantone 11-0602 Cloud Dancer */
  --color-bg: #F0EEE9;
  --color-surface: #F7F6F2;
  --color-surface-elevated: #FFFFFF;
  --color-surface-warm: #E8E4DC;

  /* Text */
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #7A7A7A;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #ABABAB;

  /* Accent — transformative teal */
  --color-accent: #2A7F8E;
  --color-accent-hover: #237080;
  --color-accent-muted: #D4EDED;
  --color-accent-subtle: rgba(42, 127, 142, 0.06);

  /* Warm */
  --color-warm: #C9A882;
  --color-warm-muted: rgba(201, 168, 130, 0.15);

  /* Border & Dividers */
  --color-border: #DCD8D0;
  --color-divider: #E8E4DC;

  /* Typography */
  --font-display: 'Fraunces', serif;
  --font-body: 'Work Sans', sans-serif;
  --font-size-h1: 64px;
  --font-size-h2: 44px;
  --font-size-h3: 32px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 700;
  --line-height-display: 1.15;
  --line-height-body: 1.6;
  --letter-spacing-display: -0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 100px;
  --content-gap: 48px;
  --border-radius: 16px;
  --border-radius-sm: 8px;

  /* Shadows — soft and warm */
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.04), 0 8px 24px rgba(0, 0, 0, 0.03);
  --shadow-elevated: 0 4px 12px rgba(0, 0, 0, 0.05), 0 12px 32px rgba(0, 0, 0, 0.05);
  --shadow-warm: 0 4px 20px rgba(201, 168, 130, 0.1);
}
```

### Signature Elements

**Soft shadows, rounded elements, mindful whitespace** — Every element feels considered. Rounded corners and warm neutrals create a sense of calm intentionality.

```css
/* Signature: Rounded content card */
.cloud-card {
  background: var(--color-surface-elevated);
  border-radius: var(--border-radius);
  padding: 40px;
  box-shadow: var(--shadow-card);
  border: 1px solid var(--color-border);
}

/* Signature: Teal accent pill */
.accent-pill {
  display: inline-block;
  padding: 6px 16px;
  background: var(--color-accent-muted);
  color: var(--color-accent);
  border-radius: 100px;
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* Signature: Warm divider with dot */
.mindful-divider {
  display: flex;
  align-items: center;
  gap: 24px;
  margin: 40px 0;
}
.mindful-divider::before,
.mindful-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--color-border);
}
.mindful-divider::after {
  content: '';
}
.mindful-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-warm);
}

/* Signature: Soft background shape */
.cloud-shape {
  position: absolute;
  width: 600px;
  height: 400px;
  border-radius: 50%;
  background: linear-gradient(
    135deg,
    rgba(42, 127, 142, 0.04),
    rgba(201, 168, 130, 0.06)
  );
  filter: blur(80px);
  pointer-events: none;
}
```

### Recommended For

- **Audience:** 2026-aware investors, ESG-focused funds, impact investors
- **Industry:** Wellness, sustainability, clean tech, mindful tech, ESG
- **When to use:** When calm confidence and contemporary relevance matter
- **Avoid when:** Aggressive growth narratives, hardcore fintech, developer tools

---

## 10. Fintech Trust

**Vibe:** Your money is safe here. Precision measured in basis points, trust measured in decades.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Manrope | 700, 800 | Google Fonts | H1: 60px, H2: 42px, H3: 30px |
| Body | Manrope | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |
| Data | JetBrains Mono | 500 | Google Fonts | Numbers: 22px, Figures: 48px |

### CSS Custom Properties

```css
:root {
  /* -- Fintech Trust -- */
  --preset-name: "fintech-trust";

  /* Surface */
  --color-bg: #FFFFFF;
  --color-surface: #F7F8FA;
  --color-surface-elevated: #FFFFFF;
  --color-surface-data: #FAFBFC;

  /* Text */
  --color-text-primary: #0A1628;
  --color-text-secondary: #4A5568;
  --color-text-on-accent: #0A1628;
  --color-text-muted: #A0AEC0;

  /* Accent */
  --color-accent-gold: #C9A84C;
  --color-accent-gold-hover: #B8973F;
  --color-accent-gold-muted: rgba(201, 168, 76, 0.1);
  --color-accent-navy: #1E3A5F;
  --color-accent-navy-muted: rgba(30, 58, 95, 0.06);

  /* Status */
  --color-positive: #059669;
  --color-negative: #DC2626;
  --color-neutral: #6B7280;

  /* Border & Dividers */
  --color-border: #E2E8F0;
  --color-divider: #EDF2F7;
  --color-table-stripe: #F7FAFC;

  /* Typography */
  --font-display: 'Manrope', sans-serif;
  --font-body: 'Manrope', sans-serif;
  --font-data: 'JetBrains Mono', monospace;
  --font-size-h1: 60px;
  --font-size-h2: 42px;
  --font-size-h3: 30px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-size-figure: 48px;
  --font-weight-display: 700;
  --line-height-display: 1.15;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.02em;
  --letter-spacing-data: 0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 32px;
  --border-radius: 8px;
  --border-radius-sm: 4px;
  --table-cell-padding: 12px 16px;

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.06);
  --shadow-elevated: 0 4px 12px rgba(0, 0, 0, 0.08);
}
```

### Signature Elements

**Precise grids, data tables, monospace numbers, gold accents** — Financial data presented with the precision of a Bloomberg terminal but the polish of a private bank.

```css
/* Signature: Data table */
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-body);
  font-size: var(--font-size-body);
}
.data-table th {
  text-align: left;
  padding: var(--table-cell-padding);
  font-weight: 600;
  font-size: var(--font-size-label);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--color-text-muted);
  border-bottom: 2px solid var(--color-accent-navy);
}
.data-table td {
  padding: var(--table-cell-padding);
  border-bottom: 1px solid var(--color-divider);
}
.data-table tr:nth-child(even) {
  background: var(--color-table-stripe);
}

/* Signature: Monospace number formatting */
.figure {
  font-family: var(--font-data);
  font-size: var(--font-size-figure);
  font-weight: 500;
  letter-spacing: var(--letter-spacing-data);
  color: var(--color-text-primary);
}
.figure-positive { color: var(--color-positive); }
.figure-negative { color: var(--color-negative); }
.figure-positive::before { content: '+'; }

/* Signature: Gold accent bar (key metric) */
.gold-bar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 24px;
  background: var(--color-accent-gold-muted);
  border-left: 4px solid var(--color-accent-gold);
  border-radius: 0 var(--border-radius-sm) var(--border-radius-sm) 0;
}

/* Signature: KPI grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--color-border);
  border-radius: var(--border-radius);
  overflow: hidden;
}
.kpi-cell {
  background: var(--color-bg);
  padding: 32px;
  text-align: center;
}
```

### Recommended For

- **Audience:** Financial institution investors, bank partnerships, insurance boards
- **Industry:** Fintech, banking, insurance, wealth management, payments
- **When to use:** When numbers tell the story and trust must be earned through precision
- **Avoid when:** Consumer-facing pitches, creative industries, early-stage concept decks

---

## 11. HealthTech Clean

**Vibe:** FDA-cleared confidence. Clinical precision meets modern product design.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Plus Jakarta Sans | 700, 800 | Google Fonts | H1: 60px, H2: 42px, H3: 30px |
| Body | Plus Jakarta Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- HealthTech Clean -- */
  --preset-name: "healthtech-clean";

  /* Surface */
  --color-bg: #FFFFFF;
  --color-surface: #F7F9FC;
  --color-surface-elevated: #FFFFFF;

  /* Text */
  --color-text-primary: #1A202C;
  --color-text-secondary: #718096;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #A0AEC0;

  /* Accent */
  --color-accent: #2B6CB0;
  --color-accent-hover: #2C5282;
  --color-accent-muted: rgba(43, 108, 176, 0.08);
  --color-accent-light: #BEE3F8;

  /* Status */
  --color-success: #38A169;
  --color-success-muted: rgba(56, 161, 105, 0.08);
  --color-warning: #D69E2E;
  --color-danger: #E53E3E;

  /* Border & Dividers */
  --color-border: #E2E8F0;
  --color-divider: #EDF2F7;

  /* Typography */
  --font-display: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-size-h1: 60px;
  --font-size-h2: 42px;
  --font-size-h3: 30px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 700;
  --line-height-display: 1.15;
  --line-height-body: 1.6;
  --letter-spacing-display: -0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 32px;
  --border-radius: 12px;
  --border-radius-sm: 6px;

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.04), 0 4px 12px rgba(0, 0, 0, 0.03);
  --shadow-elevated: 0 4px 12px rgba(0, 0, 0, 0.06), 0 8px 24px rgba(0, 0, 0, 0.04);
}
```

### Signature Elements

**Clean lines, certification badges, green for positive metrics** — Clinical cleanliness with enough warmth to feel modern, not sterile.

```css
/* Signature: Certification badge area */
.cert-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 100px;
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  color: var(--color-text-secondary);
}
.cert-badge::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-success);
}

/* Signature: Clinical stat card */
.stat-clinical {
  padding: 32px;
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-card);
}
.stat-clinical .value {
  font-family: var(--font-display);
  font-size: 48px;
  font-weight: 800;
  color: var(--color-accent);
}
.stat-clinical .trend-positive {
  color: var(--color-success);
  font-size: var(--font-size-caption);
  font-weight: 500;
}

/* Signature: Clean horizontal rule with label */
.labeled-rule {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 32px 0;
}
.labeled-rule .label {
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-text-muted);
  white-space: nowrap;
}
.labeled-rule .line {
  flex: 1;
  height: 1px;
  background: var(--color-border);
}

/* Signature: Compliance footer strip */
.compliance-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px var(--slide-padding);
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  font-family: var(--font-body);
  font-size: 11px;
  color: var(--color-text-muted);
  display: flex;
  justify-content: space-between;
}
```

### Recommended For

- **Audience:** Healthcare investors, hospital procurement, regulatory reviewers
- **Industry:** MedTech, pharma, digital health, telemedicine, biotech
- **When to use:** When clinical credibility and regulatory compliance matter
- **Avoid when:** Consumer lifestyle brands, creative industries

---

## 12. AI Frontier

**Vibe:** Somewhere between a research paper and a science fiction film. Intelligence made visible.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Clash Display | 600, 700 | Fontshare | H1: 68px, H2: 46px, H3: 34px |
| Body | Satoshi | 400, 500 | Fontshare | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- AI Frontier -- */
  --preset-name: "ai-frontier";

  /* Surface */
  --color-bg: #0B0F1A;
  --color-surface: #111827;
  --color-surface-elevated: #1A2236;
  --color-surface-hover: #1F2A40;

  /* Text */
  --color-text-primary: #E8ECF1;
  --color-text-secondary: #7B8794;
  --color-text-on-accent: #0B0F1A;
  --color-text-muted: #4A5568;

  /* Accent — dual color system */
  --color-accent-cyan: #00D4AA;
  --color-accent-purple: #8B5CF6;
  --color-accent-cyan-muted: rgba(0, 212, 170, 0.1);
  --color-accent-purple-muted: rgba(139, 92, 246, 0.1);

  /* Gradient */
  --gradient-primary: linear-gradient(135deg, #00D4AA, #8B5CF6);
  --gradient-subtle: linear-gradient(135deg, rgba(0, 212, 170, 0.15), rgba(139, 92, 246, 0.15));
  --gradient-glow: radial-gradient(ellipse at center, rgba(0, 212, 170, 0.08), transparent 70%);

  /* Border & Dividers */
  --color-border: rgba(255, 255, 255, 0.06);
  --color-border-accent: rgba(0, 212, 170, 0.2);
  --color-divider: rgba(255, 255, 255, 0.04);

  /* Typography */
  --font-display: 'Clash Display', sans-serif;
  --font-body: 'Satoshi', sans-serif;
  --font-size-h1: 68px;
  --font-size-h2: 46px;
  --font-size-h3: 34px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 600;
  --line-height-display: 1.1;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.02em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 40px;
  --border-radius: 16px;
  --border-radius-sm: 8px;

  /* Shadows & Glow */
  --shadow-card: 0 0 0 1px var(--color-border), 0 8px 24px rgba(0, 0, 0, 0.4);
  --shadow-elevated: 0 0 0 1px var(--color-border), 0 16px 48px rgba(0, 0, 0, 0.5);
  --shadow-glow-cyan: 0 0 40px rgba(0, 212, 170, 0.15);
  --shadow-glow-purple: 0 0 40px rgba(139, 92, 246, 0.15);
}
```

### Signature Elements

**Mesh gradient backgrounds, particle dots, gradient text, grid overlay** — Visual language that suggests neural networks and data flow without being literal.

```css
/* Signature: Mesh gradient background */
.mesh-gradient {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 20% 50%, rgba(0, 212, 170, 0.08), transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(139, 92, 246, 0.08), transparent 50%),
    radial-gradient(ellipse at 60% 80%, rgba(0, 212, 170, 0.05), transparent 50%);
  pointer-events: none;
}

/* Signature: Dot grid overlay */
.dot-grid {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(
    circle at center,
    rgba(255, 255, 255, 0.03) 1px,
    transparent 1px
  );
  background-size: 32px 32px;
  pointer-events: none;
}

/* Signature: Gradient text for key metrics */
.gradient-text {
  font-family: var(--font-display);
  font-size: 80px;
  font-weight: 700;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Signature: Neural connection line */
.neural-line {
  position: absolute;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--color-accent-cyan),
    transparent
  );
  opacity: 0.3;
}

/* Signature: Glowing border card */
.frontier-card {
  background: var(--color-surface);
  border-radius: var(--border-radius);
  padding: 32px;
  position: relative;
  box-shadow: var(--shadow-card);
}
.frontier-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--border-radius);
  padding: 1px;
  background: var(--gradient-primary);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0.3;
  pointer-events: none;
}
```

### Recommended For

- **Audience:** Deep tech investors, AI/ML conference demos, research showcases
- **Industry:** AI/ML, deep tech, autonomous systems, robotics, quantum computing
- **When to use:** When the technology IS the story and the audience expects innovation in presentation
- **Avoid when:** Conservative investors, healthcare compliance, traditional enterprise

---

## 13. DACH Enterprise

**Vibe:** The Mittelstand meeting room. Thorough, structured, institutional. Substance over flash.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Libre Franklin | 700, 800 | Google Fonts | H1: 56px, H2: 40px, H3: 28px |
| Body | Libre Franklin | 400, 500 | Google Fonts | Body: 20px, Caption: 16px, Label: 12px |

### CSS Custom Properties

```css
:root {
  /* -- DACH Enterprise -- */
  --preset-name: "dach-enterprise";

  /* Surface */
  --color-bg: #F7F8FA;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-header: #1A202C;

  /* Text */
  --color-text-primary: #1A202C;
  --color-text-secondary: #4A5568;
  --color-text-on-dark: #F7F8FA;
  --color-text-muted: #A0AEC0;

  /* Accent */
  --color-accent: #1A56DB;
  --color-accent-hover: #1646B8;
  --color-accent-muted: rgba(26, 86, 219, 0.06);
  --color-accent-secondary: #6B7280;

  /* Border & Dividers */
  --color-border: #D1D5DB;
  --color-divider: #E5E7EB;
  --color-table-header: #F3F4F6;

  /* Typography */
  --font-display: 'Libre Franklin', sans-serif;
  --font-body: 'Libre Franklin', sans-serif;
  --font-size-h1: 56px;
  --font-size-h2: 40px;
  --font-size-h3: 28px;
  --font-size-body: 20px;
  --font-size-caption: 16px;
  --font-size-label: 12px;
  --font-weight-display: 700;
  --line-height-display: 1.2;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.01em;
  --letter-spacing-label: 0.06em;

  /* Layout — tighter spacing, more content per slide */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 64px;
  --content-gap: 24px;
  --border-radius: 6px;
  --border-radius-sm: 3px;

  /* Shadows */
  --shadow-card: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-elevated: 0 2px 8px rgba(0, 0, 0, 0.08);
}
```

### Signature Elements

**Structured layouts, higher text density, institutional credibility markers, conservative spacing** — German-market appropriate information density with clear hierarchy.

```css
/* Signature: Dark header bar */
.slide-header-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 72px;
  background: var(--color-surface-header);
  display: flex;
  align-items: center;
  padding: 0 var(--slide-padding);
}
.slide-header-bar .title {
  font-family: var(--font-display);
  font-size: var(--font-size-h3);
  font-weight: 600;
  color: var(--color-text-on-dark);
}

/* Signature: Structured content grid (dense) */
.content-grid-dense {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

/* Signature: Section numbering */
.section-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: var(--color-accent);
  color: var(--color-text-on-dark);
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 700;
  border-radius: 50%;
  margin-right: 12px;
}

/* Signature: Institutional footer */
.institutional-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--slide-padding);
  font-family: var(--font-body);
  font-size: 11px;
  color: var(--color-text-muted);
}

/* Signature: Bullet list with accent indicators */
.structured-list {
  list-style: none;
  padding: 0;
}
.structured-list li {
  padding: 8px 0 8px 20px;
  border-bottom: 1px solid var(--color-divider);
  position: relative;
  font-family: var(--font-body);
  font-size: var(--font-size-body);
}
.structured-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  background: var(--color-accent);
  border-radius: 1px;
}
```

### Recommended For

- **Audience:** DACH-region investors, German Mittelstand, EU institutional
- **Industry:** B2B enterprise, industrial, Foerderantraege (grant applications), institutional presentations
- **When to use:** When presenting to German/Austrian/Swiss audiences who value substance and structure
- **Avoid when:** US West Coast VC culture, consumer brands, creative pitches

---

## 14. Board Executive

**Vibe:** The quarterly board deck. No surprises, just clarity. Red means act, green means continue.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Source Serif 4 | 600, 700 | Google Fonts | H1: 56px, H2: 40px, H3: 28px |
| Body | Fira Sans | 400, 500 | Google Fonts | Body: 20px, Caption: 16px, Label: 12px |
| Data | JetBrains Mono | 500 | Google Fonts | Numbers: 20px, KPIs: 44px |

### CSS Custom Properties

```css
:root {
  /* -- Board Executive -- */
  --preset-name: "board-executive";

  /* Surface */
  --color-bg: #FAF9F7;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-data: #F7F6F4;

  /* Text */
  --color-text-primary: #1F2937;
  --color-text-secondary: #6B7280;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #9CA3AF;

  /* Accent */
  --color-accent: #B45309;
  --color-accent-hover: #92400E;
  --color-accent-muted: rgba(180, 83, 9, 0.08);

  /* RAG Status Indicators */
  --color-rag-red: #DC2626;
  --color-rag-amber: #D97706;
  --color-rag-green: #059669;
  --color-rag-red-bg: rgba(220, 38, 38, 0.06);
  --color-rag-amber-bg: rgba(217, 119, 6, 0.06);
  --color-rag-green-bg: rgba(5, 150, 105, 0.06);

  /* Border & Dividers */
  --color-border: #E5E7EB;
  --color-divider: #F3F4F6;
  --color-table-header-bg: #F9FAFB;

  /* Typography */
  --font-display: 'Source Serif 4', serif;
  --font-body: 'Fira Sans', sans-serif;
  --font-data: 'JetBrains Mono', monospace;
  --font-size-h1: 56px;
  --font-size-h2: 40px;
  --font-size-h3: 28px;
  --font-size-body: 20px;
  --font-size-caption: 16px;
  --font-size-label: 12px;
  --font-size-kpi: 44px;
  --font-weight-display: 600;
  --line-height-display: 1.2;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.01em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 64px;
  --content-gap: 24px;
  --border-radius: 8px;
  --border-radius-sm: 4px;

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0, 0, 0, 0.04);
  --shadow-elevated: 0 2px 8px rgba(0, 0, 0, 0.06);
}
```

### Signature Elements

**Dashboard-style layouts, RAG indicators, data tables, executive summary format** — Every slide answers "so what?" with data and a clear status signal.

```css
/* Signature: RAG status indicator */
.rag-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 100px;
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.rag-red {
  background: var(--color-rag-red-bg);
  color: var(--color-rag-red);
}
.rag-amber {
  background: var(--color-rag-amber-bg);
  color: var(--color-rag-amber);
}
.rag-green {
  background: var(--color-rag-green-bg);
  color: var(--color-rag-green);
}
.rag-indicator::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

/* Signature: Executive KPI row */
.kpi-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.kpi-card {
  padding: 24px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius);
}
.kpi-card .value {
  font-family: var(--font-data);
  font-size: var(--font-size-kpi);
  font-weight: 500;
  color: var(--color-text-primary);
}
.kpi-card .label {
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-top: 8px;
}

/* Signature: Executive summary block */
.exec-summary {
  padding: 32px;
  background: var(--color-surface);
  border-left: 4px solid var(--color-accent);
  border-radius: 0 var(--border-radius) var(--border-radius) 0;
  box-shadow: var(--shadow-card);
}
.exec-summary .title {
  font-family: var(--font-display);
  font-size: var(--font-size-h3);
  font-weight: 600;
  margin-bottom: 16px;
}

/* Signature: Comparison table with delta column */
.comparison-table .delta-positive {
  font-family: var(--font-data);
  color: var(--color-rag-green);
}
.comparison-table .delta-negative {
  font-family: var(--font-data);
  color: var(--color-rag-red);
}
```

### Recommended For

- **Audience:** Board of directors, C-level executives, PE portfolio reviews
- **Industry:** Any industry at board/executive level, quarterly reviews, annual reports
- **When to use:** When decisions will be made based on this deck and status must be instantly clear
- **Avoid when:** External fundraising (use Muted Sophistication instead), creative pitches

---

## 15. Startup Bold

**Vibe:** Move fast, be memorable, own a color. The deck equivalent of a neon sign on a warm street.

### Typography

| Role | Font | Weight | Source | Sizes |
|------|------|--------|--------|-------|
| Display | Syne | 700, 800 | Google Fonts | H1: 72px, H2: 48px, H3: 34px |
| Body | DM Sans | 400, 500 | Google Fonts | Body: 22px, Caption: 17px, Label: 13px |

### CSS Custom Properties

```css
:root {
  /* -- Startup Bold -- */
  --preset-name: "startup-bold";

  /* Surface */
  --color-bg: #FFF8E7;
  --color-surface: #FFFFFF;
  --color-surface-elevated: #FFFFFF;
  --color-surface-accent: #FF5C00; /* Full-bleed accent sections */

  /* Text */
  --color-text-primary: #1B1B1B;
  --color-text-secondary: #7A6F5F;
  --color-text-on-accent: #FFFFFF;
  --color-text-muted: #B0A894;

  /* Accent — bold orange (replace with user brand color) */
  --color-accent: #FF5C00;
  --color-accent-hover: #E65200;
  --color-accent-muted: rgba(255, 92, 0, 0.1);
  --color-accent-badge: rgba(255, 92, 0, 0.1);

  /* Border & Dividers */
  --color-border: #E8E0D0;
  --color-divider: #F0E8D8;

  /* Typography */
  --font-display: 'Syne', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-size-h1: 72px;
  --font-size-h2: 48px;
  --font-size-h3: 34px;
  --font-size-body: 22px;
  --font-size-caption: 17px;
  --font-size-label: 13px;
  --font-weight-display: 800;
  --line-height-display: 1.05;
  --line-height-body: 1.55;
  --letter-spacing-display: -0.03em;

  /* Layout */
  --slide-width: 1920px;
  --slide-height: 1080px;
  --slide-padding: 80px;
  --content-gap: 40px;
  --border-radius: 20px;
  --border-radius-sm: 10px;

  /* Shadows */
  --shadow-card: 0 4px 16px rgba(0, 0, 0, 0.06);
  --shadow-elevated: 0 8px 32px rgba(0, 0, 0, 0.1);
  --shadow-accent: 0 8px 24px rgba(255, 92, 0, 0.2);
}
```

### Signature Elements

**Bold color blocks, playful rounded elements, oversized numbers, full-bleed accent sections** — Every slide has at least one moment of visual surprise.

```css
/* Signature: Full-bleed accent section */
.accent-bleed {
  position: absolute;
  inset: 0;
  background: var(--color-surface-accent);
  color: var(--color-text-on-accent);
}
.accent-bleed-half {
  position: absolute;
  top: 0;
  right: 0;
  width: 50%;
  height: 100%;
  background: var(--color-surface-accent);
  border-radius: var(--border-radius) 0 0 var(--border-radius);
}

/* Signature: Oversized metric number */
.oversized-number {
  font-family: var(--font-display);
  font-size: 160px;
  font-weight: 800;
  line-height: 0.9;
  letter-spacing: -0.04em;
  color: var(--color-accent);
}

/* Signature: Brand badge pill */
.brand-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 20px;
  background: var(--color-accent-badge);
  border-radius: 100px;
  font-family: var(--font-body);
  font-size: var(--font-size-label);
  font-weight: 500;
  color: var(--color-accent);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* Signature: Playful rounded card */
.playful-card {
  background: var(--color-surface);
  border-radius: var(--border-radius);
  padding: 40px;
  box-shadow: var(--shadow-card);
  border: 2px solid var(--color-border);
  position: relative;
  overflow: hidden;
}
.playful-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: var(--color-accent);
}

/* Signature: Stacked emphasis blocks */
.emphasis-stack {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.emphasis-block {
  display: inline-block;
  padding: 4px 16px;
  background: var(--color-accent);
  color: var(--color-text-on-accent);
  font-family: var(--font-display);
  font-size: var(--font-size-h2);
  font-weight: 800;
  line-height: 1.2;
  width: fit-content;
}
```

### Recommended For

- **Audience:** Angel investors, accelerator demo days, consumer-facing VCs
- **Industry:** Consumer, D2C, marketplace, social, gaming
- **When to use:** When brand energy and memorability matter more than institutional credibility
- **Avoid when:** Board presentations, healthcare, conservative financial institutions

---

## Font Pairing Quick Reference

| # | Preset | Display Font | Body Font | Source |
|---|--------|-------------|-----------|--------|
| 1 | Bold Signal | Archivo Black | Space Grotesk | Google / Google |
| 2 | Dark Botanical | Cormorant | IBM Plex Sans | Google / Google |
| 3 | Notebook Tabs | Bodoni Moda | DM Sans | Google / Google |
| 4 | Swiss Modern | Archivo (800) | Nunito | Google / Google |
| 5 | Paper & Ink | Cormorant Garamond | Source Serif 4 | Google / Google |
| 6 | Terminal Green | JetBrains Mono | JetBrains Mono | Google / Google |
| 7 | Muted Sophistication | Satoshi | DM Sans | Fontshare / Google |
| 8 | Dark Premium | General Sans | General Sans | Fontshare / Fontshare |
| 9 | Cloud Dancer | Fraunces | Work Sans | Google / Google |
| 10 | Fintech Trust | Manrope | Manrope | Google / Google |
| 11 | HealthTech Clean | Plus Jakarta Sans | Plus Jakarta Sans | Google / Google |
| 12 | AI Frontier | Clash Display | Satoshi | Fontshare / Fontshare |
| 13 | DACH Enterprise | Libre Franklin | Libre Franklin | Google / Google |
| 14 | Board Executive | Source Serif 4 | Fira Sans | Google / Google |
| 15 | Startup Bold | Syne | DM Sans | Google / Google |

### Fontshare Embed Links

Fontshare fonts require different embedding than Google Fonts. Use these base URLs:

```
Satoshi:       https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,800&display=swap
General Sans:  https://api.fontshare.com/v2/css?f[]=general-sans@400,500,700,800&display=swap
Clash Display: https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap
```

### Google Fonts Embed Pattern

```
https://fonts.googleapis.com/css2?family=FONT_NAME:wght@400;500;700;800&display=swap
```

Replace spaces in font names with `+` (e.g., `Plus+Jakarta+Sans`).

---

## DO NOT USE — Generic AI Patterns to Avoid

These patterns appear in nearly every AI-generated pitch deck. They signal "template" instantly.

### Colors
- **#6366F1 (Indigo-500) as the sole accent** — It is the default AI output color. If using indigo, use a variant (#818CF8 on dark backgrounds as in Dark Premium, or pair it in a gradient as in AI Frontier, never as the standalone accent on white).
- **Purple-to-blue gradient on white background** — The "AI startup 2024" cliche. Gradients belong on dark backgrounds or as subtle accents.
- **Pure #000000 for text** — Too harsh. Use #1A1A1A, #1F2937, #0A1628, or similar near-blacks.
- **Pure #FFFFFF for backgrounds** — Too clinical. Use #FAFAF8, #FAF9F7, #F7F8FA, or similar warm/cool off-whites. Exception: Fintech Trust and HealthTech Clean use #FFFFFF intentionally for clinical/institutional tone.

### Fonts
- **Inter as a display font** — Inter is a fine UI font but lacks personality for headlines. Use it for body text only if at all.
- **Roboto** — Google's system font. Signals "default Android app" not "funded startup."
- **Arial** — The Comic Sans of professional decks. Never.
- **Montserrat for headlines** — Overused in 2020-2024 pitch decks. Exhausted.
- **Poppins for headlines** — Same problem as Montserrat. Fine for body text in specific contexts but overdone in display.

### Layout
- **Centered everything** — Real design uses alignment tension. Left-align by default, center only for title slides and key metric callouts.
- **Equal padding all sides** — Creates a "stamp" effect. Use asymmetric padding (more left/right, less top/bottom, or vice versa) for editorial feel.
- **12px border-radius on everything** — Pick your radius system per preset and be consistent. Swiss Modern uses 0px. Startup Bold uses 20px. Mixing is worse than either extreme.

### Decorative
- **Abstract blob/wave SVGs in corners** — The "SaaS website hero section" pattern. Avoid unless highly intentional (Dark Botanical's gradient orbs are the controlled version of this).
- **Generic icons from icon libraries without modification** — Icons should match the preset's weight and style system.
- **Drop shadows on every element** — Choose: shadows OR borders. Both creates visual noise. Most presets here use one system.

---

## CSS Gotchas for PDF Rendering

### What Works in PDF

These CSS properties render reliably across PDF engines (wkhtmltopdf, Puppeteer, Playwright):

```
color, background-color, background (solid, linear-gradient, radial-gradient)
font-family, font-size, font-weight, font-style
line-height, letter-spacing, text-transform, text-align
padding, margin, width, height, max-width
border, border-radius, border-color
box-shadow (simple)
display: flex, display: grid (basic)
position: absolute/relative
clip-path (basic shapes: polygon, circle, inset)
opacity
```

### What May Not Work in PDF

```
filter: blur()          — Use pre-blurred gradient backgrounds instead of runtime blur
backdrop-filter          — Not supported; fake it with semi-transparent overlays
animation / @keyframes   — Ignored in PDF; use for screen preview only
transition               — Ignored in PDF
:hover, :focus           — No interactivity in PDF
mix-blend-mode           — Inconsistent; avoid for critical elements
-webkit-text-fill-color  — Works in Chromium-based renderers (Puppeteer) but NOT wkhtmltopdf
background-clip: text    — Same as above; provide fallback solid color
container queries         — Not supported; use fixed-width layouts
```

### Font Size Rules for Fixed-Size Slides

Since slides are always 1920x1080px:

- **Do not use `clamp()`** — No viewport variation in a fixed canvas. Use exact `px` values.
- **Do not use `rem` or `em`** — PDF renderers may not respect the root font-size correctly. Use `px`.
- **Do not use `vw` or `vh`** — Viewport units in PDF context are unreliable.

### Gradient Text Fallback Pattern

For presets that use `-webkit-background-clip: text` (Dark Premium, AI Frontier):

```css
/* Always provide a solid color fallback */
.gradient-text {
  color: var(--color-accent-cyan); /* Fallback for non-Chromium renderers */
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### Print Color Accuracy

PDF colors can shift slightly. These rules help:

```css
@media print {
  * {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    color-adjust: exact;
  }
}
```

Always include this in the global stylesheet when targeting PDF output.

---

## Preset Selection Guide

Use this decision tree to pick the right preset:

```
Is this an internal (board/exec) presentation?
  YES -> Board Executive (#14)
  NO  -> Continue

Is this for DACH/EU institutional audience?
  YES -> DACH Enterprise (#13)
  NO  -> Continue

What industry?
  Fintech/Banking     -> Fintech Trust (#10)
  Healthcare/Pharma   -> HealthTech Clean (#11)
  AI/ML/Deep Tech     -> AI Frontier (#12) or Dark Premium (#8)
  DevTools/Infra      -> Terminal Green (#6) or Dark Premium (#8)
  Consumer/D2C        -> Startup Bold (#15) or Dark Botanical (#2)
  Media/Publishing    -> Paper & Ink (#5) or Notebook Tabs (#3)
  Design/Architecture -> Swiss Modern (#4)
  Sustainability/ESG  -> Cloud Dancer (#9)
  General SaaS        -> Continue

What stage/tone?
  Early stage, bold   -> Bold Signal (#1) or Startup Bold (#15)
  Series A-C, safe    -> Muted Sophistication (#7) [DEFAULT CHOICE]
  Premium positioning -> Dark Botanical (#2) or Dark Premium (#8)
  2026-trendy         -> Cloud Dancer (#9)
```

**When in doubt, use Muted Sophistication (#7).** It is the most universally appropriate preset for fundraising.
