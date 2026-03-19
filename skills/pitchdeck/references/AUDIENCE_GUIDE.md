# Audience-Specific Design Adaptations

Reference guide for the pitchdeck-pro plugin. Provides concrete specifications for adapting
pitch decks to four primary audiences. Each section contains actionable design, content,
and delivery constraints.

---

## 1. VC Investors (Series A-C)

### Format Specifications

| Parameter | Specification |
|-----------|--------------|
| **Slide count** | 10-15 slides (core deck). Appendix up to 10 additional slides. |
| **Delivery format** | Static PDF via DocSend (preferred) or email attachment. Never Google Slides link for cold outreach. |
| **Aspect ratio** | 16:9 |
| **File size** | Under 10 MB. Optimize images. No embedded video files -- use QR codes or links. |
| **Resolution** | Export at 150 DPI minimum. 300 DPI for print-ready versions. |

### Design Language

| Element | Specification |
|---------|--------------|
| **Palette** | Muted, sophisticated. 1 primary brand color + 1 accent + neutral grays. Avoid neon, rainbow gradients, or overly saturated schemes. Reference: Linear, Notion, Stripe design language. |
| **Typography** | Modern sans-serif (Inter, Satoshi, General Sans, Geist). Max 2 font families. Title: 28-36pt. Body: 16-20pt. Captions: 12-14pt. |
| **Data visualization** | Traction slides are data-dense by design. Use clean charts (line, bar) with labeled axes. Start Y-axis at zero unless explicitly justified. Annotate inflection points. |
| **Imagery** | Product screenshots (high-res, framed in device mockups). No stock photos of people shaking hands. No clipart. |
| **Layout** | Generous whitespace. One idea per slide. Left-aligned text (not centered paragraphs). |

### Content Requirements

| Element | Specification |
|---------|--------------|
| **Metric focus** | ARR/MRR and growth rate (MoM or YoY). Net Dollar Retention (NDR). CAC payback period in months. LTV:CAC ratio. Gross margin. Burn multiple. |
| **Traction proof** | Revenue chart with time axis. Cohort retention curves. Logo garden of notable customers (with permission). |
| **Ask slide** | Specific dollar amount. Round type. Use of funds in 3-4 buckets with percentages. 18-month milestones the funding unlocks. |

### Prohibitions

- No corporate PowerPoint templates with footer bars and page numbers on every slide.
- No clipart or generic icons from free icon packs.
- No complex org charts (save for appendix if needed).
- No "Questions?" as the final slide. End on The Ask or Vision.
- No "Thank You" slide. The last slide should make the investor want to respond, not leave.
- No animations or transitions in the PDF version.
- No "confidential" watermarks on every page (one notice on cover is sufficient).

### Pre-Send Protocol

- Send as static PDF (no animations, no builds).
- Include a 2-3 sentence email body summarizing the ask and one traction highlight.
- Attach appendix as a separate PDF or include after a clear "Appendix" divider slide.
- If using DocSend: enable download, disable email gate for warm intros.
- Include detailed financials in the appendix, not the core deck.

---

## 2. B2B Enterprise Customers

### Format Specifications

| Parameter | Specification |
|-----------|--------------|
| **Slide count** | 15-25 slides. Enterprise buyers expect comprehensiveness. |
| **Delivery format** | PDF for initial send. PowerPoint (.pptx) for internal circulation -- enterprise buyers need to extract slides for internal business cases and procurement workflows. |
| **Aspect ratio** | 16:9 |
| **File size** | Under 15 MB. PowerPoint version may be larger due to editable elements. |

### Design Language

| Element | Specification |
|---------|--------------|
| **Palette** | Professional, structured. Your brand colors + neutral backgrounds. Avoid startup-casual aesthetics. |
| **Trust signals** | Security and compliance badges prominent on early slides: SOC 2 Type II, GDPR, ISO 27001, HIPAA (if applicable). Certifications in footer or dedicated slide. |
| **Typography** | Professional sans-serif. Slightly smaller body text acceptable (14-18pt) due to higher information density expectations. |
| **Imagery** | Architecture diagrams, integration flow charts, implementation timelines. Named customer logos and case study visuals. |

### Required Slides (beyond standard pitch structure)

| Slide Type | Key Content |
|-----------|-------------|
| **Case Studies (2-3 slides)** | Named customer (with permission), their challenge, your solution, quantified ROI (percentage improvement, dollars saved, time reduced). Include customer quote if available. Each case study on its own slide. |
| **Integration Architecture** | Diagram showing how your product connects to the buyer's existing stack (CRM, ERP, data warehouse, SSO provider). List supported protocols, APIs, and pre-built connectors. |
| **Implementation Timeline** | Phased rollout plan. Typical: Phase 1 (pilot, 2-4 weeks), Phase 2 (department rollout, 4-8 weeks), Phase 3 (enterprise-wide, 8-16 weeks). Include milestones, deliverables, and responsible parties. |
| **Security & Compliance** | Data residency options, encryption standards (at rest and in transit), access controls (RBAC, SSO/SAML), audit logging, penetration testing cadence, incident response SLA. |
| **Support Model & SLAs** | Tier structure (Standard, Premium, Enterprise). Response time SLAs by severity. Dedicated CSM availability. Training and onboarding included. Escalation path. |

