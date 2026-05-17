# Lifeguard Pro Design System

## Overview

**Lifeguard Pro** (Lifeguard-Pro.org) is a water safety & rescue training company — "World Leader in Water Safety & Rescue." Their technology arm has built **Lifeguard Pro CRM**, a professional Gmail Sidebar extension built entirely on Google Apps Script (GAS), integrated directly into the Gmail interface. The sidebar connects to an Odoo CRM backend via REST API, with n8n automation and Google Sheets as supporting layers.

The sidebar provides sales reps with a "Superhuman-like" inbox experience: loading CRM context, managing opportunities, viewing contacts, logging notes/activities, and navigating the chatter timeline — all without leaving Gmail.

---

## Sources

- **Codebase:** `Sukmayudha/` (local mount) — Google Apps Script project with `CardService` UI, `src/ui/` tab components, API client, config, form parser, and Sheets integration.
- **Design Brief PDF:** `uploads/Asset Design System for Gmail Sidebar.pdf` — 13-page deck describing the "Asset-Driven Design System" strategy, signature colors, typography, visual hierarchy approach.
- **Logos:** `uploads/Lifeguard-Pro.png` (banner), `uploads/lifeguard_pro_logo.png` (circular emblem).

> Note: There is no Figma link provided. The codebase and PDF are the primary design sources.

---

## Product Description

**Single product:** The Gmail Sidebar CRM Panel — a 300px-wide Google Workspace Add-on sidebar that renders inside Gmail when an email is open.

**Five main tabs:**
1. **Preview** — Deal Quick Info, Contact Quick-Access, editable fields, Activities, Notes
2. **Full Deal** — Complete Odoo opportunity record with all fields
3. **Organization** — Company/org details
4. **All Contacts** — Related contacts list
5. **Chatter Box** — Log notes, conversation timeline (messages + activities merged)

**Supporting views:** Config screen, Create Opportunity, Create Contact, Pending state.

---

## CONTENT FUNDAMENTALS

### Tone & Voice
- **Efficient and directive.** No fluff. Every word earns its place.
- **Developer-centric but not cold.** Reads like a professional CLI, not a consumer app.
- **Command-style headings:** Section labels are ALL CAPS, prefixed with `▸`. Examples: `▸ ACTIVITIES`, `▸ NOTES`, `▸ DEAL QUICK INFO`
- **Labels before values** — field names are bolded, values follow on the next line.
- **Terse action labels:** "Save Quick Deal Info", "Load CRM Data", "Post Log Note", "Quick Add Activity"

### Casing
- Section headers: **ALL CAPS** (e.g. `DEAL QUICK INFO`, `CONTACT QUICK-ACCESS`)
- Button labels: **Title Case** (e.g. `Save`, `Create Opportunity`, `Test Connection`)
- Field labels: **Title Case with (Edit)** suffix for editable fields
- Status text: **Sentence case** (e.g. "No opportunities found.")

### Voice
- First-person is avoided. Direct imperative: "Open an email to use the CRM panel."
- No emoji. No decorative punctuation.
- Errors in red, warnings in gold, success in green — state is communicated by color.
- Timestamps shown as human-readable: "Loaded: Mon, May 18 2026 9:42 AM"

### Specific Copy Examples (from codebase)
- `"Open an email to use the CRM panel."`
- `"No opportunities found."`
- `"Contact created: John Smith"`
- `"Connection error"` / `"Create request sent. Refresh after n8n finishes."`
- `"Please check 'I confirm...' before creating the opportunity."`

---

## VISUAL FOUNDATIONS

### Color Palette

#### Signature (from PDF Design System)
| Name | Hex | Role |
|------|-----|------|
| Obsidian | `#0A0A0A` | Canvas / page background |
| Terracotta | `#E25B45` | Primary accent — CTAs, alerts, brand moments |
| Mint Frost | `#DAFFDE` | Secondary highlight — labels, success indicators |

#### Functional (from codebase)
| Name | Hex | Role |
|------|-----|------|
| Navy Primary | `#1a2744` | Button fill, primary headings, key labels |
| Navy Deep | `#1A365D` | Body text, secondary content |
| Steel Blue | `#2d4a8a` | Team section headers |
| Slate | `#415064` | Info sections, CRM meta |
| Danger Red | `#cc2229` | Errors, loading state, "DO NOT CONTACT" |
| Activities Crimson | `#C63C51` | Activities section header |
| Notes Gold | `#C99026` | Notes section header |
| Chatter Purple | `#7c3f8c` | Chatter Box section |
| Success Green | `#2e7d32` / `#188038` | Confirmed states, success messages |
| Muted Gray | `#5f6368` / `#6b7280` | Hint text, legacy fields, captions |

#### Surfaces
| Name | Hex | Role |
|------|-----|------|
| Surface 0 | `#0A0A0A` | Page background |
| Surface 1 | `#161616` | Card / panel backgrounds |
| Surface 2 | `#1e1e1e` | Raised surfaces, modals |
| Border | `#2a2a2a` | Divider lines |
| Border Accent | `#333333` | Subtle card borders |

### Typography

**Display / Headers:** Myriad Pro Bold — humanist sans-serif, confident and clean. Used for section titles, primary headings.
> ✅ **Font file:** `fonts/MYRIADPRO-BOLD.OTF` — Bold weight only. Use for display/heading roles. For lighter weights, fall back to DM Sans until additional cuts are supplied.

