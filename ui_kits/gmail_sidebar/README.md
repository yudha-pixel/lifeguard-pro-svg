# Gmail Sidebar UI Kit

High-fidelity interactive prototype of the Lifeguard Pro CRM Gmail Sidebar.

## What this is

A React-based click-through simulation of the Google Apps Script sidebar, rendered inside a mock Gmail interface. Demonstrates the intended dark-mode aesthetic (achieved in production via Base64-encoded image assets inside CardService).

## Screens & Tabs

| View | Description |
|------|-------------|
| **Shell Card** | Initial state — email context (FROM/EMAIL/SUBJECT) + "Load CRM Data" button with spinner |
| **Preview Tab** | Activities, Notes, Deal Quick Info (editable), Team, Contact Quick-Access, Save |
| **Full Deal Tab** | Complete opportunity record — all fields with inline editing |
| **Organization Tab** | Company/org details |
| **All Contacts Tab** | Related contacts list |
| **Chatter Box Tab** | Log Note composer + expandable conversation timeline |

## Files

```
index.html          ← Entry point — Gmail mock + React mount
Components.jsx      ← Shared primitives: SectionHeader, FieldPair, Buttons, Inputs, TabBar
PreviewTab.jsx      ← Preview tab (Activities, Notes, Deal Quick Info, Team, Contact)
FullDealTab.jsx     ← Full Deal + Organization + All Contacts tabs
ChatterBoxTab.jsx   ← Chatter Box composer + timeline
Sidebar.jsx         ← Main shell: ShellCard, SidebarHeader, tab router
```

## Design Viewport

**300px sidebar** fixed width, matching the Gmail Add-on constraint.

## Mock Data

The prototype uses a fictional opportunity: **"Red Rooster Cafe — Group Certification"**
- Contact: Franklin Rodriguez, f.rodriguez@redroostercafe.com
- Revenue: $12,000 · Stage: Qualified Lead · Probability: 45%

## Fonts

- Display: Myriad Pro Bold (`../../fonts/MYRIADPRO-BOLD.OTF`)
- Body: DM Sans (Google Fonts)
- Mono: JetBrains Mono (Google Fonts)
