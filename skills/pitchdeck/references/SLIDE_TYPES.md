# Slide Type Archetypes Reference

> **Purpose:** Defines 16 pitch-deck slide archetypes with HTML structure templates and CSS patterns optimized for PDF rendering at fixed 1920x1080px.
>
> **Rendering constraints:**
> - All dimensions in **fixed px** -- no `clamp()`, no `vh`/`vw`, no relative units
> - Each slide: exactly **1920x1080px**, `overflow: hidden`
> - Padding: **80px** on all sides (usable content area: **1760x920px**)
> - Font sizes: body **32px min**, headlines **56-72px**, hero numbers **96-120px**
> - Content limits are **strict** -- if exceeded, the generator MUST split into multiple slides

---

## Base Slide CSS

Every slide inherits these base styles. Type-specific CSS is additive.

```css
.slide {
  width: 1920px;
  height: 1080px;
  padding: 80px;
  overflow: hidden;
  position: relative;
  box-sizing: border-box;
  font-family: var(--font-body, 'Inter', sans-serif);
  color: var(--color-text, #1a1a2e);
  background: var(--color-bg, #ffffff);
}

.slide-content {
  width: 1760px;
  height: 920px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.slide h2 {
  font-size: 56px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 40px 0;
}

.slide p,
.slide li {
  font-size: 32px;
  line-height: 1.5;
  margin: 0 0 16px 0;
}

/* Split layouts */
.split {
  display: flex;
  gap: 60px;
  height: 920px;
}
.split-60-40 .split-left  { flex: 0 0 1020px; }
.split-60-40 .split-right { flex: 0 0 680px; }
.split-50-50 > *          { flex: 0 0 850px; }

/* Utility: centered content */
.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

/* Grid system */
.grid      { display: grid; gap: 40px; }
.grid-2    { grid-template-columns: repeat(2, 1fr); }
.grid-3    { grid-template-columns: repeat(3, 1fr); }

/* Bullet list (no native markers) */
ul.bullet-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
ul.bullet-list li {
  padding-left: 48px;
  position: relative;
  margin-bottom: 24px;
}
ul.bullet-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 18px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--color-accent, #6c5ce7);
}
```

---

## 1. Cover / Title

**Description:** Opening slide with logo, company name, tagline, and optional author line.

**Content density:** Max **20 words**. Max **4 elements** (logo, name, tagline, author).

### HTML

```html
<section class="slide cover-slide">
  <div class="slide-content centered">
    <img class="cover-logo" src="logo.png" alt="Company Logo" />
    <h1 class="cover-title">Company Name</h1>
    <p class="tagline">One-liner that captures the entire value proposition</p>
    <p class="author">Founder Name -- Title</p>
  </div>
</section>
```

### CSS

```css
.cover-slide {
  background: var(--color-bg, #ffffff);
}

.cover-slide .slide-content {
  gap: 32px;
}

.cover-logo {
  width: 160px;
  height: 160px;
  object-fit: contain;
  margin-bottom: 16px;
}

.cover-title {
  font-size: 72px;
  font-weight: 800;
  line-height: 1.1;
  margin: 0;
  letter-spacing: -1px;
}

.cover-slide .tagline {
  font-size: 32px;
  color: var(--color-text-muted, #555);
  max-width: 1200px;
  margin: 0;
}

.cover-slide .author {
  font-size: 24px;
  color: var(--color-text-muted, #555);
  margin-top: 24px;
}
```

---

## 2. Hero Metric

**Description:** A single dominant number occupying the full slide to create maximum impact.

**Content density:** Max **10 words**. Max **2 elements** (number + context sentence).

### HTML

```html
<section class="slide metric-slide">
  <div class="slide-content centered">
    <span class="stat-number">4.2M</span>
    <span class="stat-label">active users across 38 countries</span>
  </div>
</section>
```

### CSS

```css
.metric-slide .slide-content {
  gap: 24px;
}

.metric-slide .stat-number {
  font-size: 120px;
  font-weight: 800;
  line-height: 1.0;
  color: var(--color-accent, #6c5ce7);
  letter-spacing: -2px;
}

.metric-slide .stat-label {
  font-size: 32px;
  color: var(--color-text-muted, #555);
  max-width: 900px;
}
```