### Content Tone

- Outcome-focused, not feature-focused. Frame everything as business impact.
- Use the buyer's language (e.g., "reduce time-to-close" not "AI-powered automation").
- Address the internal champion's need to sell upward -- give them the slides and data points they need.
- Include ROI calculator or TCO comparison if competing against build-vs-buy or incumbent replacement.

---

## 3. Board / C-Level

### Format Specifications

| Parameter | Specification |
|-----------|--------------|
| **Slide count** | 20-30 slides. Thoroughness is expected. |
| **Delivery format** | PowerPoint (.pptx) for quarterly consistency. Accompany with a 1-2 page executive memo (PDF) summarizing key decisions needed. |
| **Aspect ratio** | 16:9 |
| **Pre-read** | Send 48 hours before the meeting. Board members read in advance. The meeting is for discussion, not presentation. |

### Design Language

| Element | Specification |
|---------|--------------|
| **Palette** | Match brand guidelines exactly. Consistent quarter after quarter -- board members notice template changes. |
| **Data density** | High. Dashboard-style layouts with multiple KPIs per slide. RAG indicators (Red/Amber/Green) for status-at-a-glance. |
| **Typography** | Consistent with prior quarters. If the board has seen Calibri for 8 quarters, do not switch to Inter. |
| **Charts** | Actuals vs. plan vs. prior year. Trend lines with 3-6 month history minimum. Variance callouts. |

### Required Slides

| Slide Type | Key Content |
|-----------|-------------|
| **Executive Summary** | First slide after cover. 5-7 bullet points covering: performance vs. plan, key wins, key risks, decisions needed from the board. This slide must stand alone. |
| **KPI Dashboard** | All key metrics vs. targets. RAG status. MoM and QoQ trends. Include: revenue, burn rate, runway, headcount, pipeline, NPS/CSAT, churn. |
| **Departmental Performance** | One slide per major function (Engineering, Sales, Marketing, Customer Success, Operations). Metrics + narrative. |
| **Financial Review** | P&L actual vs. budget. Cash flow statement. Balance sheet summary. Runway in months. Key variances explained. |
| **Risk Register** | Top 5-10 risks. Each with: description, likelihood, impact, mitigation status, owner. Use a risk matrix visual if helpful. |
| **Strategic Initiatives** | Status of board-approved initiatives. Progress vs. milestones. Resource allocation. Blockers requiring board input. |
| **Decisions Needed** | Explicit list of items requiring board vote or guidance. Frame each with context, options, and management recommendation. |

### Consistency Rules

- Use the same template every quarter. Do not redesign.
- Metrics must be calculated the same way quarter over quarter. If methodology changes, flag it explicitly.
- Slide order should be predictable. Board members navigate by muscle memory.
- Number all slides. Board members reference by slide number in discussion.
- Include a "Changes Since Last Board Meeting" slide if anything material shifted between the pre-read send and the meeting.

---

## 4. DACH / European Audience

### Cultural Adaptations

| Aspect | Specification |
|--------|--------------|
| **Text density** | 20-30% more text is acceptable and expected compared to US decks. German words are longer than English, and German-speaking audiences expect substance over flash. |
| **Tone** | Formal, structured, understated. Avoid superlatives ("revolutionary," "game-changing," "disruptive"). Use precise, measured language. "Signifikante Verbesserung" over "massive improvement." |
| **Credibility signals** | University partnerships (name the institution and professor). Industry certifications. EU and national regulatory compliance. Institutional backing (KfW, BAFA, EU Horizon). Published research or peer-reviewed validations. |
| **Hype avoidance** | No Silicon Valley hyperbole. Do not claim to be "the Uber of X." European investors are skeptical of exaggerated claims. Let the data speak. |

### Design Language

