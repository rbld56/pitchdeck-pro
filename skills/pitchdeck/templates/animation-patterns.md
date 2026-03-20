# Animation Patterns Reference

## Mode Behavior

- **PDF Mode:** Animations are disabled via `@media print` in slide-base.css. Design must work statically. These patterns are still useful as they degrade gracefully.
- **HTML Interactive Mode:** Animations are **THE feature**. Every content slide should use reveal animations. Scroll-driven effects, animated counters, and interactive hover states are expected and encouraged. Use ALL patterns in this file.

## When to Animate (HTML Mode)

In HTML Interactive mode, animation is not decoration — it IS the experience:
1. **Every content element** should reveal on slide entry (`.reveal`, `.reveal-scale`, `.reveal-left`)
2. **Metrics and numbers** should use animated counters (count from 0 to value)
3. **Charts** should draw/grow into view
4. **Navigation** should feel smooth (scroll-snap + progress bar)
5. **Hover states** on cards and interactive elements add depth
6. Use **staggered delays** for sequential content (0.1s increments)

In PDF mode, these same classes simply show all content immediately.

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

---

## HTML Interactive Mode: Advanced Patterns

These patterns are specifically for HTML Interactive mode. They require JavaScript and/or CSS 2026 features.

### Animated Counter (Traction/Metric slides)

```javascript
/* Animates a number from 0 to target value on slide entry */
function animateCounter(element, target, duration = 1500, prefix = '', suffix = '') {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const start = performance.now();
                function update(now) {
                    const progress = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - progress, 3);
                    element.textContent = prefix + Math.floor(target * eased).toLocaleString('de-DE') + suffix;
                    if (progress < 1) requestAnimationFrame(update);
                }
                requestAnimationFrame(update);
                observer.unobserve(element);
            }
        });
    }, { threshold: 0.5 });
    observer.observe(element);
}

// Usage:
// animateCounter(document.querySelector('.revenue'), 2400000, 1500, '€', '');
// animateCounter(document.querySelector('.growth'), 142, 1200, '', '%');
```

### Scroll-Driven Progress Bar (CSS-only, Chrome 115+, Safari 18+)

```css
.progress-bar {
    position: fixed;
    top: 0; left: 0;
    height: 3px;
    background: var(--color-accent);
    z-index: 10000;
    transform-origin: left;
    animation: progress-grow linear;
    animation-timeline: scroll(root);
}
@keyframes progress-grow {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
}
```

### 3D Card Tilt on Hover

```javascript
document.querySelectorAll('.tilt-card').forEach(card => {
    card.style.transformStyle = 'preserve-3d';
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(800px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg)`;
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(800px) rotateY(0) rotateX(0)';
    });
});
```

### Gradient Shift Background (subtle color animation)

```css
@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.gradient-shift-bg {
    background: linear-gradient(135deg,
        var(--color-accent-muted),
        var(--color-bg),
        var(--color-success-muted, rgba(56,161,105,0.1))
    );
    background-size: 200% 200%;
    animation: gradient-shift 15s ease infinite;
}
```

### Typewriter Effect (for taglines)

```css
.typewriter {
    overflow: hidden;
    border-right: 3px solid var(--color-accent);
    white-space: nowrap;
    animation: typing 2s steps(40) 0.5s both, blink-caret 0.8s step-end infinite;
    width: 0;
}
@keyframes typing { from { width: 0; } to { width: 100%; } }
@keyframes blink-caret { 50% { border-color: transparent; } }
```

### Bar Chart Growth Animation

```css
.bar-fill {
    transform-origin: left;
    transform: scaleX(0);
    transition: transform 0.8s var(--ease-out-expo);
}
.slide.visible .bar-fill {
    transform: scaleX(1);
}
```
