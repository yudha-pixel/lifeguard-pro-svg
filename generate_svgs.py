"""
generate_svgs.py
Generates 34 SVG assets (section headers + field labels) for the
Lifeguard Pro Gmail Sidebar design system.

Output folder: svg/  (created at workspace root alongside this script)
Font:          fonts/MYRIADPRO-BOLD.OTF  (base64-embedded in each SVG)
"""

import base64
import os
import pathlib

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR = pathlib.Path(__file__).parent
FONT_PATH  = SCRIPT_DIR / "fonts" / "MYRIADPRO-BOLD.OTF"
OUT_DIR    = SCRIPT_DIR / "svg"

# ── Font embed ───────────────────────────────────────────────────────────────
with open(FONT_PATH, "rb") as f:
    FONT_B64 = base64.b64encode(f.read()).decode("utf-8")

FONT_FACE = f"""@font-face {{
  font-family: 'MyriadPro';
  src: url('data:font/opentype;base64,{FONT_B64}') format('opentype');
  font-weight: 700;
  font-style: normal;
}}"""

# ── Color / gradient constants ────────────────────────────────────────────────
NAVY      = "#1a2744"
RED       = "#B91C1C"
WHITE     = "#FFFFFF"
PALE_BLUE = "#93C5FD"

# ── Asset definitions ─────────────────────────────────────────────────────────
#  (filename_stem, display_text, width, height, font_size, text_x, text_y)
#  Headers: 320×32, prefix ▸ already in text, font 13px, left-padded 10px
#  Labels:  320×20, no prefix, font 10px, left-padded 8px

HEADERS = [
    # (stem, text, bg_color)
    # Contact group — Red
    ("header_contact",              "&#9658; CONTACT",              "#B91C1C"),
    ("header_contact_info",         "&#9658; CONTACT INFO",         "#B91C1C"),
    ("header_contact_quick_access", "&#9658; CONTACT QUICK-ACCESS", "#B91C1C"),
    ("header_contact_details",      "&#9658; CONTACT DETAILS",      "#B91C1C"),
    ("header_create_contact",       "&#9658; CREATE CONTACT",       "#B91C1C"),
    ("header_person",               "&#9658; PERSON",               "#B91C1C"),
    # Opportunities / Deal group — Navy blue
    ("header_opportunities",        "&#9658; OPPORTUNITIES",        "#1E40AF"),
    ("header_deal",                 "&#9658; DEAL",                 "#1E40AF"),
    ("header_deal_quick_info",      "&#9658; DEAL QUICK INFO",      "#1E40AF"),
    ("header_deal_details",         "&#9658; DEAL DETAILS",         "#1E40AF"),
    ("header_lead_details",         "&#9658; LEAD DETAILS",         "#1E40AF"),
    ("header_create_opportunity",   "&#9658; CREATE OPPORTUNITY",   "#4338CA"),
    # Activities group — Amber
    ("header_activities",           "&#9658; ACTIVITIES",           "#B45309"),
    ("header_quick_add_activity",   "&#9658; QUICK ADD ACTIVITY",   "#B45309"),
    # Notes / Chatter group — Purple
    ("header_notes",                "&#9658; NOTES",                "#6D28D9"),
    ("header_add_log_note",         "&#9658; ADD LOG NOTE",         "#6D28D9"),
    ("header_conversation_timeline","&#9658; CONVERSATION TIMELINE","#6D28D9"),
    # Organization group — Teal
    ("header_organization",         "&#9658; ORGANIZATION",         "#0F766E"),
    ("header_organization_details", "&#9658; ORGANIZATION DETAILS", "#0F766E"),
    # Dates / Initial Contact — Orange
    ("header_dates_deadlines",      "&#9658; DATES &amp; DEADLINES","#C2410C"),
    ("header_initial_contact",      "&#9658; INITIAL CONTACT",      "#C2410C"),
    # Form Submission — Green
    ("header_form_submission",      "&#9658; FORM SUBMISSION",      "#15803D"),
    # Odoo CRM — Dark slate
    ("header_odoo_crm",             "&#9658; ODOO CRM",             "#1a2744"),
    # Team — Cyan
    ("header_team",                 "&#9658; TEAM",                 "#0369A1"),
    # Legacy / structural sub-headers — Gray
    ("header_legacy_fields",        "&#9658; LEGACY FIELDS",        "#4B5563"),
    ("header_header",               "&#9658; HEADER",               "#4B5563"),
    ("header_address",              "&#9658; ADDRESS",              "#4B5563"),
    ("header_left_column",          "&#9658; LEFT COLUMN",          "#4B5563"),
    ("header_left_column_legacy",   "&#9658; LEFT COLUMN - LEGACY", "#4B5563"),
    ("header_right_column",         "&#9658; RIGHT COLUMN",         "#4B5563"),
]

