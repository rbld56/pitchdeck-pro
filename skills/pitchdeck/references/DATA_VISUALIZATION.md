# Data Visualization Patterns for Pitch Decks

All patterns use CSS/SVG only — no external charting libraries. PDF-compatible.

## 1. Stat Card (Big Number)

The most important pattern. Used on Traction, Financials, Unit Economics slides.

```html
<div class="stat-card">
    <div class="stat-number">$2.4M</div>
    <div class="stat-label">Annual Recurring Revenue</div>
</div>
```

```css
.stat-card { text-align: center; padding: 32px; }
.stat-number {
    font-size: 96px;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1;
    color: var(--color-accent);
}
.stat-label {
    font-size: 24px;
    font-weight: 400;
    color: var(--color-text-secondary);
    margin-top: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
```

**Gradient variant:**
```css
.stat-number.gradient {
    background: linear-gradient(135deg, var(--color-accent), var(--color-accent-hover));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

## 2. Horizontal Bar Chart (CSS-only)

For comparisons (market share, feature comparison, competitor analysis).

```html
<div class="bar-chart">
    <div class="bar-row">
        <span class="bar-label">Our Product</span>
        <div class="bar-track">
            <div class="bar-fill primary" style="width: 85%">85%</div>
        </div>
    </div>
    <div class="bar-row">
        <span class="bar-label">Competitor A</span>
        <div class="bar-track">
            <div class="bar-fill secondary" style="width: 60%">60%</div>
        </div>
    </div>
</div>
```

```css
.bar-chart { width: 100%; }
.bar-row { display: flex; align-items: center; margin-bottom: 16px; }
.bar-label { width: 200px; font-size: 24px; text-align: right; padding-right: 24px; }
.bar-track { flex: 1; height: 40px; background: var(--color-surface); border-radius: 8px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 8px; display: flex; align-items: center; justify-content: flex-end; padding-right: 16px; font-size: 20px; font-weight: 600; color: white; }
.bar-fill.primary { background: var(--color-accent); }
.bar-fill.secondary { background: var(--color-text-secondary); opacity: 0.4; }
```

## 3. Metric Row (3-4 stats inline)

For Traction slides showing multiple KPIs.

```html
<div class="metric-row">
    <div class="metric">
        <div class="metric-value">$2.4M</div>
        <div class="metric-label">ARR</div>
    </div>
    <div class="metric-divider"></div>
    <div class="metric">
        <div class="metric-value">142%</div>
        <div class="metric-label">YoY Growth</div>
    </div>
    <div class="metric-divider"></div>
    <div class="metric">
        <div class="metric-value">97%</div>
        <div class="metric-label">Net Revenue Retention</div>
    </div>
</div>
```

```css
.metric-row { display: flex; justify-content: center; align-items: center; gap: 48px; }
.metric { text-align: center; }
.metric-value { font-size: 64px; font-weight: 800; letter-spacing: -0.03em; color: var(--color-accent); }
.metric-label { font-size: 20px; color: var(--color-text-secondary); margin-top: 8px; text-transform: uppercase; letter-spacing: 0.05em; }
.metric-divider { width: 1px; height: 80px; background: var(--color-border); }
```

## 4. Simple SVG Line Chart

For growth trends (revenue, users). Inline SVG for PDF compatibility.

```html
<svg class="line-chart" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    <!-- Grid lines -->
    <line x1="0" y1="100" x2="800" y2="100" stroke="var(--color-border)" stroke-dasharray="4"/>
    <line x1="0" y1="200" x2="800" y2="200" stroke="var(--color-border)" stroke-dasharray="4"/>
    <line x1="0" y1="300" x2="800" y2="300" stroke="var(--color-border)" stroke-dasharray="4"/>
    <!-- Growth line -->
    <polyline fill="none" stroke="var(--color-accent)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"
              points="0,380 160,340 320,280 480,200 640,100 800,20"/>
    <!-- Area fill -->
    <polygon fill="url(#gradient)" opacity="0.15"
             points="0,380 160,340 320,280 480,200 640,100 800,20 800,400 0,400"/>
    <!-- Labels -->
    <text x="0" y="398" font-size="18" fill="var(--color-text-secondary)">Q1 '24</text>
    <text x="760" y="398" font-size="18" fill="var(--color-text-secondary)">Q4 '25</text>
    <text x="800" y="14" font-size="20" font-weight="700" fill="var(--color-accent)">$2.4M</text>
</svg>
```

## 5. Comparison Matrix (Competition)

2x2 matrix with your company highlighted.

```html
<div class="matrix-2x2">
    <div class="matrix-axis-y">Feature Completeness &rarr;</div>
    <div class="matrix-axis-x">Ease of Use &rarr;</div>
    <div class="matrix-quadrant q1"></div>
    <div class="matrix-quadrant q2"></div>
    <div class="matrix-quadrant q3"></div>
    <div class="matrix-quadrant q4"></div>
    <div class="matrix-dot competitor" style="left: 30%; top: 60%">Comp A</div>
    <div class="matrix-dot competitor" style="left: 50%; top: 40%">Comp B</div>
    <div class="matrix-dot highlight" style="left: 80%; top: 15%">Us</div>
</div>
```

```css
.matrix-2x2 { position: relative; width: 800px; height: 600px; border-left: 2px solid var(--color-text-secondary); border-bottom: 2px solid var(--color-text-secondary); }
.matrix-dot { position: absolute; padding: 8px 16px; border-radius: 20px; font-size: 20px; font-weight: 600; transform: translate(-50%, -50%); }
.matrix-dot.competitor { background: var(--color-surface); color: var(--color-text-secondary); }
.matrix-dot.highlight { background: var(--color-accent); color: white; font-size: 24px; padding: 12px 24px; box-shadow: 0 4px 20px var(--color-accent-muted, rgba(0,0,0,0.2)); }
```

## 6. Use of Funds (Horizontal stacked bar)

For The Ask slide.

```html
<div class="funds-bar">
    <div class="funds-segment" style="flex: 4; background: var(--color-accent);">Engineering 40%</div>
    <div class="funds-segment" style="flex: 3; background: var(--color-accent-hover);">Sales 30%</div>
    <div class="funds-segment" style="flex: 2; opacity: 0.7;">Marketing 20%</div>
    <div class="funds-segment" style="flex: 1; opacity: 0.5;">Ops 10%</div>
</div>
```

## Chart Styling Rules
1. Max 2 data series per chart
2. Always label axes
3. Brand accent for primary data, neutral gray for secondary
4. Y-axis starts at zero (no truncation)
5. No 3D effects, ever
6. No/minimal gridlines
7. Annotate key inflection points
8. Use K/M/B abbreviations ($2.4M not $2,400,000)
9. Chart font: min 20px
10. White/light background for charts (even in dark themes, chart areas can be light)
