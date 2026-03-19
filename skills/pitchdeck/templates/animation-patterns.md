# Animation Patterns Reference (HTML Preview Only)

These animations are for the HTML preview experience. They are automatically disabled in PDF output via `@media print` in slide-base.css.

## When to Animate

Animation should ONLY be used to:
1. Direct the eye to a specific data point
2. Show a relationship between two objects
3. Signal a major shift in the narrative

**Animations for pure visual appeal DISTRACT.** Use motion sparingly and purposefully.

## Timing Standards

- Duration: 200–600ms (never over 800ms)
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (fast start, gentle stop)
- Stagger delay: 100–150ms between sequential elements
- Max simultaneously animating elements: 3–4 per slide

## Entrance Animations

```css
/* Fade + Slide Up (default, most versatile) */
.reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s var(--ease-out-expo),
                transform 0.6s var(--ease-out-expo);
}
.slide.visible .reveal {
    opacity: 1;
    transform: translateY(0);
}

/* Scale In (for stat cards, logos) */
.reveal-scale {
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}
.slide.visible .reveal-scale {
    opacity: 1;
    transform: scale(1);
}

/* Slide from Left (for split layouts) */
.reveal-left {
    opacity: 0;
    transform: translateX(-40px);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}
.slide.visible .reveal-left {
    opacity: 1;
    transform: translateX(0);
}
```

## Stagger Pattern

```css
/* Sequential reveal for child elements */
.reveal:nth-child(1) { transition-delay: 0.1s; }
.reveal:nth-child(2) { transition-delay: 0.2s; }
.reveal:nth-child(3) { transition-delay: 0.3s; }
.reveal:nth-child(4) { transition-delay: 0.4s; }
```

## Animated Counter (JS, for Traction/Metric slides)

```javascript
function animateValue(element, start, end, duration = 1500) {
    const range = end - start;
    const startTime = performance.now();
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        const value = Math.floor(start + range * eased);
        element.textContent = value.toLocaleString();
        if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
}

// Usage: animateValue(document.querySelector('.stat-number'), 0, 2400000, 1500);
```

## Effect-to-Feeling Guide

| Feeling | Animation Style | Speed |
|---------|----------------|-------|
| Dramatic / Cinematic | Slow fade-ins (1s), scale 0.9→1 | Slow |
| Professional / Corporate | Subtle fast fades (200–300ms) | Fast |
| Calm / Minimal | Gentle fades, no transforms | Very slow |
| Energetic / Bold | Quick slide-ups, staggered | Medium |
| Data / Analytical | Counter animations, bar growth | Medium |

## Background Effects (CSS-only)

```css
/* Subtle gradient mesh */
.gradient-bg {
    background:
        radial-gradient(ellipse at 20% 80%, rgba(120, 0, 255, 0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 255, 200, 0.04) 0%, transparent 50%),
        var(--bg-primary);
}

/* Noise texture overlay */
.noise-bg::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
}

/* Subtle grid pattern */
.grid-bg {
    background-image:
        linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
}
```

## Print Safety

All animations automatically resolve to their end state in PDF:

```css
@media print {
    .reveal, .reveal-scale, .reveal-left {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
    }
}
```

This is already included in slide-base.css — no additional print styles needed in animation code.
