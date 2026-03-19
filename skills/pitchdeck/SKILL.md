---
name: pitchdeck
version: 1.0.0
description: Activate when the user wants to create a pitch deck, build investor slides, design a fundraising presentation, make a board deck, convert a PowerPoint to a modern pitch, or generate a startup presentation. Covers VC-structure templates (YC, Sequoia, a16z), 15 industry-specific design presets, and MCP-powered graphics via Canva, HuggingFace, and Mermaid. Outputs PDF-ready single-file HTML with 2026 design standards.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion, WebFetch, mcp__claude_ai_Canva__generate-design, mcp__claude_ai_Canva__generate-design-structured, mcp__claude_ai_Canva__request-outline-review, mcp__claude_ai_Canva__create-design-from-candidate, mcp__claude_ai_Canva__export-design, mcp__claude_ai_Canva__upload-asset-from-url, mcp__claude_ai_Canva__list-brand-kits, mcp__claude_ai_Canva__start-editing-transaction, mcp__claude_ai_Canva__perform-editing-operations, mcp__claude_ai_Canva__commit-editing-transaction, mcp__claude_ai_Canva__get-assets, mcp__claude_ai_Canva__get-design, mcp__claude_ai_Canva__get-design-pages, mcp__claude_ai_Canva__get-export-formats, mcp__claude_ai_Hugging_Face__dynamic_space, mcp__claude_ai_Hugging_Face__space_search, mcp__claude_ai_Mermaid_Chart__validate_and_render_mermaid_diagram
---

# Pitchdeck Pro

Generate PDF-optimized pitch decks with 2026 design standards. Single-file HTML -> PDF export.

**Note:** MCP tools (Canva, HuggingFace, Mermaid) in `allowed-tools` are optional. The plugin works fully with HTML/CSS-only generation. MCP graphics are only used when the corresponding connectors are configured AND the user opts in during Phase 1.

## Core Principles
1. **PDF-First** -- Fixed 16:9 (1920x1080px), @media print, design must work without animation
2. **150-Second Rule** -- Investors spend <=150 seconds. Every slide passes the "Icon-and-Number" test (viewer should grasp the slide from title, one key icon, and one isolated metric alone)
3. **Anti-AI-Slop** -- Distinctive, human-crafted aesthetics. See [ANTI_PATTERNS.md](references/ANTI_PATTERNS.md)
4. **Show, Don't Tell** -- Generate visual previews for style discovery, don't ask abstract questions

## Design Standards (2026)
- Body text: minimum 24pt. Headlines: 44-64pt
- Maximum 2 fonts per deck (Display + Body)
- AA contrast compliance (4.5:1 body, 3:1 headlines)
- One idea per slide, max 30 words body text
- Breathing room slides every 3-4 content slides
- Content density limits per slide type -- see [SLIDE_TYPES.md](references/SLIDE_TYPES.md)

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
5. **Generation Path** (header: "Path"): HTML->PDF (default) / Canva-Native / Hybrid (recommended)
6. **AI Graphics** (header: "Graphics"): Yes (Canva + HF for visuals) / Canva only / CSS/SVG only / None

If user has content, ask them to share it. If they selected Canva-Native or Hybrid with Brand Kit, call `list-brand-kits`.

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

If AI Graphics enabled: optionally use `mcp-tools/Qwen-Image-Fast` for quick atmospheric mockups in previews.

### Step 2.3: User Picks
Ask which preview they prefer. If "Mix elements", ask specifics.

---

## Phase 3: Generate Pitch Deck

Read these files before generating:
- [SLIDE_TYPES.md](references/SLIDE_TYPES.md) -- Slide archetypes with HTML/CSS templates
- [VC_STRUCTURES.md](references/VC_STRUCTURES.md) -- Chosen VC template slide order
- [slide-base.css](templates/slide-base.css) -- Mandatory PDF-optimized CSS base
- [html-template.md](templates/html-template.md) -- HTML architecture and JS
- [DATA_VISUALIZATION.md](references/DATA_VISUALIZATION.md) -- Chart and stat card patterns
- [AUDIENCE_GUIDE.md](references/AUDIENCE_GUIDE.md) -- Audience-specific adaptations
- [MCP_GRAPHICS_GUIDE.md](references/MCP_GRAPHICS_GUIDE.md) -- If using MCP graphics

### Generation Paths

**Path A: HTML->PDF (default)**
Generate single-file HTML with fixed 16:9 dimensions. Include @media print CSS. If AI graphics enabled, generate Canva infographics / HF images for specific slides and embed as assets.

**Path B: Canva-Native**
Use `request-outline-review` with slide outline -> user reviews -> `generate-design-structured` -> user edits in Canva -> `export-design` (pdf).

**Path C: Hybrid (recommended)**
Generate HTML skeleton for layout control. For complex slides (Market Size, How It Works, Traction), generate Canva infographics via `generate-design` and embed exported PNGs. Use HF Spaces for atmospheric backgrounds. Use Mermaid for flowcharts/diagrams.

### MCP Asset Pipeline (Paths A & C)
1. Analyze which slides need generated graphics
2. For infographics/charts: `generate-design` (type: infographic/report) -> user picks candidate -> `create-design-from-candidate` -> `export-design` (png) -> embed in HTML
3. For AI images: `dynamic_space` invoke (FLUX.1-Krea-dev or Qwen-Image) -> embed result
4. For diagrams: `validate_and_render_mermaid_diagram` -> embed SVG
5. For logos: `not-lain/background-removal` if needed

### Key Requirements
- Single self-contained HTML file, all CSS/JS inline
- Include FULL contents of slide-base.css in the style block
- Fonts via Google Fonts @import (never system fonts)
- Every section: clear `/* === SECTION NAME === */` comment
- Design must work statically (no JS dependencies for layout)

---

## Phase 4: PPT Conversion

Requires: `pip install python-pptx` (install if not available)

1. Run `python scripts/extract-pptx.py <input.pptx> <output_dir>`
2. Confirm extracted content with user
3. Proceed to Phase 2 for style selection
4. Generate in chosen style, preserving all content

---

## Phase 5: Delivery

1. Open HTML preview in browser
2. **PDF Export options:**
   - Browser: File -> Print -> Save as PDF (landscape, no margins)
   - If Canva-Native: `export-design` (format: pdf)
   - Script: `npx playwright pdf` or browser automation
3. Clean up `.claude-design/slide-previews/` if exists
4. Show Pre-Send Checklist -- see [AUDIENCE_GUIDE.md](references/AUDIENCE_GUIDE.md)
5. Summarize: file location, style, slide count, export instructions

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
| [MCP_GRAPHICS_GUIDE.md](references/MCP_GRAPHICS_GUIDE.md) | Canva/HF/Mermaid integration | Phase 3 (if graphics) |
| [slide-base.css](templates/slide-base.css) | Mandatory CSS base | Phase 3 |
| [html-template.md](templates/html-template.md) | HTML architecture + JS | Phase 3 |
| [animation-patterns.md](templates/animation-patterns.md) | Optional CSS animations | Phase 3 (HTML only) |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | PPT extraction | Phase 4 |
