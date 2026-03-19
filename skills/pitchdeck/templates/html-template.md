# HTML Presentation Template (PDF-Optimized)

**CRITICAL: This is your working example.** Copy this structure as your base. Extend with more slides. Do NOT start from scratch. Do NOT use inline `style=""` attributes. Do NOT invent your own CSS variables.

## Complete Working Example: 3 Slides

This example uses the "HealthTech Clean" preset. When generating, replace the `:root` variables with the user's chosen preset from STYLE_PRESETS.md.

```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Company Name — Pitch Deck</title>

<style>
/* === FONT IMPORTS (from preset) === */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* === THEME: HealthTech Clean (from STYLE_PRESETS.md) ===
   Replace this ENTIRE :root block with the chosen preset */
:root {
    /* Surface colors */
    --color-bg: #F8FAFB;
    --color-surface: #FFFFFF;
    --color-surface-elevated: #FFFFFF;

    /* Text colors */
    --color-text-primary: #1A202C;
    --color-text-secondary: #718096;
    --color-text-on-accent: #FFFFFF;
    --color-text-muted: #A0AEC0;

    /* Accent colors */
    --color-accent: #2B6CB0;
    --color-accent-hover: #2C5282;
    --color-accent-muted: rgba(43, 108, 176, 0.12);
    --color-success: #38A169;
    --color-success-muted: rgba(56, 161, 105, 0.12);
    --color-danger: #E53E3E;

    /* Borders & dividers */
    --color-border: #E2E8F0;
    --color-divider: #EDF2F7;

    /* Typography — FIXED px for PDF */
    --font-display: 'Plus Jakarta Sans', sans-serif;
    --font-body: 'Plus Jakarta Sans', sans-serif;
    --title-size: 64px;
    --h2-size: 56px;
    --h3-size: 42px;
    --body-size: 32px;
    --small-size: 24px;
    --caption-size: 20px;
    --hero-number-size: 112px;
    --stat-number-size: 72px;

    /* Spacing */
    --slide-padding: 80px;
    --content-gap: 40px;
    --element-gap: 24px;

    /* Shadows */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 32px rgba(0,0,0,0.1);

    /* Border radius */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;

    /* Animation (HTML preview only) */
    --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
    --duration-normal: 0.6s;
}

/* === RESET === */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* === PASTE FULL slide-base.css HERE === */
@page { size: 1920px 1080px; margin: 0; }
html, body { width: 1920px; height: 100%; overflow: hidden; -webkit-font-smoothing: antialiased; }
body { transform-origin: top left; font-family: var(--font-body); color: var(--color-text-primary); background: #CBD5E0; }

.slide {
    width: 1920px; height: 1080px; overflow: hidden; position: relative;
    display: flex; flex-direction: column;
    background: var(--color-bg);
    page-break-after: always; page-break-inside: avoid;
}

.slide-content {
    flex: 1; display: flex; flex-direction: column; justify-content: center;
    max-height: 100%; overflow: hidden; padding: var(--slide-padding);
}

/* === TYPOGRAPHY === */
.section-label {
    font-size: var(--caption-size);
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--color-accent);
    margin-bottom: 12px;
}

.slide-title {
    font-family: var(--font-display);
    font-size: var(--h2-size);
    font-weight: 800;
    color: var(--color-text-primary);
    line-height: 1.15;
    letter-spacing: -0.02em;
    margin-bottom: 16px;
}

.slide-subtitle {
    font-size: var(--body-size);
    font-weight: 400;
    color: var(--color-text-secondary);
    line-height: 1.5;
    margin-bottom: var(--content-gap);
}

/* === STAT CARDS === */
.stat-card {
    text-align: center;
    padding: 32px;
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
}

.stat-number {
    font-family: var(--font-display);
    font-size: var(--stat-number-size);
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1;
    color: var(--color-accent);
}

.stat-label {
    font-size: var(--small-size);
    font-weight: 500;
    color: var(--color-text-secondary);
    margin-top: 12px;
}

/* === HERO NUMBER (full-slide metric) === */
.hero-number {
    font-family: var(--font-display);
    font-size: var(--hero-number-size);
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1;
    color: var(--color-accent);
}

.hero-context {
    font-size: var(--body-size);
    color: var(--color-text-secondary);
    margin-top: 16px;
}

/* === LAYOUTS === */
.split { display: flex; height: 100%; gap: var(--content-gap); }
.split-60-40 .split-left { flex: 0 0 1080px; }
.split-60-40 .split-right { flex: 0 0 680px; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--element-gap); }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--element-gap); }

/* === BULLET LIST === */
.bullet-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.bullet-list li {
    font-size: var(--body-size);
    color: var(--color-text-primary);
    line-height: 1.5;
    padding-left: 32px;
    position: relative;
}
.bullet-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 14px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--color-accent);
}

/* === ACCENT LINE (decorative) === */
.accent-line {
    width: 56px;
    height: 4px;
    background: var(--color-accent);
    border-radius: 2px;
    margin-bottom: 16px;
}

/* === ATMOSPHERIC BACKGROUND === */
.atmospheric-bg::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at 15% 85%, var(--color-accent-muted) 0%, transparent 50%),
        radial-gradient(ellipse at 85% 15%, var(--color-success-muted) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}
.atmospheric-bg > * { position: relative; z-index: 1; }

/* === COMPLIANCE FOOTER === */
.slide-footer {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--slide-padding);
    font-size: var(--caption-size);
    color: var(--color-text-muted);
    border-top: 1px solid var(--color-divider);
    background: var(--color-surface);
}

/* === CERT BADGES === */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 20px;
    border-radius: 100px;
    background: var(--color-success-muted);
    font-size: var(--small-size);
    font-weight: 600;
    color: var(--color-success);
}
.badge::before {
    content: '';
    width: 10px; height: 10px;
    border-radius: 50%;
    background: currentColor;
}

/* === REVEAL ANIMATIONS (HTML preview only) === */
.reveal {
    opacity: 0; transform: translateY(24px);
    transition: opacity var(--duration-normal) var(--ease-out-expo),
                transform var(--duration-normal) var(--ease-out-expo);
}
.slide.visible .reveal { opacity: 1; transform: translateY(0); }
.reveal:nth-child(1) { transition-delay: 0.1s; }
.reveal:nth-child(2) { transition-delay: 0.2s; }
.reveal:nth-child(3) { transition-delay: 0.3s; }
.reveal:nth-child(4) { transition-delay: 0.4s; }

/* === PRINT === */
@media print {
    body { background: white; transform: none !important; }
    .slide { page-break-after: always; break-after: page; break-inside: avoid; }
    .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
    .nav-dots, .progress-bar { display: none !important; }
    * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
}

@media (prefers-reduced-motion: reduce) {
    .reveal { opacity: 1; transform: none; transition: none; }
}
</style>
</head>
<body>

<!-- ==========================================================
     SLIDE 1: COVER
     ========================================================== -->
<section class="slide cover-slide atmospheric-bg">
    <div class="slide-content" style="align-items: center; text-align: center;">

        <!-- Logo mark (CSS-only) -->
        <div class="reveal" style="width: 88px; height: 88px; border-radius: var(--radius-lg); background: var(--color-accent); display: flex; align-items: center; justify-content: center; margin-bottom: 40px; box-shadow: var(--shadow-lg);">
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none">
                <circle cx="20" cy="20" r="16" stroke="white" stroke-width="2.5" fill="none"/>
                <circle cx="20" cy="20" r="6" fill="white"/>
            </svg>
        </div>

        <h1 class="reveal" style="font-family: var(--font-display); font-size: var(--title-size); font-weight: 800; letter-spacing: -0.03em; color: var(--color-text-primary);">
            CompanyName
        </h1>

        <p class="reveal" style="font-size: var(--body-size); font-weight: 500; color: var(--color-accent); margin-top: 12px;">
            One-line value proposition that captures the core benefit
        </p>

        <p class="reveal" style="font-size: var(--small-size); color: var(--color-text-secondary); max-width: 800px; margin-top: 24px; line-height: 1.6;">
            Supporting context sentence. What you do and for whom.
        </p>

        <!-- Badges -->
        <div class="reveal" style="display: flex; gap: 16px; margin-top: 40px;">
            <span class="badge">MDR Certified</span>
            <span class="badge">GDPR Compliant</span>
            <span class="badge">On-Premise</span>
        </div>

        <!-- Cover metrics -->
        <div class="reveal" style="display: flex; gap: 80px; margin-top: 56px;">
            <div style="text-align: center;">
                <div class="stat-number" style="font-size: 48px;">$2.4M</div>
                <div class="stat-label">Key Metric 1</div>
            </div>
            <div style="text-align: center;">
                <div class="stat-number" style="font-size: 48px;">420</div>
                <div class="stat-label">Key Metric 2</div>
            </div>
            <div style="text-align: center;">
                <div class="stat-number" style="font-size: 48px;">&lt;30s</div>
                <div class="stat-label">Key Metric 3</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <span>Company GmbH | Confidential</span>
        <span>March 2026 — 1 / 12</span>
    </div>
</section>

<!-- ==========================================================
     SLIDE 2: PROBLEM (darker tone = tension)
     ========================================================== -->
<section class="slide problem-slide" style="background: var(--color-text-primary);">
    <div class="slide-content">
        <div class="accent-line" style="background: var(--color-danger);"></div>
        <div class="section-label" style="color: var(--color-danger);">The Problem</div>

        <h2 class="slide-title reveal" style="color: var(--color-surface); max-width: 1200px;">
            The headline stat that makes the pain visceral and undeniable
        </h2>

        <div style="display: flex; gap: var(--content-gap); margin-top: var(--content-gap); flex: 1;">
            <!-- Left: Hero number -->
            <div class="reveal" style="flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; background: rgba(255,255,255,0.06); border-radius: var(--radius-xl); padding: 48px;">
                <div class="hero-number" style="color: var(--color-danger);">73%</div>
                <div class="hero-context" style="color: rgba(255,255,255,0.7); text-align: center; max-width: 400px;">
                    of hospitals still plan surgeries manually
                </div>
            </div>

            <!-- Right: Supporting data -->
            <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: var(--element-gap);">
                <div class="stat-card reveal" style="background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.1);">
                    <div class="stat-number" style="color: var(--color-surface); font-size: 48px;">1,900</div>
                    <div class="stat-label" style="color: rgba(255,255,255,0.6);">Hospitals in Germany</div>
                </div>
                <div class="stat-card reveal" style="background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.1);">
                    <div class="stat-number" style="color: var(--color-surface); font-size: 48px;">€15-30</div>
                    <div class="stat-label" style="color: rgba(255,255,255,0.6);">Cost per OR minute</div>
                </div>
                <div class="stat-card reveal" style="background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.1);">
                    <div class="stat-number" style="color: var(--color-surface); font-size: 48px;">~50/yr</div>
                    <div class="stat-label" style="color: rgba(255,255,255,0.6);">Closures (consolidation)</div>
                </div>
                <div class="stat-card reveal" style="background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.1);">
                    <div class="stat-number" style="color: var(--color-surface); font-size: 48px;">€3.1M</div>
                    <div class="stat-label" style="color: rgba(255,255,255,0.6);">Savings potential/site</div>
                </div>
            </div>
        </div>

        <p class="reveal" style="font-size: var(--caption-size); color: rgba(255,255,255,0.4); margin-top: 20px;">
            Sources: DKG 2024, InEK cost data, Cardoen et al. 2010
        </p>
    </div>

    <div class="slide-footer" style="background: transparent; border-color: rgba(255,255,255,0.1); color: rgba(255,255,255,0.4);">
        <span>Company GmbH | Confidential</span>
        <span>March 2026 — 2 / 12</span>
    </div>
</section>

<!-- ==========================================================
     SLIDE 3: TRACTION (the most important slide)
     ========================================================== -->
<section class="slide traction-slide atmospheric-bg">
    <div class="slide-content">
        <div class="accent-line"></div>
        <div class="section-label">Traction</div>
        <h2 class="slide-title reveal">Validated at pilot site with measurable results</h2>

        <!-- Metric row: 4 key stats -->
        <div class="reveal" style="display: flex; gap: 48px; justify-content: center; margin: var(--content-gap) 0;">
            <div style="text-align: center; flex: 1;">
                <div class="stat-number">€3.1M</div>
                <div class="stat-label">Annual savings at pilot</div>
            </div>
            <div style="width: 1px; background: var(--color-border);"></div>
            <div style="text-align: center; flex: 1;">
                <div class="stat-number" style="color: var(--color-success);">+8%</div>
                <div class="stat-label">OR capacity increase</div>
            </div>
            <div style="width: 1px; background: var(--color-border);"></div>
            <div style="text-align: center; flex: 1;">
                <div class="stat-number">&lt;30s</div>
                <div class="stat-label">Planning suggestion</div>
            </div>
            <div style="width: 1px; background: var(--color-border);"></div>
            <div style="text-align: center; flex: 1;">
                <div class="stat-number" style="color: var(--color-success);">92%</div>
                <div class="stat-label">Acceptance rate</div>
            </div>
        </div>

        <!-- Chart placeholder (use SVG or Canva-generated) -->
        <div class="reveal" style="flex: 1; background: var(--color-surface); border-radius: var(--radius-lg); border: 1px solid var(--color-border); padding: 40px; display: flex; align-items: center; justify-content: center;">
            <svg viewBox="0 0 1200 300" style="width: 100%; max-height: 280px;">
                <defs>
                    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="var(--color-accent)" stop-opacity="0.2"/>
                        <stop offset="100%" stop-color="var(--color-accent)" stop-opacity="0"/>
                    </linearGradient>
                </defs>
                <!-- Grid -->
                <line x1="0" y1="75" x2="1200" y2="75" stroke="var(--color-divider)" stroke-dasharray="4"/>
                <line x1="0" y1="150" x2="1200" y2="150" stroke="var(--color-divider)" stroke-dasharray="4"/>
                <line x1="0" y1="225" x2="1200" y2="225" stroke="var(--color-divider)" stroke-dasharray="4"/>
                <!-- Area -->
                <polygon fill="url(#areaGrad)" points="0,280 200,260 400,230 600,180 800,120 1000,60 1200,20 1200,300 0,300"/>
                <!-- Line -->
                <polyline fill="none" stroke="var(--color-accent)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"
                          points="0,280 200,260 400,230 600,180 800,120 1000,60 1200,20"/>
                <!-- End dot -->
                <circle cx="1200" cy="20" r="6" fill="var(--color-accent)"/>
                <!-- Labels -->
                <text x="0" y="298" font-size="20" fill="var(--color-text-muted)" font-family="var(--font-body)">Q1 '25</text>
                <text x="1120" y="298" font-size="20" fill="var(--color-text-muted)" font-family="var(--font-body)">Q4 '26</text>
                <text x="1200" y="14" font-size="24" font-weight="700" fill="var(--color-accent)" font-family="var(--font-display)" text-anchor="end">€3.1M ARR</text>
            </svg>
        </div>
    </div>

    <div class="slide-footer">
        <span>Company GmbH | Confidential</span>
        <span>March 2026 — 8 / 12</span>
    </div>
</section>

<!-- === JAVASCRIPT: Presentation Controller (HTML preview only) === -->
<script>
class SlidePresentation {
    constructor() {
        this.slides = document.querySelectorAll('.slide');
        this.current = 0;
        this.scaleToFit();
        this.setupNav();
        this.show(0);
        window.addEventListener('resize', () => this.scaleToFit());
    }

    scaleToFit() {
        const s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
        document.body.style.transform = `scale(${s})`;
        document.body.style.width = '1920px';
        document.body.style.height = `${1080 * this.slides.length}px`;
    }

    setupNav() {
        document.addEventListener('keydown', e => {
            if (['ArrowDown','ArrowRight',' '].includes(e.key)) { e.preventDefault(); this.show(this.current + 1); }
            if (['ArrowUp','ArrowLeft'].includes(e.key)) { e.preventDefault(); this.show(this.current - 1); }
        });
        let t; window.addEventListener('wheel', e => { clearTimeout(t); t = setTimeout(() => e.deltaY > 0 ? this.show(this.current + 1) : this.show(this.current - 1), 80); }, {passive:true});
    }

    show(i) {
        if (i < 0 || i >= this.slides.length) return;
        this.current = i;
        this.slides.forEach((s, idx) => { s.style.display = idx === i ? 'flex' : 'none'; s.classList.toggle('visible', idx === i); });
    }
}

if (!window.matchMedia('print').matches) new SlidePresentation();
window.addEventListener('beforeprint', () => document.querySelectorAll('.slide').forEach(s => { s.style.display = 'flex'; s.classList.add('visible'); }));
</script>
</body>
</html>
```

## How to Use This Template

1. **Copy the entire HTML above** as your starting point
2. **Replace the `:root` block** with the user's chosen preset from STYLE_PRESETS.md
3. **Replace the `@import` font URL** with the preset's font pairing
4. **Add slides** following the patterns shown (Cover, Problem, Traction)
5. **For each new slide type,** read SLIDE_TYPES.md and use its HTML template + CSS classes
6. **NEVER drop below the font size minimums** shown in the `:root` variables
7. **NEVER use inline `style=""` for colors** — always use `var(--color-*)` variables

## Quality Checklist

Before delivering the HTML file, verify:
- [ ] Smallest font in the file >= 20px
- [ ] All colors use `var(--color-*)` variables
- [ ] Display font AND body font from preset are both used
- [ ] At least one `.atmospheric-bg` element exists
- [ ] Breathing room slide every 3-4 content slides
- [ ] `@media print` block present and complete
- [ ] Every `<section>` has `class="slide [type]-slide"`
