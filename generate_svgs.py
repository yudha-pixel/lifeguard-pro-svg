"""
generate_svgs.py
Generates Gmail sidebar SVG assets for section headers, subtitles, labels,
dividers, and buttons.

Output folder: svg/
Font: fonts/MYRIADPRO-BOLD.OTF
"""

import base64
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).parent
FONT_PATH = SCRIPT_DIR / "fonts" / "MYRIADPRO-BOLD.OTF"
OUT_DIR = SCRIPT_DIR / "svg"

with open(FONT_PATH, "rb") as f:
    FONT_B64 = base64.b64encode(f.read()).decode("utf-8")

FONT_FACE = f"""@font-face {{
  font-family: 'MyriadPro';
  src: url('data:font/opentype;base64,{FONT_B64}') format('opentype');
  font-weight: 700;
  font-style: normal;
}}"""

NAVY = "#1a2744"
RED = "#B91C1C"
WHITE = "#FFFFFF"
PALE_BLUE = "#93C5FD"

HEADERS = [
    ("header_contact", "&#9658; CONTACT", RED),
    ("header_contact_info", "&#9658; CONTACT INFO", RED),
    ("header_contact_quick_access", "&#9658; CONTACT QUICK-ACCESS", NAVY),
    ("header_contact_details", "&#9658; CONTACT DETAILS", RED),
    ("header_create_contact", "&#9658; CREATE CONTACT", NAVY),
    ("header_person", "&#9658; PERSON", RED),
    ("header_opportunities", "&#9658; OPPORTUNITIES", NAVY),
    ("header_deal", "&#9658; DEAL", RED),
    ("header_deal_quick_info", "&#9658; DEAL QUICK INFO", RED),
    ("header_deal_details", "&#9658; DEAL DETAILS", RED),
    ("header_lead_details", "&#9658; LEAD DETAILS", NAVY),
    ("header_create_opportunity", "&#9658; CREATE OPPORTUNITY", RED),
    ("header_activities", "&#9658; ACTIVITIES", RED),
    ("header_quick_add_activity", "&#9658; QUICK ADD ACTIVITY", NAVY),
    ("header_notes", "&#9658; NOTES", NAVY),
    ("header_add_log_note", "&#9658; ADD LOG NOTE", RED),
    ("header_quick_chatter", "&#9658; QUICK CHATTER", RED),
    ("header_conversation_timeline", "&#9658; CONVERSATION TIMELINE", NAVY),
    ("header_organization", "&#9658; ORGANIZATION", NAVY),
    ("header_organization_details", "&#9658; ORGANIZATION DETAILS", RED),
    ("header_dates_deadlines", "&#9658; DATES &amp; DEADLINES", NAVY),
    ("header_initial_contact", "&#9658; INITIAL CONTACT", NAVY),
    ("header_form_submission", "&#9658; FORM SUBMISSION", RED),
    ("header_odoo_crm", "&#9658; ODOO CRM", NAVY),
    ("header_team", "&#9658; TEAM", NAVY),
    ("header_legacy_fields", "&#9658; LEGACY FIELDS", RED),
    ("header_header", "&#9658; HEADER", RED),
    ("header_address", "&#9658; ADDRESS", NAVY),
    ("header_left_column", "&#9658; LEFT COLUMN", RED),
    ("header_left_column_legacy", "&#9658; LEFT COLUMN - LEGACY", NAVY),
    ("header_right_column", "&#9658; RIGHT COLUMN", RED),
    ("header_related_contacts", "&#9658; RELATED CONTACTS", RED),
    ("header_create_related_contacts", "&#9658; CREATE RELATED CONTACTS", RED),
    ("header_company_contacts", "&#9658; COMPANY CONTACTS", NAVY),
    ("header_company", "&#9658; COMPANY", NAVY),
    ("header_context", "&#9658; CONTEXT", RED),
    ("header_confirm", "&#9658; CONFIRM", RED),
    ("header_message", "&#9658; MESSAGE", RED),
    ("header_people", "&#9658; PEOPLE", RED),
    ("header_quick_fix", "&#9658; QUICK FIX", NAVY),
    ("header_select_existing_company", "&#9658; SELECT EXISTING COMPANY", RED),
    ("header_add_new_contact_to_company", "&#9658; + ADD NEW CONTACT TO COMPANY", RED),
    ("header_contacts", "&#9658; CONTACTS", NAVY),
    ("header_create_link_company", "&#9658; + CREATE &amp; LINK COMPANY", NAVY),
    ("header_re_create_link_company", "&#9658; + RE-CREATE &amp; LINK COMPANY", NAVY),
]