---

## 3. Problem

**Description:** Frames the pain point with urgency using a darker visual tone to create tension.

**Content density:** Max **60 words**. Max **5 elements** (headline + 3 bullets + 1 stat).

### HTML

```html
<section class="slide problem-slide">
  <div class="slide-content">
    <h2>The Problem</h2>
    <ul class="bullet-list">
      <li>First pain point described in one concise sentence</li>
      <li>Second pain point described in one concise sentence</li>
      <li>Third pain point described in one concise sentence</li>
    </ul>
    <div class="highlight-stat">
      <span class="stat-number">72%</span>
      <span class="stat-label">of enterprises report this exact frustration</span>
    </div>
  </div>
</section>
```

### CSS

```css
.problem-slide {
  background: var(--color-bg-dark, #1a1a2e);
  color: var(--color-text-inverse, #f0f0f0);
}

.problem-slide h2 {
  color: var(--color-accent-warm, #e74c3c);
}

.problem-slide .bullet-list li::before {
  background: var(--color-accent-warm, #e74c3c);
}

.problem-slide .highlight-stat {
  display: flex;
  align-items: baseline;
  gap: 20px;
  margin-top: 48px;
  padding-top: 40px;
  border-top: 2px solid rgba(255, 255, 255, 0.15);
}

.problem-slide .highlight-stat .stat-number {
  font-size: 96px;
  font-weight: 800;
  color: var(--color-accent-warm, #e74c3c);
  line-height: 1.0;
}

.problem-slide .highlight-stat .stat-label {
  font-size: 32px;
  color: var(--color-text-muted-inverse, #aaa);
}
```

---

## 4. Solution

**Description:** Presents the product as the answer, using a lighter tone to contrast the problem slide and signal relief.

**Content density:** Max **50 words**. Max **5 elements** (headline + 3 benefits + visual area).

### HTML

```html
<section class="slide solution-slide">
  <div class="split split-60-40">
    <div class="split-left">
      <h2>The Solution</h2>
      <ul class="bullet-list">
        <li>Benefit one with clear outcome</li>
        <li>Benefit two with clear outcome</li>
        <li>Benefit three with clear outcome</li>
      </ul>
    </div>
    <div class="split-right">
      <div class="visual-area">
        <!-- Product screenshot or illustration placeholder -->
        <img src="product-screenshot.png" alt="Product Screenshot" />
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.solution-slide {
  background: var(--color-bg-light, #f8f9fa);
}

.solution-slide .split-left {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.solution-slide .visual-area {
  width: 680px;
  height: 920px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg, #ffffff);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.solution-slide .visual-area img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
```

---

## 5. How It Works

**Description:** Shows a 3-step process flow in a horizontal layout to explain the product mechanism.

**Content density:** Max **45 words**. Max **4 elements** (headline + 3 steps with number, title, and 5-8 word description each).

### HTML

```html
<section class="slide process-slide">
  <div class="slide-content">
    <h2>How It Works</h2>
    <div class="process-flow">
      <div class="step">
        <span class="step-number">1</span>
        <h3 class="step-title">Connect</h3>
        <p class="step-desc">Integrate with your existing data sources</p>
      </div>
      <div class="step-connector"></div>
      <div class="step">
        <span class="step-number">2</span>
        <h3 class="step-title">Analyze</h3>
        <p class="step-desc">AI processes and surfaces key insights</p>
      </div>
      <div class="step-connector"></div>
      <div class="step">
        <span class="step-number">3</span>
        <h3 class="step-title">Act</h3>
        <p class="step-desc">Receive actionable recommendations instantly</p>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.process-slide .slide-content {
  justify-content: center;
}

.process-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 60px;
  gap: 0;
}

.process-flow .step {
  flex: 0 0 440px;
  text-align: center;
  padding: 48px 32px;
}

.process-flow .step-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: var(--color-accent, #6c5ce7);
  color: #ffffff;
  font-size: 36px;
  font-weight: 800;
  margin: 0 auto 24px auto;
}

.process-flow .step-title {
  font-size: 36px;
  font-weight: 700;
  margin: 0 0 16px 0;
}

.process-flow .step-desc {
  font-size: 28px;
  color: var(--color-text-muted, #555);
  margin: 0;
}

.step-connector {
  flex: 0 0 60px;
  height: 4px;
  background: var(--color-accent, #6c5ce7);
  opacity: 0.4;
  margin-top: -40px;
}
```