| Element | Specification |
|---------|--------------|
| **Palette** | Conservative, Swiss-inspired. Primary: deep blue (#1a365d to #2b4c7e). Secondary: warm gray (#6b7280 to #9ca3af). Accent: teal or muted green for positive indicators. Avoid bright primary colors. |
| **Typography** | Clean European sans-serif (Inter, Source Sans Pro, Fira Sans). Slightly smaller point sizes acceptable due to higher text density tolerance. |
| **Layout** | Structured grids. Clear visual hierarchy. Tables are welcomed more than in US decks. Infographic-style data presentation. |
| **Imagery** | Real product screenshots, architectural diagrams, process flows. European audiences value substance over polish. |

### Foerderantrag Culture

European fundraising (especially in Germany, Austria, Switzerland) is influenced by a grant-application mindset. Investors expect:

| Expectation | How to Address |
|-------------|---------------|
| **Thoroughness** | Cover all aspects of the business. Gaps are interpreted as lack of preparation, not as brevity. |
| **Risk mitigation** | Include a risk section with mitigation strategies. Show you have thought about what could go wrong. |
| **Regulatory compliance** | Address GDPR, AI Act, sector-specific regulations proactively. Show compliance roadmap. |
| **Financial conservatism** | Projections should be defensible and conservative. Include bear/base/bull scenarios. |
| **References and evidence** | Cite sources for market data. Name pilot customers. Reference academic validation. |

### Bilingual Considerations

If the deck serves both German and English audiences:

- **Option A (preferred):** Maintain two separate decks. Use the same structure and data but adapt language, tone, and cultural framing.
- **Option B:** English deck with German executive summary slide and German appendix. Acceptable for international rounds with DACH participation.
- **Option C:** German deck with English financial terminology kept as-is (ARR, MRR, CAC, LTV are understood in English across DACH markets).
- **Avoid:** Mixed-language slides where German and English appear on the same slide in a haphazard way.

### DACH-Specific Extra Slides

| Slide Type | Key Content |
|-----------|-------------|
| **Regulatory & Compliance** | GDPR compliance status, AI Act readiness, sector-specific regulations (MedTech: MDR, FinTech: BaFin, etc.). Data residency (EU-hosted). |
| **Foerdermittel & Grants** | If applicable: grants received or applied for (EXIST, ZIM, Horizon Europe, INVEST). Signals institutional validation. |
| **Academic & Research Partnerships** | University collaborations, research projects, published papers. Highly valued in DACH ecosystem. |

---

## Pre-Send Checklist

Apply this checklist before sending any deck to any audience. Every item must pass.

### Content Check

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | **Title scan test** | The business is understandable from reading slide titles alone, in sequence. |
| 2 | **Problem resonance** | The problem slide creates an emotional reaction, not just intellectual understanding. |
| 3 | **Traction prominence** | The strongest traction metric is visible within the first 5 slides. |
| 4 | **Ask clarity** | The ask slide specifies: exact amount, use of funds (3-4 buckets), and milestones. No ambiguity. |
| 5 | **Jargon check** | No undefined acronyms. No insider terminology without explanation. |
| 6 | **Claim substantiation** | Every claim has a data point, source, or customer reference backing it. |

### Design Check

| # | Check | Pass Criteria |
|---|-------|---------------|
| 7 | **Mobile readability** | Every slide is readable on a phone screen (investors often first-scan on mobile). Text minimum 14pt effective. |
| 8 | **Font consistency** | Maximum 2 font families used. Consistent sizing hierarchy throughout. |
| 9 | **Color consistency** | Maximum 3 colors plus neutrals. Same colors mean the same things throughout. |
| 10 | **Word count** | No slide exceeds 30 words of body text (excluding labels and data). Titles are under 8 words. |
| 11 | **Image quality** | All images are high-resolution. No pixelated screenshots. No stretched logos. |
| 12 | **Chart integrity** | All charts have labeled axes. Y-axis starts at zero (unless log scale is explicitly justified). No 3D charts. No dual-axis charts unless clearly labeled. |
| 13 | **Contrast ratio** | Text meets WCAG AA contrast ratio (4.5:1 for body text, 3:1 for large text). Test with a contrast checker. |

### Narrative Check

| # | Check | Pass Criteria |
|---|-------|---------------|
| 14 | **Story arc** | The deck follows a clear narrative progression: tension (problem) to relief (solution) to proof (traction) to trust (team) to action (ask). |
| 15 | **Emotional arc** | The deck creates emotional movement. The audience should feel: concern (problem) to excitement (solution) to confidence (traction/team) to urgency (ask). |
| 16 | **Breathing slides** | Every 3-4 dense slides are followed by a visual or transitional slide that gives the audience a moment to absorb. Full-bleed images, bold quotes, or section dividers. |
| 17 | **Opening hook** | The first 3 slides (after cover) create enough intrigue to ensure the investor reads slide 4. |
| 18 | **Closing momentum** | The last 3 slides build toward the ask with increasing confidence and specificity. The deck does not "trail off." |

### Audience-Specific Final Check

| Audience | Additional Check |
|----------|-----------------|
| **VC Investors** | Is there a static PDF version with no animations? Is the file under 10MB? Is the appendix separated or clearly divided? |
| **B2B Enterprise** | Is there a .pptx version for internal circulation? Are case studies included with ROI numbers? Are compliance badges visible? |
| **Board / C-Level** | Is the template identical to last quarter? Are all metrics calculated consistently? Is the executive summary slide self-contained? Is the pre-read sent 48 hours early? |
| **DACH / European** | Is the tone measured and formal? Are credibility signals (academic, institutional) included? Are financial projections conservative with scenarios? Is regulatory compliance addressed? |