LABELS = [
    ("label_from",         "FROM"),
    ("label_email",        "EMAIL"),
    ("label_subject",      "SUBJECT"),
    ("label_name",         "NAME"),
    ("label_phone",        "PHONE"),
    ("label_company",      "COMPANY"),
    ("label_location",     "LOCATION"),
    ("label_course",       "COURSE"),
    ("label_date",         "DATE"),
    ("label_interested",   "INTERESTED IN"),
    ("label_message",      "MESSAGE"),
    ("label_url",          "URL"),
    ("label_user",         "USER"),
    ("label_google_sheet",    "GOOGLE SHEET"),
    ("label_sender_email",    "SENDER EMAIL"),
    ("label_sender_name",     "SENDER NAME"),
    ("label_opportunity_name","OPPORTUNITY NAME"),
    ("label_confirmation",    "CONFIRMATION"),
]

DIVIDERS = [
    ("divider_red",   "#B91C1C"),  # Contact / danger sections
    ("divider_navy",  "#1a2744"),  # Deal sections
    ("divider_gold",  "#C99026"),  # Activities / notes
    ("divider_teal",  "#2d7d6e"),  # Organization sections
    ("divider_pink",  "#D95A8A"),  # Person / contact sections
    ("divider_gray",  "#6b7280"),  # Legacy fields
]

BUTTONS = [
    ("btn_save",   "SAVE"),
    ("btn_cancel", "CANCEL"),
    ("btn_submit", "SUBMIT"),
    ("btn_create", "CREATE"),
    ("btn_update", "UPDATE"),
]


def make_divider_svg(color: str, width: int = 320, height: int = 4) -> str:
    """Return SVG markup for a solid thin divider line."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <rect width="{width}" height="{height}" fill="{color}" rx="1" ry="1"/>
</svg>"""


def make_button_svg(text: str, width: int = 150, height: int = 36) -> str:
    """Return SVG markup for a white-background action button with red border and text."""
    radius = 4
    border = 2
    font_size = 14
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <defs>
    <style>{FONT_FACE}</style>
  </defs>
  <!-- white button background with red border -->
  <rect x="{border/2}" y="{border/2}"
        width="{width - border}" height="{height - border}"
        rx="{radius}" ry="{radius}"
        fill="{WHITE}" stroke="{RED}" stroke-width="{border}"/>
  <!-- button label -->
  <text
    x="{width // 2}"
    y="{height // 2}"
    font-family="MyriadPro, 'Myriad Pro', Arial, sans-serif"
    font-weight="700"
    font-size="{font_size}"
    fill="{RED}"
    dominant-baseline="middle"
    text-anchor="middle"
    letter-spacing="1">{text}</text>
</svg>"""


def make_svg(text: str, width: int, height: int, font_size: int,
             text_x: int, text_y: float, bg_color: str = NAVY) -> str:
    """Return SVG markup for one asset."""
    grad_id = "bg"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <defs>
    <style>{FONT_FACE}</style>
    <linearGradient id="{grad_id}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{bg_color}"  stop-opacity="1"/>
      <stop offset="50%"  stop-color="{bg_color}"  stop-opacity="1"/>
      <stop offset="100%" stop-color="{bg_color}"  stop-opacity="0"/>
    </linearGradient>
  </defs>
  <!-- background gradient strip -->
  <rect width="{width}" height="{height}" fill="url(#{grad_id})"/>
  <!-- label text -->
  <text
    x="{text_x}"
    y="{text_y}"
    font-family="MyriadPro, 'Myriad Pro', Arial, sans-serif"
    font-weight="900"
    font-size="{font_size}"
    fill="{WHITE}"
    dominant-baseline="middle"
    text-anchor="start"
    letter-spacing="0">{text}</text>
</svg>"""


def generate_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0

    # Section headers — 320×36px, font 18px, per-section color
    for stem, text, color in HEADERS:
        svg = make_svg(
            text=text,
            width=320, height=36,
            font_size=18,
            text_x=10,
            text_y=18.0,   # vertical center of 36px
            bg_color=color,
        )
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    # Field labels — 320×22px, font 13px, pale blue background
    for stem, text in LABELS:
        svg = make_svg(
            text=text,
            width=320, height=22,
            font_size=13,
            text_x=8,
            text_y=11.0,   # vertical center of 22px
            bg_color=PALE_BLUE,
        )
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    # Divider lines — 320×4px, solid color, no text
    for stem, color in DIVIDERS:
        svg = make_divider_svg(color=color)
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    # Action buttons — 150×36px, white bg, red border + text
    for stem, text in BUTTONS:
        svg = make_button_svg(text=text)
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    print(f"\nDone — {count} SVG files written to: {OUT_DIR}")


if __name__ == "__main__":
    generate_all()