---

## 6. Market Size

**Description:** Presents TAM/SAM/SOM figures with source citations to validate the market opportunity.

**Content density:** Max **50 words**. Max **5 elements** (headline + 3 market tiers + source citation).

### HTML

```html
<section class="slide market-slide">
  <div class="slide-content">
    <h2>Market Opportunity</h2>
    <div class="market-visual">
      <div class="market-ring ring-tam">
        <span class="market-value">$84B</span>
        <span class="market-tier">TAM</span>
        <span class="market-desc">Total Addressable Market</span>
      </div>
      <div class="market-ring ring-sam">
        <span class="market-value">$12B</span>
        <span class="market-tier">SAM</span>
        <span class="market-desc">Serviceable Addressable Market</span>
      </div>
      <div class="market-ring ring-som">
        <span class="market-value">$1.8B</span>
        <span class="market-tier">SOM</span>
        <span class="market-desc">Serviceable Obtainable Market</span>
      </div>
    </div>
    <p class="source-citation">Source: Gartner 2025, McKinsey Global Institute</p>
  </div>
</section>
```

### CSS

```css
.market-slide .slide-content {
  align-items: center;
}

.market-visual {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 80px;
  margin: 60px 0 40px 0;
  flex: 1;
}

.market-ring {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  text-align: center;
}

.ring-tam {
  width: 400px;
  height: 400px;
  background: rgba(108, 92, 231, 0.08);
  border: 4px solid var(--color-accent, #6c5ce7);
}

.ring-sam {
  width: 320px;
  height: 320px;
  background: rgba(108, 92, 231, 0.15);
  border: 4px solid var(--color-accent, #6c5ce7);
}

.ring-som {
  width: 240px;
  height: 240px;
  background: rgba(108, 92, 231, 0.25);
  border: 4px solid var(--color-accent, #6c5ce7);
}

.market-value {
  font-size: 48px;
  font-weight: 800;
  color: var(--color-accent, #6c5ce7);
}

.market-tier {
  font-size: 28px;
  font-weight: 700;
  margin-top: 4px;
}

.market-desc {
  font-size: 20px;
  color: var(--color-text-muted, #555);
  margin-top: 4px;
}

.source-citation {
  font-size: 20px;
  color: var(--color-text-muted, #888);
  font-style: italic;
  margin: 0;
}
```

---

## 7. Business Model

**Description:** Explains how the company makes money using a card grid for pricing tiers or unit economics.

**Content density:** Max **60 words**. Max **5 elements** (headline + 3-4 model cards).

### HTML

```html
<section class="slide model-slide">
  <div class="slide-content">
    <h2>Business Model</h2>
    <div class="model-grid">
      <div class="model-card">
        <h3 class="model-card-title">Starter</h3>
        <span class="model-card-price">$49/mo</span>
        <p class="model-card-desc">For small teams up to 10 users</p>
      </div>
      <div class="model-card featured">
        <h3 class="model-card-title">Growth</h3>
        <span class="model-card-price">$199/mo</span>
        <p class="model-card-desc">For scaling companies up to 100 users</p>
      </div>
      <div class="model-card">
        <h3 class="model-card-title">Enterprise</h3>
        <span class="model-card-price">Custom</span>
        <p class="model-card-desc">Dedicated support, SSO, SLA</p>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.model-grid {
  display: flex;
  gap: 40px;
  justify-content: center;
  margin-top: 60px;
  flex: 1;
  align-items: center;
}

.model-card {
  flex: 0 0 480px;
  padding: 48px 40px;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 16px;
  border: 2px solid transparent;
  text-align: center;
}

.model-card.featured {
  border-color: var(--color-accent, #6c5ce7);
  background: var(--color-bg, #ffffff);
  box-shadow: 0 8px 32px rgba(108, 92, 231, 0.12);
  transform: scale(1.05);
}

.model-card-title {
  font-size: 32px;
  font-weight: 700;
  margin: 0 0 16px 0;
}

.model-card-price {
  font-size: 48px;
  font-weight: 800;
  color: var(--color-accent, #6c5ce7);
  display: block;
  margin-bottom: 16px;
}

.model-card-desc {
  font-size: 24px;
  color: var(--color-text-muted, #555);
  margin: 0;
}
```

