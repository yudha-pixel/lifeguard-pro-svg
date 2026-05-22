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

# â”€â”€ Paths â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
SCRIPT_DIR = pathlib.Path(__file__).parent
FONT_PATH  = SCRIPT_DIR / "fonts" / "MYRIADPRO-BOLD.OTF"
OUT_DIR    = SCRIPT_DIR / "svg"

# â”€â”€ Font embed â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
with open(FONT_PATH, "rb") as f:
    FONT_B64 = base64.b64encode(f.read()).decode("utf-8")

FONT_FACE = f"""@font-face {{
  font-family: 'MyriadPro';
  src: url('data:font/opentype;base64,{FONT_B64}') format('opentype');
  font-weight: 700;
  font-style: normal;
}}"""

# â”€â”€ Color / gradient constants â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
NAVY      = "#1a2744"
RED       = "#B91C1C"
WHITE     = "#FFFFFF"
PALE_BLUE = "#93C5FD"

# â”€â”€ Asset definitions â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#  (filename_stem, display_text, width, height, font_size, text_x, text_y)
#  Headers: 320Ã—32, prefix â–¸ already in text, font 13px, left-padded 10px
#  Labels:  320Ã—20, no prefix, font 10px, left-padded 8px

HEADERS = [
    ("header_contact",              "&#9658; CONTACT",              RED),
    ("header_contact_info",         "&#9658; CONTACT INFO",         RED),
    ("header_contact_quick_access", "&#9658; CONTACT QUICK-ACCESS", NAVY),
    ("header_contact_details",      "&#9658; CONTACT DETAILS",      RED),
    ("header_create_contact",       "&#9658; CREATE CONTACT",       NAVY),
    ("header_person",               "&#9658; PERSON",               RED),
    ("header_opportunities",        "&#9658; OPPORTUNITIES",        NAVY),
    ("header_deal",                 "&#9658; DEAL",                 RED),
    ("header_deal_quick_info",      "&#9658; DEAL QUICK INFO",      RED),
    ("header_deal_details",         "&#9658; DEAL DETAILS",         RED),
    ("header_lead_details",         "&#9658; LEAD DETAILS",         NAVY),
    ("header_create_opportunity",   "&#9658; CREATE OPPORTUNITY",   RED),
    ("header_activities",           "&#9658; ACTIVITIES",           RED),
    ("header_quick_add_activity",   "&#9658; QUICK ADD ACTIVITY",   NAVY),
    ("header_notes",                "&#9658; NOTES",                NAVY),
    ("header_add_log_note",         "&#9658; ADD LOG NOTE",         RED),
    ("header_quick_chatter",        "&#9658; QUICK CHATTER",        RED),
    ("header_conversation_timeline","&#9658; CONVERSATION TIMELINE",NAVY),
    ("header_organization",         "&#9658; ORGANIZATION",         NAVY),
    ("header_organization_details", "&#9658; ORGANIZATION DETAILS", RED),
    ("header_dates_deadlines",      "&#9658; DATES &amp; DEADLINES",NAVY),
    ("header_initial_contact",      "&#9658; INITIAL CONTACT",      NAVY),
    ("header_form_submission",      "&#9658; FORM SUBMISSION",      RED),
    ("header_odoo_crm",             "&#9658; ODOO CRM",             NAVY),
    ("header_team",                 "&#9658; TEAM",                 NAVY),
    ("header_legacy_fields",        "&#9658; LEGACY FIELDS",        RED),
    ("header_header",               "&#9658; HEADER",               RED),
    ("header_address",              "&#9658; ADDRESS",              NAVY),
    ("header_left_column",          "&#9658; LEFT COLUMN",          RED),
    ("header_left_column_legacy",   "&#9658; LEFT COLUMN - LEGACY", NAVY),
    ("header_right_column",         "&#9658; RIGHT COLUMN",         RED),
    ("header_related_contacts",         "&#9658; RELATED CONTACTS",         RED),
    ("header_create_related_contacts",  "&#9658; CREATE RELATED CONTACTS",  RED),
    ("header_company_contacts",         "&#9658; COMPANY CONTACTS",         NAVY),
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
    ("divider_red",      RED),
    ("divider_navy",     NAVY),
    ("divider_gold",     RED),
    ("divider_teal",     NAVY),
    ("divider_pink",     RED),
    ("divider_gray",     NAVY),
    ("divider_purple",   RED),
    ("divider_amber",    RED),
    ("divider_blue",     NAVY),
    ("divider_indigo",   RED),
    ("divider_orange",   NAVY),
    ("divider_green",    RED),
    ("divider_cyan",     NAVY),
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


def to_camel(stem: str) -> str:
    """Convert snake_case stem to camelCase filename (e.g. header_related_contacts â†’ headerRelatedContacts)."""
    parts = stem.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])


