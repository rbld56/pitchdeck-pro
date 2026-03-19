# MCP Graphics Integration Guide

Guide for integrating MCP tools to generate graphics for pitch deck slides.

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

## HuggingFace Dynamic Spaces

**When to use:** AI-generated images for backgrounds, abstract visuals, atmospheric slides. NOT for realistic photos of people.

**Available spaces (invoke via `dynamic_space`):**

| Space | Best For | Speed |
|-------|----------|-------|
| `mcp-tools/FLUX.1-Krea-dev` | High-quality hero images, product visuals | Medium |
| `mcp-tools/Qwen-Image` | Images with text placement (quotes, branding) | Medium |
| `mcp-tools/Qwen-Image-Fast` | Quick style previews, draft visuals | Fast |
| `evalstate/flux1_schnell` | Rapid idea exploration | Very Fast |
| `mcp-tools/FLUX.1-Kontext-Dev` | Edit existing images with text prompts | Medium |
| `not-lain/background-removal` | Freistellen logos/product photos | Fast |
| `prithivMLmods/Photo-Mate-i2i` | Upscaling, watermark removal, restoration | Medium |

**Usage:**
1. Call `dynamic_space` with operation: "view_parameters" to check inputs
2. Call `dynamic_space` with operation: "invoke", space_name, and parameters JSON
3. Result is an image URL or base64 — embed in HTML

**Prompting tips for image generation:**
- Always specify style matching the chosen preset: "abstract geometric shapes in deep navy and gold tones"
- For backgrounds: "atmospheric, subtle, low contrast — serves as background not focal point"
- For hero visuals: "bold, high-quality, minimal text — single concept"

**AI Image Guardrails (CRITICAL):**
- NEVER generate photorealistic team photos (instant AI-slop red flag for investors)
- NEVER generate generic stock-photo-like imagery
- PREFER: abstract art, geometric patterns, mesh gradients, atmospheric backgrounds
- ALWAYS ask user permission before generating AI images
- Generated images MUST match the preset's color palette and mood
- If image doesn't match, use `FLUX.1-Kontext-Dev` to edit colors/style

## Mermaid Chart Integration

**When to use:** Flowcharts, process diagrams, competitive matrices, timelines.

**Tool:** `validate_and_render_mermaid_diagram`

**Slide type to Mermaid diagram mapping:**

| Slide | Diagram Type | Example |
|-------|-------------|---------|
| How It Works | flowchart LR | A[Upload] --> B[Analyze] --> C[Report] |
| Business Model | flowchart TD | Revenue flow from user to platform |
| Competition | quadrantChart | Axes: ease-of-use, features |
| Timeline | timeline | Milestones Q1-Q4 |
| Architecture | flowchart | System components |
| Go-to-Market | journey | Customer journey stages |

**Embedding:** Mermaid renders to SVG. Embed the SVG code directly in HTML for perfect PDF scaling. The MCP tool validates syntax before rendering.

**Styling:** Use `%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#hex'}}}%%` to match preset colors.