---

## 8. Traction

**Description:** The most important slide. Shows growth evidence with one dominant chart and supporting stat cards.

**Content density:** Max **50 words**. Max **6 elements** (headline + chart area + 3-4 stat cards).

### HTML

```html
<section class="slide traction-slide">
  <div class="slide-content">
    <h2>Traction</h2>
    <div class="traction-layout">
      <div class="chart-area">
        <!-- Chart rendered via charting library or SVG -->
        <div class="chart-placeholder" data-chart="revenue-growth"></div>
      </div>
      <div class="stat-row">
        <div class="stat-card">
          <span class="stat-card-value">340%</span>
          <span class="stat-card-label">YoY Revenue Growth</span>
        </div>
        <div class="stat-card">
          <span class="stat-card-value">12K</span>
          <span class="stat-card-label">Paying Customers</span>
        </div>
        <div class="stat-card">
          <span class="stat-card-value">$2.4M</span>
          <span class="stat-card-label">ARR</span>
        </div>
        <div class="stat-card">
          <span class="stat-card-value">4.8/5</span>
          <span class="stat-card-label">Customer Rating</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.traction-layout {
  display: flex;
  gap: 40px;
  flex: 1;
  margin-top: 20px;
}

.traction-layout .chart-area {
  flex: 0 0 1020px;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 16px;
  padding: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.traction-layout .chart-placeholder {
  width: 100%;
  height: 100%;
}

.stat-row {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 24px;
  justify-content: center;
}

.stat-card {
  padding: 28px 32px;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 12px;
  border-left: 5px solid var(--color-accent, #6c5ce7);
}

.stat-card-value {
  display: block;
  font-size: 40px;
  font-weight: 800;
  color: var(--color-accent, #6c5ce7);
  line-height: 1.1;
}

.stat-card-label {
  display: block;
  font-size: 22px;
  color: var(--color-text-muted, #555);
  margin-top: 4px;
}
```

---

## 9. Competition

**Description:** Positions the company against competitors using a 2x2 matrix or feature comparison table.

**Content density:** Max **60 words**. Max **6 elements** (headline + matrix/table with 4-5 features and 3-4 competitors).

### HTML

```html
<section class="slide competition-slide">
  <div class="slide-content">
    <h2>Competitive Landscape</h2>
    <div class="competition-matrix">
      <table class="comp-table">
        <thead>
          <tr>
            <th>Feature</th>
            <th class="comp-us">Our Company</th>
            <th>Competitor A</th>
            <th>Competitor B</th>
            <th>Competitor C</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Feature One</td>
            <td class="comp-us"><span class="check full"></span></td>
            <td><span class="check partial"></span></td>
            <td><span class="check none"></span></td>
            <td><span class="check partial"></span></td>
          </tr>
          <tr>
            <td>Feature Two</td>
            <td class="comp-us"><span class="check full"></span></td>
            <td><span class="check full"></span></td>
            <td><span class="check partial"></span></td>
            <td><span class="check none"></span></td>
          </tr>
          <tr>
            <td>Feature Three</td>
            <td class="comp-us"><span class="check full"></span></td>
            <td><span class="check none"></span></td>
            <td><span class="check full"></span></td>
            <td><span class="check partial"></span></td>
          </tr>
          <tr>
            <td>Feature Four</td>
            <td class="comp-us"><span class="check full"></span></td>
            <td><span class="check partial"></span></td>
            <td><span class="check partial"></span></td>
            <td><span class="check none"></span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```

### CSS

