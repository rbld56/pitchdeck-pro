# MCP Graphics Integration Guide

Guide for integrating MCP tools and AI image generation scripts for pitch deck slides.

## Canva MCP Integration

**When to use:** Infographics, professional charts, data visualizations, poster-style slide graphics.

**Available tools:**
- `generate-design` — Generate infographic (type: infographic), poster (type: poster), report (type: report)
- `generate-design-structured` — Full Canva presentation (type: presentation). Requires `request-outline-review` first
- `export-design` — Export to PDF, PNG, JPG. Use PNG for embedding in HTML
- `upload-asset-from-url` — Upload user logos/images into Canva
- `list-brand-kits` — Load user's brand identity for consistent design
- `create-design-from-candidate` — Convert AI-generated candidate to editable design
- `start-editing-transaction` + `perform-editing-operations` — Edit generated designs

**Asset Pipeline (for HTML-first path):**
1. Identify slides needing generated graphics (Market Size, How It Works, Traction)
2. Call `generate-design` with design_type + descriptive query including brand colors
3. Present candidates to user (thumbnails are returned)
4. User picks → `create-design-from-candidate` with job_id + candidate_id
5. `export-design` format: {type: "png", width: 1920} → get download URL
6. Download PNG and embed in HTML as `<img>` with file path or base64

**Prompting tips for Canva:**
- Include brand colors in the query: "...using dark navy (#0A1628) and gold (#C9A84C) accent"
- Specify the data: "Show TAM $50B, SAM $8B, SOM $1.2B as concentric circles"
- Request style: "Modern, minimal infographic style, no clip art"

### Canva-Native Path (full presentation in Canva)
1. Build slide outline from VC_STRUCTURES.md
2. Call `request-outline-review` with presentation_outlines array
3. User reviews and approves in Canva widget
4. Call `generate-design-structured` with approved outline + style + audience
5. User edits in Canva
6. `export-design` format: {type: "pdf"}

---

## Nano Banana 2 (Gemini 3.1 Flash Image Preview)

**When to use:** Hero images, product visuals, text-on-image graphics, atmospheric backgrounds, quick style mockups. Best for speed, cost-efficiency, and precise text rendering in images.

**Model:** `gemini-2.0-flash-preview-image-generation` via Google Gemini API

