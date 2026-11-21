"""Página web de SAVA Software (Streamlit).

Ejecutar en local:  streamlit run app.py
Los textos están en content.py y el diseño en assets/style.css.
"""
import base64
import re
from pathlib import Path
from urllib.parse import quote

import requests
import streamlit as st
from PIL import Image

from content import EMAIL, LINKEDIN_CEO, LINKEDIN_COMPANY, TEXT, WHATSAPP_NUMBER

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

# ---------------------------------------------------------------- idioma
lang = st.query_params.get("lang", "es")
if lang not in TEXT:
    lang = "es"
T = TEXT[lang]

st.set_page_config(
    page_title=T["page_title"],
    page_icon=Image.open(ASSETS / "icono.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data
def b64(name: str) -> str:
    data = (ASSETS / name).read_bytes()
    mime = "image/jpeg" if name.endswith(".jpg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def html(block: str) -> None:
    st.markdown(block, unsafe_allow_html=True)


def wa_link(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"


ICONS = {
    "stock": '<svg viewBox="0 0 24 24"><path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/></svg>',
    "flow": '<svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h7a3 3 0 0 1 0 6h-4a3 3 0 0 0 0 6h7"/></svg>',
    "setup": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M8.5 10l2.5 2.5L15.5 8"/></svg>',
    "care": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L15.5 10"/></svg>',
}

html(f"<style>{(ASSETS / 'style.css').read_text(encoding='utf-8')}</style>")

# ---------------------------------------------------------------- barra superior
links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav"])
lang_switch = (
    f'<a class="{"on" if lang == "es" else ""}" href="?lang=es" target="_self">ES</a>'
    f'<a class="{"on" if lang == "en" else ""}" href="?lang=en" target="_self">EN</a>'
)
html(f"""
<div class="nav"><div class="wrap">
  <a href="#inicio" target="_self"><img src="{b64('logo_blanco.png')}" alt="SAVA Software"></a>
  <div class="links">{links}</div>
  <div class="right"><span class="lang">{lang_switch}</span>
    <a class="btn btn-blue btn-sm" href="{wa_link(T['wa_default'])}" target="_blank">{T['nav_cta']}</a></div>
</div></div>
""")

# ---------------------------------------------------------------- portada
stats = "".join(f"<div><b>{n}</b><span>{t}</span></div>" for n, t in T["stats"])
html(f"""
<section class="hero" id="inicio"><div class="wrap">
  <div class="grid">
    <div>
      <div class="eyebrow">{T['hero_eyebrow']}</div>
      <div class="h1">{T['hero_title']}</div>
      <p class="sub">{T['hero_sub']}</p>
      <div class="ctas">
        <a class="btn btn-blue" href="{wa_link(T['wa_default'])}" target="_blank">{T['hero_cta1']}</a>
        <a class="btn btn-ghost" href="#productos" target="_self">{T['hero_cta2']}</a>
      </div>
    </div>
    <div class="bird"><img src="{b64('colibri_blanco.png')}" alt="SAVA"></div>
  </div>
  <div class="stats">{stats}</div>
</div></section>
""")

# ---------------------------------------------------------------- problema
problems = "".join(
    f'<div class="card"><div class="num">{i}</div><div class="h3">{t}</div><p>{d}</p></div>'
    for i, (t, d) in enumerate(T["problems"], start=1)
)
html(f"""
<section class="sec"><div class="wrap">
  <div class="kicker">{T['problem_kicker']}</div>
  <div class="h2">{T['problem_title']}</div>
  <div class="cards c3">{problems}</div>
  <div class="note">{T['problem_note']}</div>
</div></section>
""")

# ---------------------------------------------------------------- productos
cards = ""
for p in T["products"]:
    items = "".join(f"<li>{x}</li>" for x in p["items"])
    cards += f"""
    <div class="card prod">
      <div class="top"><div class="ico">{ICONS[p['icon']]}</div><span class="tag">{p['tag']}</span></div>
      <div class="h3">{p['name']}</div><p>{p['desc']}</p>
      <ul>{items}</ul>
      <div class="price">{p['price']}</div>
    </div>"""
html(f"""
<section class="sec bg2" id="productos"><div class="wrap">
  <div class="kicker">{T['products_kicker']}</div>
  <div class="h2">{T['products_title']}</div>
  <div class="cards c4">{cards}</div>
</div></section>
""")

# ---------------------------------------------------------------- planes
plans = ""
for p in T["plans"]:
    items = "".join(f"<li>{x}</li>" for x in p["items"])
    badge = f'<span class="badge">{p["badge"]}</span>' if p["badge"] else ""
    plans += f"""
    <div class="card plan {'featured' if p['featured'] else ''}">{badge}
      <div class="h3">{p['name']}</div>
      <div class="amount">{p['price']}</div><div class="unit">{p['unit']}</div>
      <ul>{items}</ul>
    </div>"""
html(f"""
<section class="sec" id="planes"><div class="wrap">
  <div class="kicker">{T['plans_kicker']}</div>
  <div class="h2">{T['plans_title']}</div>
  <div class="cards c2">{plans}</div>
  <div class="addon">{T['plans_addon']}</div>
  <div class="note">{T['plans_note']}</div>
</div></section>
""")

# ---------------------------------------------------------------- proceso
steps = "".join(
    f'<div class="step"><b>{i:02d}</b><div class="h4">{t}</div><p>{d}</p></div>'
    for i, (t, d) in enumerate(T["steps"], start=1)
)
html(f"""
<section class="sec bg2" id="proceso"><div class="wrap">
  <div class="kicker">{T['process_kicker']}</div>
  <div class="h2">{T['process_title']}</div>
  <div class="steps">{steps}</div>
</div></section>
""")

# ---------------------------------------------------------------- por qué SAVA
why = "".join(
    f'<div class="card"><div class="num">{i}</div><div class="h3">{t}</div><p>{d}</p></div>'
    for i, (t, d) in enumerate(T["why"], start=1)
)
html(f"""
<section class="sec"><div class="wrap">
  <div class="kicker">{T['why_kicker']}</div>
  <div class="h2">{T['why_title']}</div>
  <div class="cards c3">{why}</div>
</div></section>
""")

# ---------------------------------------------------------------- nosotros
chips = "".join(f'<span class="chip">{a}</span>' for a in T["about_areas"])
html(f"""
<section class="sec bg2" id="nosotros"><div class="wrap">
  <div class="kicker">{T['about_kicker']}</div>
  <div class="h2">{T['about_title']}</div>
  <div class="about">
    <img src="{b64('joseph.jpg')}" alt="{T['about_name']}">
    <div>
      <div class="h3">{T['about_name']}</div>
      <div class="role">{T['about_role']}</div>
      <p>{T['about_bio']}</p>
      <p>{T['about_team']}</p>
      <div class="chips">{chips}</div>
      <p class="social" style="margin-top:18px">
        <a href="{LINKEDIN_CEO}" target="_blank">LinkedIn</a>
        <a href="{LINKEDIN_COMPANY}" target="_blank">SAVA Software</a>
      </p>
    </div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- contacto
html(f"""
<div class="contact-head" id="contacto"><div class="wrap">
  <div class="kicker">{T['contact_kicker']}</div>
  <div class="h2">{T['contact_title']}</div>
  <p class="lead">{T['contact_sub']}</p>
</div></div>
""")


def save_lead(data: dict) -> bool:
    """Guarda la solicitud en Supabase si hay credenciales en los secrets de Streamlit."""
    try:
        url = st.secrets["SUPABASE_URL"].rstrip("/")
        key = st.secrets["SUPABASE_ANON_KEY"]
    except Exception:
        return False
    try:
        r = requests.post(
            f"{url}/rest/v1/leads",
            headers={"apikey": key, "Authorization": f"Bearer {key}",
                     "Content-Type": "application/json", "Prefer": "return=minimal"},
            json=data, timeout=8,
        )
        return r.status_code in (200, 201, 204)
    except requests.RequestException:
        return False


L = T["contact_labels"]
with st.container(key="contact_box"):
    left, right = st.columns([1, 1.4], gap="large")
    with left:
        info = "".join(f"<div><small>{k}</small><span>{v}</span></div>" for k, v in T["contact_info"])
        html(f"""<div class="info">{info}
          <a class="btn btn-blue" href="{wa_link(T['wa_default'])}" target="_blank">WhatsApp</a></div>""")
    with right:
        with st.form("lead_form", clear_on_submit=False):
            c1, c2 = st.columns(2)
            name = c1.text_input(L["name"], max_chars=100)
            email = c2.text_input(L["email"], max_chars=255)
            company = c1.text_input(L["company"], max_chars=100)
            product = c2.selectbox(L["product"], [p["name"] for p in T["products"]] + [L["not_sure"]])
            message = st.text_area(L["message"], max_chars=1000, height=110)
            consent = st.checkbox(L["consent"])
            sent = st.form_submit_button(L["submit"])
        if sent:
            if not name.strip() or not message.strip() or not consent:
                st.warning(L["required"])
            elif email and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email.strip()):
                st.warning(L["required"])
            else:
                full = f"{message.strip()}\n\n[{L['product']}: {product}]"
                saved = save_lead({"name": name.strip(), "email": email.strip() or None,
                                   "company": company.strip() or None, "message": full})
                wa_text = f"{T['wa_default']}\n\n{L['name']}: {name.strip()}\n{L['company']}: {company.strip()}\n{L['product']}: {product}\n{message.strip()}"
                st.success(L["ok"] + (" " + L["saved"] if saved else ""))
                st.link_button(L["open_wa"], wa_link(wa_text))

# ---------------------------------------------------------------- pie de página
foot_links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav"][1:])
html(f"""
<div class="foot"><div class="wrap">
  <div class="row">
    <div><img src="{b64('logo_blanco.png')}" alt="SAVA Software"><p>{T['footer_tag']}</p></div>
    <div>{foot_links}</div>
    <div><a href="{LINKEDIN_COMPANY}" target="_blank">LinkedIn</a><a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{wa_link(T['wa_default'])}" target="_blank">WhatsApp</a></div>
  </div>
  <details><summary>{T['privacy_title']}</summary><p style="max-width:900px;margin-top:10px">{T['privacy']}</p></details>
  <div class="copy">{T['footer_rights']}</div>
</div></div>
""")