```css
.competition-matrix {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 40px;
}

.comp-table {
  width: 1600px;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 28px;
}

.comp-table th,
.comp-table td {
  padding: 24px 32px;
  text-align: center;
  border-bottom: 2px solid var(--color-border, #e0e0e0);
}

.comp-table th {
  font-size: 24px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--color-text-muted, #555);
}

.comp-table td:first-child,
.comp-table th:first-child {
  text-align: left;
  font-weight: 600;
}

/* Emphasize our column */
.comp-us {
  background: rgba(108, 92, 231, 0.06);
}
th.comp-us {
  color: var(--color-accent, #6c5ce7) !important;
  font-size: 26px !important;
}

/* Check indicators */
.check {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
}
.check.full    { background: var(--color-accent, #6c5ce7); }
.check.partial { background: var(--color-text-muted, #ccc); }
.check.none    { background: transparent; border: 3px solid var(--color-border, #ddd); }
```

---

## 10. Team

**Description:** Introduces key team members with photo placeholders, names, titles, and one standout credential each.

**Content density:** Max **60 words**. Max **5 people** (each: photo + name + title + credential).

### HTML

```html
<section class="slide team-slide">
  <div class="slide-content">
    <h2>The Team</h2>
    <div class="team-grid">
      <div class="team-member">
        <div class="team-photo">
          <img src="team-1.jpg" alt="Jane Doe" />
        </div>
        <span class="team-name">Jane Doe</span>
        <span class="team-title">CEO & Co-Founder</span>
        <span class="team-credential">Ex-Google, 12y SaaS</span>
      </div>
      <div class="team-member">
        <div class="team-photo">
          <img src="team-2.jpg" alt="John Smith" />
        </div>
        <span class="team-name">John Smith</span>
        <span class="team-title">CTO & Co-Founder</span>
        <span class="team-credential">PhD ML, Stanford</span>
      </div>
      <div class="team-member">
        <div class="team-photo">
          <img src="team-3.jpg" alt="Alice Johnson" />
        </div>
        <span class="team-name">Alice Johnson</span>
        <span class="team-title">VP Engineering</span>
        <span class="team-credential">Ex-Stripe, Scale-up Lead</span>
      </div>
      <div class="team-member">
        <div class="team-photo">
          <img src="team-4.jpg" alt="Bob Lee" />
        </div>
        <span class="team-name">Bob Lee</span>
        <span class="team-title">Head of Sales</span>
        <span class="team-credential">$50M+ Enterprise ARR</span>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.team-slide .slide-content {
  align-items: center;
}

.team-grid {
  display: flex;
  gap: 60px;
  justify-content: center;
  margin-top: 60px;
  flex: 1;
  align-items: center;
}

.team-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 0 0 320px;
}

.team-photo {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  overflow: hidden;
  margin-bottom: 24px;
  background: var(--color-bg-light, #e8e8e8);
}

.team-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-name {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 4px;
}

.team-title {
  font-size: 20px;
  color: var(--color-text, #1a1a2e);
  margin-bottom: 8px;
}

.team-credential {
  font-size: 20px;
  color: var(--color-text-muted, #888);
}
```

---

## 11. Financials

**Description:** Presents 3-5 year financial projections with a bar chart and key assumptions sidebar.

**Content density:** Max **60 words**. Max **6 elements** (headline + chart area + 3-4 assumption bullets).

### HTML

```html
<section class="slide financials-slide">
  <div class="split split-60-40">
    <div class="chart-area">
      <h2>Financial Projections</h2>
      <div class="chart-placeholder" data-chart="revenue-projection"></div>
    </div>
    <div class="assumptions">
      <h3 class="assumptions-title">Key Assumptions</h3>
      <ul class="bullet-list">
        <li>20% MoM growth sustained through Y2</li>
        <li>Gross margin expanding to 78% by Y3</li>
        <li>CAC payback under 12 months</li>
        <li>OpEx scaling at 60% of revenue growth</li>
      </ul>
    </div>
  </div>
</section>
```

### CSS

```css
.financials-slide .chart-area {
  display: flex;
  flex-direction: column;
}

.financials-slide .chart-area h2 {
  margin-bottom: 32px;
}

.financials-slide .chart-placeholder {
  flex: 1;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 16px;
  padding: 32px;
}

.financials-slide .assumptions {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 20px;
  border-left: 4px solid var(--color-accent, #6c5ce7);
}

.assumptions-title {
  font-size: 32px;
  font-weight: 700;
  margin: 0 0 32px 0;
}

.financials-slide .bullet-list li {
  font-size: 26px;
  margin-bottom: 20px;
}
```

