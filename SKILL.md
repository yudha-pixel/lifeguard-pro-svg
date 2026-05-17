---
name: lifeguard-pro-design
description: Use this skill to generate well-branded interfaces and assets for Lifeguard Pro, a professional Gmail Sidebar CRM extension. Contains essential design guidelines, colors, type (Myriad Pro Bold), fonts, assets, and UI kit components for prototyping the 300px Gmail sidebar.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

Key files to read first:
- README.md — full brand context, visual foundations, content fundamentals
- colors_and_type.css — all CSS variables for colors, type, spacing, radii
- ui_kits/gmail_sidebar/index.html — live interactive prototype (open to see the UI)
- ui_kits/gmail_sidebar/Components.jsx — shared React primitives to reuse

Core design rules to follow:
1. **300px fixed width** — all sidebar designs lock to this viewport
2. **Section headers** always use `▸ LABEL` pattern, ALL CAPS, semantic color per section type
3. **Color by section**: Activities=#C63C51, Notes=#C99026, Team=#2d4a8a, Contact=#cc2229, Chatter=#7c3f8c
4. **Myriad Pro Bold** for display/headings; DM Sans for body; JetBrains Mono for code/IDs
5. **Dark surfaces**: #0A0A0A canvas, #161616 cards, #1e1e1e inputs
6. **No emoji** in UI; no decorative gradients; crisp 1px borders at #2a2a2a
7. **Buttons**: navy #1a2744 primary fill; terracotta #E25B45 accent; ghost with #333 border
8. **Image assets** (PNG/SVG Base64) are used in production to render the dark aesthetic inside CardService — the HTML prototype shows the target design

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.