LABELS = [
    ("label_from", "FROM"),
    ("label_email", "EMAIL"),
    ("label_subject", "SUBJECT"),
    ("label_name", "NAME"),
    ("label_phone", "PHONE"),
    ("label_company", "COMPANY"),
    ("label_location", "LOCATION"),
    ("label_course", "COURSE"),
    ("label_date", "DATE"),
    ("label_interested", "INTERESTED IN"),
    ("label_message", "MESSAGE"),
    ("label_url", "URL"),
    ("label_user", "USER"),
    ("label_google_sheet", "GOOGLE SHEET"),
    ("label_sender_email", "SENDER EMAIL"),
    ("label_sender_name", "SENDER NAME"),
    ("label_opportunity_name", "OPPORTUNITY NAME"),
    ("label_confirmation", "CONFIRMATION"),
]

SUBTITLES = [
    ("subtitle_edit_company_details_name_address_phone", "Edit company details - name, address, phone"),
    ("subtitle_people_who_work_at_this_company", "People who work at this company"),
    ("subtitle_or_select_an_existing_company", "Or select an existing company"),
    ("subtitle_matched_via_email_1", "Matched via Email 1"),
    ("subtitle_matched_via_email_2", "Matched via Email 2"),
    ("subtitle_matched_via_email_3", "Matched via Email 3"),
    ("subtitle_matched_via_email_4", "Matched via Email 4"),
    ("subtitle_matched_via_alternate_email", "Matched via alternate email"),
    ("subtitle_no_company_is_linked_to_this_deal_create_one_and_it_will_be_automatically_linked", "No company is linked to this deal. Create one and it will be automatically linked."),
    ("subtitle_create_the_company_record_and_it_will_be_automatically_linked_to_this_deal", "Create the company record and it will be automatically linked to this deal."),
    ("subtitle_the_previous_company_was_deleted_create_a_new_one_to_restore_the_link", "The previous company was deleted. Create a new one to restore the link."),
]

DIVIDERS = [
    ("divider_red", RED),
    ("divider_navy", NAVY),
    ("divider_gold", RED),
    ("divider_teal", NAVY),
    ("divider_pink", RED),
    ("divider_gray", NAVY),
    ("divider_purple", RED),
    ("divider_amber", RED),
    ("divider_blue", NAVY),
    ("divider_indigo", RED),
    ("divider_orange", NAVY),
    ("divider_green", RED),
    ("divider_cyan", NAVY),
]

BUTTONS = [
    ("btn_save", "SAVE"),
    ("btn_cancel", "CANCEL"),
    ("btn_submit", "SUBMIT"),
    ("btn_create", "CREATE"),
    ("btn_update", "UPDATE"),
]


def make_divider_svg(color: str, width: int = 320, height: int = 4) -> str:
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
  <rect width=\"{width}\" height=\"{height}\" fill=\"{color}\" rx=\"1\" ry=\"1\"/>
</svg>"""


def make_button_svg(text: str, width: int = 150, height: int = 36) -> str:
    radius = 4
    border = 2
    font_size = 14
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
  <defs><style>{FONT_FACE}</style></defs>
  <rect x=\"{border/2}\" y=\"{border/2}\" width=\"{width - border}\" height=\"{height - border}\" rx=\"{radius}\" ry=\"{radius}\" fill=\"{WHITE}\" stroke=\"{RED}\" stroke-width=\"{border}\"/>
  <text x=\"{width // 2}\" y=\"{height // 2}\" font-family=\"MyriadPro, 'Myriad Pro', Arial, sans-serif\" font-weight=\"700\" font-size=\"{font_size}\" fill=\"{RED}\" dominant-baseline=\"middle\" text-anchor=\"middle\" letter-spacing=\"1\">{text}</text>
</svg>"""