---

## 12. The Ask / CTA

**Description:** States the funding amount, intended use of funds, and key milestones. Visually confident and forward-looking.

**Content density:** Max **50 words**. Max **5 elements** (amount headline + 3-4 use-of-funds bullets + milestone row).

### HTML

```html
<section class="slide ask-slide">
  <div class="slide-content">
    <h2 class="ask-amount">Raising $5M Series A</h2>
    <div class="use-of-funds">
      <h3 class="uof-title">Use of Funds</h3>
      <ul class="bullet-list">
        <li>40% -- Engineering & Product (AI platform expansion)</li>
        <li>30% -- Go-to-Market (US & EU sales team)</li>
        <li>20% -- Customer Success & Operations</li>
        <li>10% -- Reserve</li>
      </ul>
    </div>
    <div class="milestones">
      <div class="milestone">
        <span class="milestone-date">Q3 2026</span>
        <span class="milestone-text">$5M ARR</span>
      </div>
      <div class="milestone-connector"></div>
      <div class="milestone">
        <span class="milestone-date">Q1 2027</span>
        <span class="milestone-text">50K Users</span>
      </div>
      <div class="milestone-connector"></div>
      <div class="milestone">
        <span class="milestone-date">Q4 2027</span>
        <span class="milestone-text">Series B Ready</span>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.ask-slide {
  background: var(--color-accent, #6c5ce7);
  color: #ffffff;
}

.ask-amount {
  font-size: 72px;
  font-weight: 800;
  color: #ffffff;
  text-align: center;
  margin-bottom: 48px;
}

.ask-slide .uof-title {
  font-size: 32px;
  font-weight: 700;
  margin: 0 0 24px 0;
  color: rgba(255, 255, 255, 0.85);
}

.ask-slide .bullet-list li {
  color: rgba(255, 255, 255, 0.95);
  font-size: 28px;
}

.ask-slide .bullet-list li::before {
  background: #ffffff;
}

.milestones {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 48px;
  padding-top: 40px;
  border-top: 2px solid rgba(255, 255, 255, 0.2);
  gap: 0;
}

.milestone {
  text-align: center;
  flex: 0 0 360px;
}

.milestone-date {
  display: block;
  font-size: 22px;
  font-weight: 600;
  opacity: 0.75;
  margin-bottom: 8px;
}

.milestone-text {
  display: block;
  font-size: 32px;
  font-weight: 800;
}

.milestone-connector {
  flex: 0 0 60px;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
}
```

---

## 13. ESG / Mission (2026)

**Description:** Highlights environmental, social, and governance impact metrics with compliance badges in a card grid layout.

**Content density:** Max **50 words**. Max **5 elements** (headline + 3-4 impact cards).

### HTML

```html
<section class="slide esg-slide">
  <div class="slide-content">
    <h2>Impact & ESG Commitment</h2>
    <div class="impact-grid grid grid-2">
      <div class="impact-card">
        <div class="impact-icon" aria-label="Carbon">CO2</div>
        <span class="impact-value">Carbon Neutral</span>
        <span class="impact-desc">Operations certified since 2025</span>
      </div>
      <div class="impact-card">
        <div class="impact-icon" aria-label="Diversity">DEI</div>
        <span class="impact-value">52% Diverse Leadership</span>
        <span class="impact-desc">Gender parity across all levels</span>
      </div>
      <div class="impact-card">
        <div class="impact-icon" aria-label="Data Privacy">GDPR</div>
        <span class="impact-value">Privacy First</span>
        <span class="impact-desc">SOC 2 Type II, GDPR, HIPAA compliant</span>
      </div>
      <div class="impact-card">
        <div class="impact-icon" aria-label="Community">CSR</div>
        <span class="impact-value">1% Pledge</span>
        <span class="impact-desc">Revenue donated to STEM education</span>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.esg-slide .impact-grid {
  margin-top: 48px;
  flex: 1;
  align-content: center;
}

.impact-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 48px 40px;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 16px;
}

.impact-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: var(--color-accent, #6c5ce7);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 24px;
}

.impact-value {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
}

.impact-desc {
  font-size: 22px;
  color: var(--color-text-muted, #555);
}
```

---

## 14. AI Strategy (2026)