**Body:** DM Sans — clean, neutral, optimized for small sizes in sidebar.

**Monospace:** JetBrains Mono — developer-centric, used for IDs, URLs, code values.

**Sizes (300px sidebar context):**
- Section heading (▸ LABEL): 11px, bold, letter-spacing: 0.08em
- Field label: 11px, semibold
- Field value: 13px, regular
- Button text: 13px, medium
- Caption / hint: 11px, muted

### Backgrounds & Surfaces
- **No gradients on backgrounds.** Pure `#0A0A0A` canvas.
- Cards/sections use `#161616`–`#1e1e1e` surface fills.
- Top-accent borders in Terracotta or Mint Frost signal priority sections.
- Subtle `1px` solid borders in `#2a2a2a`.

### Spacing & Layout
- **Fixed 300px width** — all assets designed at exactly this viewport.
- Sections separated by text-based dividers (underscores rendered as HTML font tags, not CSS `<hr>`).
- Padding: 12–16px horizontal, 8–12px vertical per section.
- Field rows: 4px gap between label and value.

### Borders & Corner Radii
- Cards: `border-radius: 8px`
- Buttons: `border-radius: 6px`
- Inputs: `border-radius: 4px`
- All borders: `1px solid #2a2a2a` (subtle) or `1px solid #333` (card)

### Shadow System
- Minimal. Depth expressed via surface color contrast, not drop shadows.
- Image-based buttons may include embedded glows/highlights via PNG assets.

### Animations
- **None.** Google Apps Script CardService has no CSS animation support.
- Transitions are handled by GAS load indicators (spinner).

### Hover & Press States
- Hover: Google's native CardService hover (cannot be customized in CardService).
- In HTML Service views: opacity decrease on hover (`opacity: 0.85`), no color shift.
- Active: subtle darkening.

### Section Header Pattern
Every section uses the same visual grammar:
```
___________________________ (divider)

▸ SECTION TITLE  (colored, bold, uppercase)
```
Color is semantic per section type.

### Iconography
See ICONOGRAPHY section below.

### Imagery
- The brand logo (circular emblem + banner wordmark) uses a red/white/navy color palette from the physical brand.
- In the digital sidebar, the logo is served as a hosted image URL via Google Drive or Odoo CDN.
- No decorative illustrations in the sidebar UI.
- Dividers can use ornamental image assets (e.g. floral/geometric PNG patterns per PDF p.6).

---

## ICONOGRAPHY

- **No icon font or SVG sprite system** in the current GAS implementation.
- Section labels use **Unicode arrow** `▸` (U+25B8) as a pseudo-icon — this is the primary "icon" in the system.
- Action-state icons: `↻` (refresh), `‹` / `›` (pagination).
- The PDF uses Lucide-style emoji icons (palette 🎨, lightning ⚡, resize ⛶) for presentation — these are **not** used in the production sidebar.
- **No emoji** in the sidebar UI.
- For the web/HTML-based UI kit, **Lucide Icons** (CDN) are used as the closest matching system — thin, 1.5px stroke weight, consistent geometric style.

---

## File Index

```
/
├── README.md                          ← This file
├── SKILL.md                           ← Agent skill — loadable in Claude Code
├── colors_and_type.css                ← All CSS vars: colors, type, spacing, radii
├── fonts/
│   └── MYRIADPRO-BOLD.OTF            ← Brand display font (Bold weight)
├── assets/
│   ├── lifeguard_pro_logo.png         ← Circular emblem (round badge)
│   ├── Lifeguard-Pro-banner.png       ← Horizontal banner wordmark
│   └── Lifeguard-Pro-banner-2.png    ← Alternate banner (navy/red/white)
├── preview/                           ← Design System tab cards (12 cards)
│   ├── colors-brand.html              ← Navy · Red · White — from logo
│   ├── colors-functional.html         ← Section semantic colors
│   ├── colors-surfaces.html           ← Surface scale tokens
│   ├── colors-semantic.html           ← Section → color map
│   ├── type-scale.html                ← Full type scale (Myriad Pro + DM Sans + Mono)
│   ├── type-specimens.html            ← Type in context
│   ├── spacing-tokens.html            ← Spacing scale + border radii
│   ├── components-buttons.html        ← Button variants + tab nav
│   ├── components-section-headers.html← ▸ SECTION pattern, all 6 types
│   ├── components-fields.html         ← Field pairs + editable inputs
│   ├── components-badges.html         ← Status badges + boolean indicators
│   └── brand-logos.html               ← Logo assets with usage notes
└── ui_kits/
    └── gmail_sidebar/
        ├── README.md                  ← Kit overview, screens, mock data
        ├── index.html                 ← Interactive Gmail mock + sidebar prototype
        ├── Components.jsx             ← Shared primitives (exported to window)
        ├── PreviewTab.jsx             ← Preview tab: Activities, Notes, Deal Info
        ├── FullDealTab.jsx            ← Full Deal, Organization, All Contacts tabs
        ├── ChatterBoxTab.jsx          ← Chatter Box: log note + timeline
        └── Sidebar.jsx                ← Shell card, header, tab router
```
