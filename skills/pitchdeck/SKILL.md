---
name: pitchdeck
version: 1.0.0
description: Activate when the user wants to create a pitch deck, build investor slides, design a fundraising presentation, make a board deck, convert a PowerPoint to a modern pitch, or generate a startup presentation. Covers VC-structure templates (YC, Sequoia, a16z), 15 industry-specific design presets, and MCP-powered graphics via Canva, Nano Banana 2 (Gemini), FLUX.2, and Google Whisk. Outputs PDF-ready single-file HTML with 2026 design standards.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion, WebFetch, mcp__claude_ai_Canva__generate-design, mcp__claude_ai_Canva__generate-design-structured, mcp__claude_ai_Canva__request-outline-review, mcp__claude_ai_Canva__create-design-from-candidate, mcp__claude_ai_Canva__export-design, mcp__claude_ai_Canva__upload-asset-from-url, mcp__claude_ai_Canva__list-brand-kits, mcp__claude_ai_Canva__start-editing-transaction, mcp__claude_ai_Canva__perform-editing-operations, mcp__claude_ai_Canva__commit-editing-transaction, mcp__claude_ai_Canva__get-assets, mcp__claude_ai_Canva__get-design, mcp__claude_ai_Canva__get-design-pages, mcp__claude_ai_Canva__get-export-formats, mcp__plugin_playwright_playwright__browser_navigate, mcp__plugin_playwright_playwright__browser_click, mcp__plugin_playwright_playwright__browser_snapshot, mcp__plugin_playwright_playwright__browser_file_upload, mcp__plugin_playwright_playwright__browser_take_screenshot, mcp__plugin_playwright_playwright__browser_wait_for
---

# Pitchdeck Pro

Generate PDF-optimized pitch decks with 2026 design standards. Single-file HTML -> PDF export.

**Note:** MCP tools (Canva) and scripts (NanoBanana2, FLUX.2) in `allowed-tools` are optional. The plugin works fully with HTML/CSS-only generation. MCP graphics and AI image scripts are only used when the corresponding API keys/connectors are configured AND the user opts in during Phase 1. Google Whisk requires Playwright browser automation.

## Core Principles
1. **Dual-Mode** -- PDF (fixed 16:9, print-ready, static) OR HTML Interactive (responsive, animated, scroll-nav)
2. **150-Second Rule** -- Investors spend <=150 seconds. Every slide passes the "Icon-and-Number" test (viewer should grasp the slide from title, one key icon, and one isolated metric alone)
3. **Anti-AI-Slop** -- Distinctive, human-crafted aesthetics. See [ANTI_PATTERNS.md](references/ANTI_PATTERNS.md)
4. **Show, Don't Tell** -- Generate visual previews for style discovery, don't ask abstract questions

## NON-NEGOTIABLE RULES

Violating ANY of these produces unacceptable output. These rules are absolute and apply to BOTH modes.

### Font Sizes

**PDF Mode (1920x1080px fixed):**
- Hero/metric numbers: **96-120px**
- Slide titles (h2): **56-72px**
- Body text, bullets, table cells: **32px**
- Labels, captions, sources: **24px**
- **NOTHING below 20px. Ever.**

**HTML Interactive Mode (viewport-responsive):**
- Hero/metric numbers: **clamp(3rem, 8vw, 7.5rem)**
- Slide titles (h2): **clamp(1.75rem, 4vw, 3.5rem)**
- Body text: **clamp(0.95rem, 1.5vw, 1.5rem)**
- Labels/captions: **clamp(0.7rem, 1vw, 0.95rem)**
- All sizes via `clamp()` — responsive but never unreadable