**Description:** Communicates the company's AI architecture overview and key differentiator in a balanced split layout.

**Content density:** Max **50 words**. Max **4 elements** (visual area + headline + differentiator statement + optional bullets).

### HTML

```html
<section class="slide ai-slide">
  <div class="split split-50-50">
    <div class="visual-area">
      <!-- AI architecture diagram or illustration -->
      <div class="architecture-placeholder" data-diagram="ai-architecture"></div>
    </div>
    <div class="text-area">
      <h2>AI-Native Architecture</h2>
      <p class="differentiator">Our proprietary model pipeline delivers 10x faster inference at 1/3 the cost of generic LLM integrations.</p>
      <ul class="bullet-list">
        <li>Fine-tuned domain models, not wrapper APIs</li>
        <li>On-premise deployment option for regulated industries</li>
        <li>Continuous learning from anonymized usage data</li>
      </ul>
    </div>
  </div>
</section>
```

### CSS

```css
.ai-slide .visual-area {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg-dark, #1a1a2e);
  border-radius: 16px;
  padding: 40px;
  height: 920px;
}

.ai-slide .architecture-placeholder {
  width: 100%;
  height: 100%;
}

.ai-slide .text-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 20px;
}

.ai-slide .differentiator {
  font-size: 32px;
  font-weight: 600;
  color: var(--color-accent, #6c5ce7);
  line-height: 1.4;
  margin-bottom: 40px;
}

.ai-slide .bullet-list li {
  font-size: 26px;
}
```

---

## 15. Unit Economics (2026)

**Description:** Displays 4-6 SaaS health metrics as stat cards in a clean grid layout.

**Content density:** Max **40 words**. Max **6 stat cards** (NDR, CAC, LTV, Burn Multiple, Payback Period, Gross Margin).

### HTML

```html
<section class="slide economics-slide">
  <div class="slide-content">
    <h2>Unit Economics</h2>
    <div class="grid grid-3 economics-grid">
      <div class="stat-card">
        <span class="stat-card-value">135%</span>
        <span class="stat-card-label">Net Dollar Retention</span>
      </div>
      <div class="stat-card">
        <span class="stat-card-value">$1,200</span>
        <span class="stat-card-label">CAC</span>
      </div>
      <div class="stat-card">
        <span class="stat-card-value">$18,000</span>
        <span class="stat-card-label">LTV</span>
      </div>
      <div class="stat-card">
        <span class="stat-card-value">1.2x</span>
        <span class="stat-card-label">Burn Multiple</span>
      </div>
      <div class="stat-card">
        <span class="stat-card-value">8 mo</span>
        <span class="stat-card-label">Payback Period</span>
      </div>
      <div class="stat-card">
        <span class="stat-card-value">82%</span>
        <span class="stat-card-label">Gross Margin</span>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.economics-grid {
  margin-top: 60px;
  flex: 1;
  align-content: center;
}

.economics-grid .stat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 48px 32px;
  background: var(--color-bg-light, #f8f9fa);
  border-radius: 16px;
  border-left: none;
  border-bottom: 5px solid var(--color-accent, #6c5ce7);
}

.economics-grid .stat-card-value {
  font-size: 56px;
  font-weight: 800;
  color: var(--color-accent, #6c5ce7);
  line-height: 1.1;
}

.economics-grid .stat-card-label {
  font-size: 24px;
  font-weight: 600;
  color: var(--color-text-muted, #555);
  margin-top: 12px;
}
```

---

## 16. Breathing Room

**Description:** A cognitive reset slide with maximal whitespace. Contains only one element -- a quote, single stat, section title, or full-bleed visual.

**Content density:** Max **20 words**. Max **1 element**.

### HTML (Variant A -- Quote)

```html
<section class="slide breathing-slide">
  <div class="slide-content centered">
    <blockquote>
      "The best way to predict the future is to create it."
      <cite>-- Peter Drucker</cite>
    </blockquote>
  </div>
</section>
```

### HTML (Variant B -- Section Title)

```html
<section class="slide breathing-slide">
  <div class="slide-content centered">
    <h2 class="section-title">Traction</h2>
  </div>
</section>
```

### HTML (Variant C -- Single Stat)

