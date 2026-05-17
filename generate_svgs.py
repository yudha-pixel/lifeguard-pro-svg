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
WHITE     = "#FFFFFF"

# ── Asset definitions ─────────────────────────────────────────────────────────
#  (filename_stem, display_text, width, height, font_size, text_x, text_y)
#  Headers: 320×32, prefix ▸ already in text, font 13px, left-padded 10px
#  Labels:  320×20, no prefix, font 10px, left-padded 8px

HEADERS = [
    ("header_contact",              "&#9658; CONTACT"),
    ("header_opportunities",        "&#9658; OPPORTUNITIES"),
    ("header_odoo_crm",             "&#9658; ODOO CRM"),
    ("header_form_submission",      "&#9658; FORM SUBMISSION"),
    ("header_deal_quick_info",      "&#9658; DEAL QUICK INFO"),
    ("header_team",                 "&#9658; TEAM"),
    ("header_contact_quick_access", "&#9658; CONTACT QUICK-ACCESS"),
    ("header_activities",           "&#9658; ACTIVITIES"),
    ("header_notes",                "&#9658; NOTES"),
    ("header_quick_add_activity",   "&#9658; QUICK ADD ACTIVITY"),
    ("header_deal",                 "&#9658; DEAL"),
    ("header_contact_info",         "&#9658; CONTACT INFO"),
    ("header_dates_deadlines",      "&#9658; DATES &amp; DEADLINES"),
    ("header_deal_details",         "&#9658; DEAL DETAILS"),
    ("header_initial_contact",      "&#9658; INITIAL CONTACT"),
    ("header_legacy_fields",        "&#9658; LEGACY FIELDS"),
    ("header_add_log_note",         "&#9658; ADD LOG NOTE"),
    ("header_conversation_timeline","&#9658; CONVERSATION TIMELINE"),
    ("header_person",               "&#9658; PERSON"),
    ("header_organization",         "&#9658; ORGANIZATION"),
    ("header_create_opportunity",   "&#9658; CREATE OPPORTUNITY"),
    ("header_create_contact",       "&#9658; CREATE CONTACT"),
    ("header_lead_details",         "&#9658; LEAD DETAILS"),
    ("header_contact_details",      "&#9658; CONTACT DETAILS"),
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
    ("label_google_sheet", "GOOGLE SHEET"),
]


def make_svg(text: str, width: int, height: int, font_size: int,
             text_x: int, text_y: float) -> str:
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
      <stop offset="0%"   stop-color="{NAVY}"  stop-opacity="1"/>
      <stop offset="70%"  stop-color="{NAVY}"  stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{NAVY}"  stop-opacity="0"/>
    </linearGradient>
  </defs>
  <!-- background gradient strip -->
  <rect width="{width}" height="{height}" fill="url(#{grad_id})"/>
  <!-- label text -->
  <text
    x="{text_x}"
    y="{text_y}"
    font-family="MyriadPro, 'Myriad Pro', Arial, sans-serif"
    font-weight="700"
    font-size="{font_size}"
    fill="{WHITE}"
    dominant-baseline="middle"
    text-anchor="start"
    letter-spacing="0.5">{text}</text>
</svg>"""


def generate_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0

    # Section headers — 320×40px, font 18px
    for stem, text in HEADERS:
        svg = make_svg(
            text=text,
            width=320, height=40,
            font_size=18,
            text_x=10,
            text_y=20.0,   # vertical center of 40px
        )
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    # Field labels — 320×24px, font 13px
    for stem, text in LABELS:
        svg = make_svg(
            text=text,
            width=320, height=24,
            font_size=13,
            text_x=8,
            text_y=12.0,   # vertical center of 24px
        )
        out = OUT_DIR / f"{stem}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  ✓  {out.name}")
        count += 1

    print(f"\nDone — {count} SVG files written to: {OUT_DIR}")


if __name__ == "__main__":
    generate_all()