### CSS Architecture (both modes)
- **MUST** copy the chosen preset's ENTIRE `:root` block from [STYLE_PRESETS.md](references/STYLE_PRESETS.md) into `<style>`
- **PDF Mode:** Include FULL [slide-base.css](templates/slide-base.css) (fixed 1920x1080, @media print)
- **HTML Mode:** Include FULL [slide-base-html.css](templates/slide-base-html.css) (viewport, scroll-snap, animations)
- **MUST** use `--color-*` CSS variables from the preset for ALL colors — never hardcoded hex in HTML
- **MUST** use CSS classes from [SLIDE_TYPES.md](references/SLIDE_TYPES.md) — NOT inline `style=""` attributes
- Inline `style=""` is **FORBIDDEN** except for one-off positioning (top/left) or chart bar widths
- Every slide **MUST** have `class="slide [type]-slide"` (e.g., `class="slide cover-slide"`)

### Visual Quality (both modes)
- **NEVER** use `#FFFFFF` as background. Use the preset's `--color-bg` (off-white/dark)
- **NEVER** use `#000000` as text. Use `--color-text-primary` (near-black)
- **MUST** use 2 fonts: Display font for headlines + Body font for text (from the preset's font pairing)
- **MUST** include at least 1 atmospheric element per deck (gradient mesh, noise texture, or CSS decorative shape)
- **MUST** include breathing room slides (quote, single stat, or section divider) every 3-4 content slides
- Accent color used consistently on key metrics and CTAs only — not on every element

### HTML Mode Specific
- Animations are **EXPECTED and REQUIRED** — not optional. Use reveal, scale, stagger, counter animations
- **MUST** include scroll-snap navigation (keyboard + wheel + touch)
- **MUST** include progress bar (scroll-linked) + nav dots
- **MUST** include `prefers-reduced-motion` support
- Read [animation-patterns.md](templates/animation-patterns.md) for available animation classes
- Viewport fitting: every slide `height: 100vh; height: 100dvh; overflow: hidden`
- Responsive breakpoints for height (700px, 600px, 500px) and width (600px)

### Content Density (both modes)
- Max **30 words** body text per slide (presenter mode) / **75 words** (async/PDF)
- Max **6 bullet points** per slide
- If content exceeds limits: **SPLIT into multiple slides**, never cram
- One core idea per slide — the "Icon-and-Number" test must pass

---

## Phase 0: Detect Mode

Determine what the user wants:
- **Mode A: New Pitch Deck** -> Phase 1
- **Mode B: PPT Conversion** -> Phase 4
- **Mode C: Enhancement** -> Read existing HTML deck, analyze against [ANTI_PATTERNS.md](references/ANTI_PATTERNS.md) and design standards, identify issues (layout, typography, density, narrative arc), propose specific improvements, then apply changes with user approval. Skip to Phase 3 with the existing file as base.

---

## Phase 1: Content & Audience Discovery

**Ask ALL questions in a single AskUserQuestion call:**

1. **Audience** (header: "Audience"): VC Investor / B2B Enterprise / Board/C-Level / General
2. **Industry** (header: "Industry"): AI/ML / Fintech / HealthTech / SaaS / Consumer / DeepTech / Other
3. **Structure** (header: "Structure"): YC (10-12 slides) / Sequoia (15-20) / a16z (Insight-driven) / Custom
4. **Content** (header: "Content"): All content ready / Rough notes / Topic only — if "Topic only", generate content suggestions and draft slide text before proceeding to Phase 2
5. **Output Mode** (header: "Mode"): PDF (print-optimized, fixed dimensions, static — for investor email, DocSend) / HTML Interactive (animated, scroll-nav, responsive — for live demo, website, screen-share)
6. **Generation Path** (header: "Path"): HTML-generated (default) / Canva-Native / Hybrid (recommended)
7. **AI Graphics** (header: "Graphics"): Yes (Canva + NanoBanana2/FLUX.2/Whisk for visuals) / Canva only / AI Scripts only (NanoBanana2/FLUX.2) / CSS/SVG only / None

If user has content, ask them to share it. If they selected Canva-Native or Hybrid with Brand Kit, call `list-brand-kits`. If AI Scripts selected, verify `GEMINI_API_KEY` and/or `BFL_API_KEY` are set.

**Remember choices -- they control which reference files and MCP tools are loaded in later phases.**

### Image Evaluation (if images provided)
1. Scan all images provided by user
2. Evaluate each: usable/not usable, dominant colors, what it represents
3. Co-design the outline around text AND images together
4. If logo found, embed in style previews (Phase 2)

---

## Phase 2: Style Discovery

Read [STYLE_PRESETS.md](references/STYLE_PRESETS.md) for all available presets.

### Step 2.0: Style Path
Ask: "Show me options" (recommended) / "I know what I want" (pick from preset list)

### Step 2.1: Mood Selection (if guided)
Ask (multiSelect, max 2): Impressed/Confident / Excited/Energized / Calm/Focused / Inspired/Moved

Audience influences preset recommendation:
- VC -> Muted Sophistication, Cloud Dancer, Dark Premium
- B2B Enterprise -> DACH Enterprise, Fintech Trust, HealthTech Clean
- Board -> Board Executive, Muted Sophistication

### Step 2.2: Generate 3 Style Previews
Based on mood + audience + industry, generate 3 single-slide HTML previews. Save to `.claude-design/slide-previews/`. Open each automatically.

If AI Graphics enabled: optionally use `generate-image-nanobanana.py` for quick atmospheric mockups in previews (fast, cheap).

### Step 2.3: User Picks
Ask which preview they prefer. If "Mix elements", ask specifics.

---

## Phase 3: Generate Pitch Deck

Read these files before generating:
- [SLIDE_TYPES.md](references/SLIDE_TYPES.md) -- Slide archetypes with HTML/CSS templates
- [VC_STRUCTURES.md](references/VC_STRUCTURES.md) -- Chosen VC template slide order
- **PDF Mode:** [slide-base.css](templates/slide-base.css) -- Fixed 1920x1080, @media print
- **HTML Mode:** [slide-base-html.css](templates/slide-base-html.css) -- Viewport, scroll-snap, animations
- [html-template.md](templates/html-template.md) -- HTML architecture + JS (has examples for BOTH modes)
- [DATA_VISUALIZATION.md](references/DATA_VISUALIZATION.md) -- Chart and stat card patterns
- [AUDIENCE_GUIDE.md](references/AUDIENCE_GUIDE.md) -- Audience-specific adaptations
- **HTML Mode:** [animation-patterns.md](templates/animation-patterns.md) -- Full animation reference (REQUIRED)
- [MCP_GRAPHICS_GUIDE.md](references/MCP_GRAPHICS_GUIDE.md) -- If using MCP graphics

### Generation Paths

**Path A: HTML->PDF (default)**
Generate single-file HTML with fixed 16:9 dimensions. Include @media print CSS. If AI graphics enabled, generate Canva infographics / NanoBanana2/FLUX.2 images for specific slides and embed as assets.

**Path B: Canva-Native**
Use `request-outline-review` with slide outline -> user reviews -> `generate-design-structured` -> user edits in Canva -> `export-design` (pdf).

**Path C: Hybrid (recommended)**
Generate HTML skeleton for layout control. For complex slides (Market Size, How It Works, Traction), generate Canva infographics via `generate-design` and embed exported PNGs. Use NanoBanana2/FLUX.2 for atmospheric backgrounds and hero visuals. Use Google Whisk for style-remixed visuals. Diagrams are built as inline CSS/SVG.

### MCP Asset Pipeline (Paths A & C)
1. Analyze which slides need generated graphics
2. For infographics/charts: `generate-design` (type: infographic/report) -> user picks candidate -> `create-design-from-candidate` -> `export-design` (png) -> embed in HTML
3. For AI images (hero, backgrounds, product visuals): `python scripts/generate-image-nanobanana.py` (fast, good text rendering) or `python scripts/generate-image-flux.py` (photorealistic quality) -> embed result PNG
4. For style-remixed visuals: Google Whisk via Playwright browser automation (navigate to labs.google/fx/tools/whisk, upload subject/scene/style images, download result)
5. For diagrams: Build as inline CSS/SVG within the HTML (no external tool needed)
6. For logos: Ask user to provide transparent PNG, or use CSS background-removal techniques

### Key Requirements
- Single self-contained HTML file, all CSS/JS inline
- Include FULL contents of slide-base.css in the style block
- Copy the chosen preset's ENTIRE :root block (do NOT invent your own CSS variables)
- Fonts via Google Fonts @import — use BOTH the Display and Body font from the preset
- Every section: clear `/* === SECTION NAME === */` comment
- Design must work statically (no JS dependencies for layout)
- Use CSS classes from SLIDE_TYPES.md for every slide — no inline style soup

### Generation Checklist (verify BEFORE writing the HTML file)
Before outputting, mentally verify EVERY slide against these 5 checks:
1. **Font check:** Is the smallest text on this slide >= 20px? Are titles >= 56px?
2. **Class check:** Does this slide use CSS classes (not inline styles)?
3. **Variable check:** Does this slide use `--color-*` variables from the preset?
4. **Density check:** Is there <= 30 words of body text? <= 6 bullets?
5. **Investor check:** Would an investor grasp this slide in 5 seconds?
If ANY check fails, fix it before generating.

---

## Phase 4: PPT Conversion

Requires: `pip install python-pptx` (install if not available)

1. Run `python scripts/extract-pptx.py <input.pptx> <output_dir>`
2. Confirm extracted content with user
3. Proceed to Phase 2 for style selection
4. Generate in chosen style, preserving all content

---

## Phase 5: Delivery

### PDF Mode Delivery:
1. Open HTML preview in browser (scaling via transform)
2. **PDF Export:** Browser: File -> Print -> Save as PDF (landscape, no margins)
3. Alternative: Canva `export-design` (pdf) or `npx playwright pdf`

### HTML Interactive Mode Delivery:
1. Open in browser — this IS the final product
2. Verify: scroll-snap navigation, animations, responsive resize, nav dots, progress bar
3. Test keyboard (arrows, space), mouse wheel, and touch swipe
4. Test `prefers-reduced-motion` (animations should disable gracefully)

### Both Modes:
5. Clean up `.claude-design/slide-previews/` if exists
6. Show Pre-Send Checklist -- see [AUDIENCE_GUIDE.md](references/AUDIENCE_GUIDE.md)
7. Summarize: file location, style, slide count, mode, navigation instructions

---

## Supporting Files

| File | Purpose | When to Read |
|------|---------|-------------|
| [STYLE_PRESETS.md](references/STYLE_PRESETS.md) | 15 curated visual presets | Phase 2 |
| [SLIDE_TYPES.md](references/SLIDE_TYPES.md) | 16 slide archetypes with HTML/CSS | Phase 3 |
| [VC_STRUCTURES.md](references/VC_STRUCTURES.md) | YC/Sequoia/a16z templates | Phase 3 |
| [DATA_VISUALIZATION.md](references/DATA_VISUALIZATION.md) | Charts, stat cards, metrics | Phase 3 |
| [AUDIENCE_GUIDE.md](references/AUDIENCE_GUIDE.md) | VC vs B2B vs Board adaptation | Phase 1, 5 |
| [ANTI_PATTERNS.md](references/ANTI_PATTERNS.md) | AI-slop avoidance guide | Always |
| [MCP_GRAPHICS_GUIDE.md](references/MCP_GRAPHICS_GUIDE.md) | Canva/NanoBanana2/FLUX.2/Whisk integration | Phase 3 (if graphics) |
| [slide-base.css](templates/slide-base.css) | PDF mode CSS base (fixed 1920x1080) | Phase 3 (PDF) |
| [slide-base-html.css](templates/slide-base-html.css) | HTML mode CSS base (viewport, scroll-snap, animations) | Phase 3 (HTML) |
| [html-template.md](templates/html-template.md) | HTML architecture + JS (both modes) | Phase 3 |
| [animation-patterns.md](templates/animation-patterns.md) | Animation reference (required for HTML mode) | Phase 3 (HTML) |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | PPT extraction | Phase 4 |