```html
<section class="slide breathing-slide">
  <div class="slide-content centered">
    <span class="stat-number">10x</span>
    <span class="stat-label">faster than the industry average</span>
  </div>
</section>
```

### CSS

```css
.breathing-slide {
  background: var(--color-bg, #ffffff);
}

.breathing-slide .slide-content {
  gap: 24px;
}

.breathing-slide blockquote {
  font-size: 48px;
  font-weight: 300;
  font-style: italic;
  line-height: 1.4;
  max-width: 1200px;
  text-align: center;
  margin: 0;
  color: var(--color-text, #1a1a2e);
}

.breathing-slide blockquote cite {
  display: block;
  font-size: 24px;
  font-style: normal;
  font-weight: 400;
  color: var(--color-text-muted, #888);
  margin-top: 24px;
}

.breathing-slide .section-title {
  font-size: 72px;
  font-weight: 800;
  letter-spacing: -1px;
  color: var(--color-accent, #6c5ce7);
}

.breathing-slide .stat-number {
  font-size: 120px;
  font-weight: 800;
  color: var(--color-accent, #6c5ce7);
  line-height: 1.0;
}

.breathing-slide .stat-label {
  font-size: 32px;
  color: var(--color-text-muted, #555);
  max-width: 900px;
}
```

---

## Quick Reference Table

| Slide Type | Max Words | Max Elements | Layout | Primary Use |
|---|---|---|---|---|
| 1. Cover/Title | 20 | 4 (logo, name, tagline, author) | Centered, vertical stack | Opening, first impression |
| 2. Hero Metric | 10 | 2 (number, label) | Centered, full-slide | Single wow-factor number |
| 3. Problem | 60 | 5 (headline, 3 bullets, stat) | Top-down flow, dark bg | Pain point framing |
| 4. Solution | 50 | 5 (headline, 3 benefits, visual) | 60/40 split (text/visual) | Product introduction |
| 5. How It Works | 45 | 4 (headline, 3 steps) | Horizontal 3-column flow | Process explanation |
| 6. Market Size | 50 | 5 (headline, TAM/SAM/SOM, source) | Centered, concentric rings | Market validation |
| 7. Business Model | 60 | 5 (headline, 3-4 cards) | Card grid, centered | Revenue model |
| 8. Traction | 50 | 6 (headline, chart, 3-4 stats) | Chart left + stat sidebar | Growth evidence |
| 9. Competition | 60 | 6 (headline, table/matrix) | Feature comparison table | Differentiation |
| 10. Team | 60 | 5 people max | Horizontal grid | Credibility, expertise |
| 11. Financials | 60 | 6 (headline, chart, 3-4 assumptions) | 60/40 split (chart/text) | Revenue projections |
| 12. The Ask/CTA | 50 | 5 (amount, 3-4 bullets, milestones) | Centered, accent bg | Funding request |
| 13. ESG/Mission | 50 | 5 (headline, 3-4 cards) | 2x2 card grid | Impact, compliance |
| 14. AI Strategy | 50 | 4 (visual, headline, text, bullets) | 50/50 split (visual/text) | Technical differentiation |
| 15. Unit Economics | 40 | 6 stat cards max | 3x2 stat card grid | SaaS health metrics |
| 16. Breathing Room | 20 | 1 (quote, stat, title, or visual) | Centered, max whitespace | Cognitive reset |

---

## Usage Notes

1. **Splitting rule:** If content for any slide type exceeds the max words or max elements listed above, the generator MUST split into multiple slides of the same type. Never compress or shrink fonts below the defined minimums.

2. **CSS custom properties:** All color values use CSS custom properties with fallback defaults. Theme changes only require updating the property values, not the structural CSS.

3. **Charts and visuals:** Placeholder elements (`data-chart`, `data-diagram`) are replaced at render time by the charting engine. The CSS ensures containers are properly sized regardless of content.

4. **Print/PDF fidelity:** All dimensions are in fixed `px` to ensure 1:1 rendering in headless browser PDF generation. Never substitute with relative units.

5. **Accessibility:** All images require `alt` attributes. Icon placeholders use `aria-label`. Color contrast ratios should meet WCAG AA (4.5:1 for body text, 3:1 for large text).