def make_svg(text: str, width: int, height: int, font_size: int, text_x: int, text_y: float, bg_color: str = NAVY) -> str:
    grad_id = "bg"
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
  <defs>
    <style>{FONT_FACE}</style>
    <linearGradient id=\"{grad_id}\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\">
      <stop offset=\"0%\" stop-color=\"{bg_color}\" stop-opacity=\"1\"/>
      <stop offset=\"50%\" stop-color=\"{bg_color}\" stop-opacity=\"1\"/>
      <stop offset=\"100%\" stop-color=\"{bg_color}\" stop-opacity=\"0\"/>
    </linearGradient>
  </defs>
  <rect width=\"{width}\" height=\"{height}\" fill=\"url(#{grad_id})\"/>
  <text x=\"{text_x}\" y=\"{text_y}\" font-family=\"MyriadPro, 'Myriad Pro', Arial, sans-serif\" font-weight=\"900\" font-size=\"{font_size}\" fill=\"{WHITE}\" dominant-baseline=\"middle\" text-anchor=\"start\" letter-spacing=\"0\">{text}</text>
</svg>"""


def make_subtitle_svg(text: str, color: str, width: int = 320, height: int = 18) -> str:
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"{width}\" height=\"{height}\" viewBox=\"0 0 {width} {height}\">
  <defs><style>{FONT_FACE}</style></defs>
  <text x=\"0\" y=\"{height / 2}\" font-family=\"MyriadPro, 'Myriad Pro', Arial, sans-serif\" font-weight=\"700\" font-size=\"11\" font-style=\"italic\" fill=\"{color}\" dominant-baseline=\"middle\" text-anchor=\"start\">{text}</text>
</svg>"""


def to_camel(stem: str) -> str:
    parts = stem.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])


def write_svg(name: str, svg: str) -> int:
    out = OUT_DIR / name
    out.write_text(svg, encoding="utf-8")
    print(f"  OK  {out.name}")
    return 1


def write_tone_variants(stem: str, text: str, factory) -> int:
    count = 0
    for tone_name, tone_color in (("Red", RED), ("Blue", NAVY)):
        count += write_svg(f"{to_camel(stem)}{tone_name}.svg", factory(text, tone_color))
    return count


def generate_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for stem, text, color in HEADERS:
        count += write_svg(
            f"{to_camel(stem)}.svg",
            make_svg(text=text, width=320, height=36, font_size=18, text_x=10, text_y=18.0, bg_color=color),
        )
        count += write_tone_variants(
            stem,
            text,
            lambda value, tone_color: make_svg(value, 320, 36, 18, 10, 18.0, tone_color),
        )

    for stem, text in LABELS:
        count += write_svg(
            f"{to_camel(stem)}.svg",
            make_svg(text=text, width=320, height=22, font_size=13, text_x=8, text_y=11.0, bg_color=NAVY),
        )
        count += write_tone_variants(
            stem,
            text,
            lambda value, tone_color: make_svg(value, 320, 22, 13, 8, 11.0, tone_color),
        )

    for stem, text in SUBTITLES:
        count += write_svg(f"{to_camel(stem)}.svg", make_subtitle_svg(text, NAVY))
        count += write_tone_variants(stem, text, lambda value, tone_color: make_subtitle_svg(value, tone_color))

    for stem, color in DIVIDERS:
        count += write_svg(f"{to_camel(stem)}.svg", make_divider_svg(color=color))

    for stem, text in BUTTONS:
        count += write_svg(f"{to_camel(stem)}.svg", make_button_svg(text=text))

    print(f"\nDone - {count} SVG files written to: {OUT_DIR}")


if __name__ == "__main__":
    generate_all()
