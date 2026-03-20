# Pitchdeck Pro

State-of-the-art pitch deck generator for Claude Code. Creates PDF-optimized HTML presentations with 2026 design best practices.

## Features

- **15 curated visual presets** — from VC-ready minimalism to bold consumer branding
- **VC-structure templates** — YC (10-12 slides), Sequoia (15-20), a16z (insight-driven)
- **Audience adaptation** — VC investors, B2B enterprise, board/C-level, DACH
- **Industry presets** — Fintech, HealthTech, AI/ML, SaaS, Consumer, DeepTech
- **MCP-powered graphics** — Canva infographics, Nano Banana 2 (Gemini) images, FLUX.2 photorealistic visuals, Google Whisk style-remixing
- **PDF-first** — Fixed 16:9 (1920x1080px), print-optimized CSS, works without animation
- **PPT conversion** — Convert existing .pptx files to styled web presentations
- **Anti-AI-slop** — Distinctive designs that avoid generic AI aesthetics

## Installation

```bash
# Clone the plugin
git clone <repo-url> pitchdeck-pro

# Use with Claude Code
claude --plugin-dir /path/to/pitchdeck-pro
```

Or install as a global plugin:

```bash
cp -r pitchdeck-pro ~/.claude/plugins/pitchdeck-pro
```

## Usage

```
/pitchdeck

> "Create a pitch deck for our AI healthcare startup raising Series A"
```

The skill guides you through:
1. **Content & Audience** — Who is this for? What structure?
2. **Style Discovery** — Pick from visual previews (show, don't tell)
3. **Generation** — HTML with optional Canva/HF graphics
4. **PDF Export** — Browser print or automated export

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) CLI
- For PPT conversion: Python with `python-pptx` (`pip install python-pptx`)
- For Canva graphics: Canva MCP connector configured
- For AI images (Nano Banana 2): `pip install google-genai` + `GEMINI_API_KEY` env var
- For AI images (FLUX.2): `pip install requests` + `BFL_API_KEY` env var
- For style-remixing (Google Whisk): Playwright MCP plugin configured

## Architecture

Progressive disclosure — the main SKILL.md is a concise workflow map, with supporting files loaded on-demand:

| File | Purpose | Loaded When |
|------|---------|-------------|
| `SKILL.md` | Core workflow | Always |
| `STYLE_PRESETS.md` | 15 visual presets | Phase 2 (style) |
| `SLIDE_TYPES.md` | 16 slide archetypes | Phase 3 (generation) |
| `VC_STRUCTURES.md` | VC deck templates | Phase 3 |
| `DATA_VISUALIZATION.md` | Charts, stats, metrics | Phase 3 |
| `AUDIENCE_GUIDE.md` | Audience adaptation | Phase 1, 5 |
| `ANTI_PATTERNS.md` | What to avoid | Always |
| `MCP_GRAPHICS_GUIDE.md` | Canva/NanoBanana2/FLUX.2/Whisk | Phase 3 (if graphics) |
| `slide-base.css` | PDF-optimized CSS | Phase 3 |
| `html-template.md` | HTML architecture | Phase 3 |

## License

MIT