def generate_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0

    # Section headers â€” 320Ã—36px, font 18px, per-section color
    for stem, text, color in HEADERS:
        svg = make_svg(
            text=text,
            width=320, height=36,
            font_size=18,
            text_x=10,
            text_y=18.0,   # vertical center of 36px
            bg_color=color,
        )
        out = OUT_DIR / f"{to_camel(stem)}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  OK  {out.name}")
        count += 1

        for tone_name, tone_color in (("Red", RED), ("Blue", NAVY)):
            tone_svg = make_svg(
                text=text,
                width=320, height=36,
                font_size=18,
                text_x=10,
                text_y=18.0,
                bg_color=tone_color,
            )
            tone_out = OUT_DIR / f"{to_camel(stem)}{tone_name}.svg"
            tone_out.write_text(tone_svg, encoding="utf-8")
            print(f"  OK  {tone_out.name}")
            count += 1

    # Field labels â€” 320Ã—22px, font 13px, pale blue background
    for stem, text in LABELS:
        svg = make_svg(
            text=text,
            width=320, height=22,
            font_size=13,
            text_x=8,
            text_y=11.0,   # vertical center of 22px
            bg_color=PALE_BLUE,
        )
        out = OUT_DIR / f"{to_camel(stem)}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  OK  {out.name}")
        count += 1

        for tone_name, tone_color in (("Red", RED), ("Blue", NAVY)):
            tone_svg = make_svg(
                text=text,
                width=320, height=36,
                font_size=18,
                text_x=10,
                text_y=18.0,
                bg_color=tone_color,
            )
            tone_out = OUT_DIR / f"{to_camel(stem)}{tone_name}.svg"
            tone_out.write_text(tone_svg, encoding="utf-8")
            print(f"  OK  {tone_out.name}")
            count += 1

    # Divider lines â€” 320Ã—4px, solid color, no text
    for stem, color in DIVIDERS:
        svg = make_divider_svg(color=color)
        out = OUT_DIR / f"{to_camel(stem)}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  OK  {out.name}")
        count += 1

        for tone_name, tone_color in (("Red", RED), ("Blue", NAVY)):
            tone_svg = make_svg(
                text=text,
                width=320, height=36,
                font_size=18,
                text_x=10,
                text_y=18.0,
                bg_color=tone_color,
            )
            tone_out = OUT_DIR / f"{to_camel(stem)}{tone_name}.svg"
            tone_out.write_text(tone_svg, encoding="utf-8")
            print(f"  OK  {tone_out.name}")
            count += 1

    # Action buttons â€” 150Ã—36px, white bg, red border + text
    for stem, text in BUTTONS:
        svg = make_button_svg(text=text)
        out = OUT_DIR / f"{to_camel(stem)}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"  OK  {out.name}")
        count += 1

        for tone_name, tone_color in (("Red", RED), ("Blue", NAVY)):
            tone_svg = make_svg(
                text=text,
                width=320, height=36,
                font_size=18,
                text_x=10,
                text_y=18.0,
                bg_color=tone_color,
            )
            tone_out = OUT_DIR / f"{to_camel(stem)}{tone_name}.svg"
            tone_out.write_text(tone_svg, encoding="utf-8")
            print(f"  OK  {tone_out.name}")
            count += 1

    print(f"\nDone â€” {count} SVG files written to: {OUT_DIR}")


if __name__ == "__main__":
    generate_all()