**Requires:** `GEMINI_API_KEY` environment variable (get from [AI Studio](https://aistudio.google.com/))

**How to invoke:**
```bash
python scripts/generate-image-nanobanana.py --prompt "abstract medical AI visualization, blue tones, minimal" --output assets/hero.png
```

**Parameters:**
| Flag | Description | Default |
|------|-------------|---------|
| `--prompt` | Image generation prompt (required) | — |
| `--output` | Output file path (required) | — |
| `--reference-image` | Path to reference image for style guidance (optional, up to 14) | — |
| `--aspect-ratio` | Aspect ratio: `16:9`, `1:1`, `4:3`, `9:16` | `16:9` |

**Strengths:**
- Fast generation (~2-5 seconds)
- Cost-effective (significantly cheaper than FLUX.2 Pro)
- Excellent text rendering in images (logos, quotes, branded text)
- Supports up to 14 reference images for style/content guidance
- Good for iterative exploration (generate many variants quickly)

**Best for these slide types:**
| Slide Type | Prompt Strategy |
|-----------|----------------|
| Cover/Hero | "atmospheric [industry] visualization, [preset colors], minimal, premium" |
| Problem | "dark, dramatic visual representing [pain point], [preset dark tones]" |
| Solution | "bright, clean product visualization, [brand colors], modern" |
| Vision | "futuristic, aspirational [industry] scene, [accent color] highlights" |
| Breathing Room | "abstract texture, [preset palette], subtle, background-quality" |

**Prompting tips:**
- Always include preset colors: "...in deep navy (#0A1628) and warm gold (#C9A84C) tones"
- Specify purpose: "serves as slide background, not focal point — low contrast, atmospheric"
- For text-on-image: "include text '[Your Text]' in clean sans-serif font, centered"
- Reference images: Use for style consistency across multiple slides

---

## FLUX.2 (Black Forest Labs API)

**When to use:** Photorealistic images, complex compositions with accurate hands/faces, high-detail product renders, cinematic visuals. Best quality for hero visuals where realism matters.

**Models:** `flux-pro-1.1` (best quality), `flux-dev` (good quality, cheaper), `flux-schnell` (fast drafts)

**Requires:** `BFL_API_KEY` environment variable (get from [BFL API](https://docs.bfl.ai/))

**How to invoke:**
```bash
python scripts/generate-image-flux.py --prompt "modern hospital corridor, cinematic lighting, clean architecture" --model pro --output assets/visual.png
```

**Parameters:**
| Flag | Description | Default |
|------|-------------|---------|
| `--prompt` | Image generation prompt (required) | — |
| `--output` | Output file path (required) | — |
| `--model` | Model tier: `pro`, `dev`, `schnell` | `pro` |
| `--width` | Image width in pixels | `1920` |
| `--height` | Image height in pixels | `1080` |

**Strengths:**
- Best-in-class photorealistic quality
- Accurate hands, faces, and complex anatomy
- Excellent at cinematic/architectural compositions
- Multiple quality tiers for budget flexibility

**Model selection guide:**
| Model | Quality | Speed | Cost | Use When |
|-------|---------|-------|------|----------|
| `pro` (flux-pro-1.1) | Highest | ~10-15s | $$$ | Final hero visuals, cover slides |
| `dev` | High | ~5-8s | $$ | Good-quality visuals, most slides |
| `schnell` | Good | ~2-3s | $ | Quick drafts, style exploration |

**Best for these slide types:**
| Slide Type | Prompt Strategy |
|-----------|----------------|
| Cover/Hero | "cinematic [industry scene], professional, [preset mood], 16:9 composition" |
| Product | "clean product photography, [product description], studio lighting" |
| Team (abstract) | "professional workspace, diverse team silhouettes, [brand colors]" |
| Market | "aerial view of [market/city], scale and opportunity, [preset tones]" |

**Prompting tips:**
- Specify composition: "16:9 landscape, subject on left third, negative space on right for text overlay"
- Include lighting: "soft studio lighting", "golden hour", "cinematic blue tones"
- For backgrounds: append "shallow depth of field, bokeh background" for text-overlay-friendly results
- NEVER request photorealistic individual faces for team slides (AI-slop red flag)

---

## Google Whisk (Browser-Automation)

**When to use:** Creative style remixing — combine a subject, scene, and style from separate reference images into a new composition. Unique capability not available via API. Best for artistic/creative visuals.

**Tool:** Google Whisk at `https://labs.google/fx/tools/whisk` (uses Gemini + Imagen 3 internally)

**Requires:** Playwright MCP browser tools + active Google account login in the browser session

**How it works:**
Whisk takes up to 3 image inputs:
1. **Subject** — What to depict (e.g., your product, logo, mascot)
2. **Scene** — Where/context (e.g., futuristic lab, city skyline, nature)
3. **Style** — Visual style reference (e.g., watercolor, 3D render, line art)

It remixes them into a new image combining all three aspects.

**Workflow (automated via Playwright):**
```
1. browser_navigate → https://labs.google/fx/tools/whisk
2. browser_wait_for → page loaded
3. browser_snapshot → identify upload areas
4. browser_file_upload → upload Subject image
5. browser_file_upload → upload Scene image (optional)
6. browser_file_upload → upload Style image (optional)
7. browser_click → "Generate" / "Remix" button
8. browser_wait_for → result generated
9. browser_take_screenshot → capture result
10. browser_click → download result
```

**Limitations:**
- No official API — requires browser automation
- Requires active Google account session
- Generation can take 10-30 seconds
- Results are less predictable than prompt-based tools
- May require multiple attempts for desired result

**Best for these slide types:**
| Slide Type | Subject | Scene | Style |
|-----------|---------|-------|-------|
| Cover | Product logo | Industry backdrop | Preset's visual mood |
| Vision | Abstract concept | Futuristic scene | Artistic/painterly |
| Breathing Room | Brand element | Atmospheric scene | Watercolor/sketch |
| ESG/Mission | Impact symbol | Nature/community | Warm, human |

**When NOT to use Whisk:**
- When you need text in images (use NanoBanana2 instead)
- When you need precise photorealism (use FLUX.2 instead)
- When speed matters (use NanoBanana2 schnell)
- When no reference images are available (use prompt-based tools)

---

## AI Image Guardrails (CRITICAL — applies to ALL tools)

- **NEVER** generate photorealistic team photos (instant AI-slop red flag for investors)
- **NEVER** generate generic stock-photo-like imagery
- **PREFER:** abstract art, geometric patterns, mesh gradients, atmospheric backgrounds
- **ALWAYS** ask user permission before generating AI images
- Generated images **MUST** match the preset's color palette and mood
- Include preset colors in every prompt for visual consistency
- For slide backgrounds: ensure low contrast so overlaid text remains readable

## Tool Selection Quick Reference

| Need | Best Tool | Why |
|------|-----------|-----|
| Fast background/texture | NanoBanana2 | Speed + cost |
| Text in image | NanoBanana2 | Best text rendering |
| Photorealistic hero | FLUX.2 Pro | Best quality |
| Quick draft/exploration | FLUX.2 Schnell or NanoBanana2 | Speed |
| Style remix from references | Whisk | Unique capability |
| Infographic/chart | Canva | Professional templates |
| Data visualization | Canva or CSS/SVG inline | Control + consistency |
| Diagrams/flowcharts | CSS/SVG inline | No external dependency |
