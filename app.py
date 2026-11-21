"""Página web de SAVA Software (Streamlit).

Ejecutar en local:  streamlit run app.py
Los textos están en content.py y el diseño en assets/style.css.
"""
import base64
import re
import smtplib
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote

import requests
import streamlit as st
from PIL import Image

import importlib

import content

importlib.reload(content)  # Streamlit Cloud: siempre usa la última versión de content.py
from content import (EMAIL, INSTAGRAM, LINKEDIN_CEO, LINKEDIN_COMPANY, PHONE_DISPLAY, TEXT, TIKTOK,  # noqa: E402
                     WHATSAPP_NUMBER, YOUTUBE)

BASE = Path(__file__).parent

# Base de datos (Supabase). La clave "publishable" es pública por diseño: la tabla solo permite
# insertar solicitudes con autorización de datos; nadie puede leerlas sin entrar a Supabase.
SUPABASE_URL = "https://refhtyobgnyonhexszhz.supabase.co"
SUPABASE_KEY = "sb_publishable_1e8SknhYLNPfu-0HEGkSJg_XAkCBNgL"
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


def full_width(fn, *args, **kwargs):
    """Botón a todo el ancho, compatible con versiones nuevas y antiguas de Streamlit."""
    try:
        return fn(*args, width="stretch", **kwargs)
    except TypeError:
        return fn(*args, use_container_width=True, **kwargs)


def html(block: str) -> None:
    st.markdown(block, unsafe_allow_html=True)


def wa_link(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"


SOCIAL_SVG = {
    "whatsapp": '<svg viewBox="0 0 24 24"><path d="M20.5 3.5A11 11 0 0 0 3.2 17.1L2 22l5-1.3A11 11 0 0 0 20.5 3.5zM12 20.1a9 9 0 0 1-4.6-1.3l-.3-.2-3 .8.8-2.9-.2-.3A9 9 0 1 1 12 20.1zm5-6.7c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1l-.9 1.1c-.2.2-.3.2-.6.1a7.4 7.4 0 0 1-3.7-3.2c-.3-.5.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-2c-.2-.5-.4-.5-.6-.5h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.6-.6 1.8-1.3.2-.6.2-1.2.2-1.3-.1-.1-.2-.2-.5-.3z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.7 4.8 6.1V21h-4v-5.4c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2-2.8V9.1a6.3 6.3 0 1 0 5.4 6.3V8.6a8 8 0 0 0 4.4 1.3V6.5a4.5 4.5 0 0 1-4.4-4.5z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2c-2.7 0-3 0-4.1.1C4.2 2.3 2.3 4.2 2.1 7.9 2 9 2 9.3 2 12s0 3 .1 4.1c.2 3.7 2.1 5.6 5.8 5.8 1.1.1 1.4.1 4.1.1s3 0 4.1-.1c3.7-.2 5.6-2.1 5.8-5.8.1-1.1.1-1.4.1-4.1s0-3-.1-4.1c-.2-3.7-2.1-5.6-5.8-5.8C15 2 14.7 2 12 2z"/></svg>',
}


def social_row(cls: str = "social-icons") -> str:
    items = [("whatsapp", wa_link(T["wa_default"]), "WhatsApp"), ("linkedin", LINKEDIN_COMPANY, "LinkedIn"),
             ("tiktok", TIKTOK, "TikTok"), ("youtube", YOUTUBE, "YouTube"), ("instagram", INSTAGRAM, "Instagram")]
    links = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}" title="{n}">{SOCIAL_SVG[k]}</a>'
                    for k, u, n in items if u)
    return f'<div class="{cls}">{links}</div>'


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
  <div class="right">{social_row("social-icons nav-social")}<span class="lang">{lang_switch}</span>
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
      <div class="keys hero-keys">{"".join(f"<span>{k}</span>" for k in T['hero_sub'])}</div>
      <div class="ctas">
        <a class="btn btn-blue" href="#contacto" target="_self">{T['hero_cta1']} →</a>
        <a class="btn btn-ghost" href="#productos" target="_self">{T['hero_cta2']}</a>
      </div>
    </div>
    <div class="bird"><img src="{b64('colibri_blanco.png')}" alt="SAVA"></div>
  </div>
  <div class="stats">{stats}</div>
</div></section>
""")

# ---------------------------------------------------------------- propuesta de valor
value = "".join(f'<div class="val"><div class="vt">{t}</div><div class="vk">{d}</div></div>' for t, d in T["value"])
html(f'<section class="valuebar"><div class="wrap vals">{value}</div></section>')

# ---------------------------------------------------------------- productos
cards = ""
for p in T["products"]:
    cards += f"""
    <div class="card prod">
      <div class="top"><div class="ico">{ICONS[p['icon']]}</div><span class="tag">{p['tag']}</span></div>
      <div class="pname"><small>SAVA</small>{p['name']}</div>
      <div class="keys">{"".join(f"<span>{k}</span>" for k in p['keys'])}</div>
      <div class="price">{p['price']}</div>
    </div>"""
def cap_words(texto: str) -> str:
    return " ".join(w[:1].upper() + w[1:] for w in texto.split())


steps = "".join(f'<span class="chip-step"><b>{i:02d}</b> {cap_words(s)}</span>' + ('<span class="arrow">→</span>' if i < len(T["steps"]) else "")
                for i, s in enumerate(T["steps"], start=1))
html(f"""
<section class="sec bg2" id="productos"><div class="wrap">
  <div class="kicker">{T['products_kicker']}</div>
  <div class="h2">{T['products_title']}</div>
  <div class="cards c4">{cards}</div>
  <div class="flow"><span class="flow-t">{T['steps_title']}</span>{steps}</div>
</div></section>
""")

# ---------------------------------------------------------------- planes
plans = ""
for p in T["plans"]:
    items = "".join(f"<li>{x}</li>" for x in p["items"])
    badge = f'<span class="badge">{p["badge"]}</span>' if p["badge"] else ""
    plans += f"""
    <div class="card plan {'featured' if p['featured'] else ''}">{badge}
      <div class="pl-name">{p['name']}</div>
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

# ---------------------------------------------------------------- nosotros
html(f"""
<section class="sec bg2 about-sec" id="nosotros"><div class="wrap">
  <div class="about">
    <img src="{b64('joseph.jpg')}" alt="{T['about_name']}">
    <div>
      <div class="kicker">{T['about_kicker']}</div>
      <div class="h3">{T['about_name']}</div>
      <div class="role">{T['about_role']}</div>
      <div class="keys">{"".join(f"<span>{k}</span>" for k in T['about_bio'])}</div>
      <div class="chips">{"".join(f'<span class="chip">{k}</span>' for k in T['about_team'])}</div>
      {social_row("social-icons light")}
    </div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- contacto
html(f"""
<div class="contact-head" id="contacto"><div class="wrap">
  <div class="kicker">{T['contact_kicker']}</div>
  <div class="h2">{T['contact_title']}</div>
  <div class="keys">{"".join(f"<span>{k}</span>" for k in T['contact_sub'])}</div>
</div></div>
""")


def secret(name: str, default: str = "") -> str:
    try:
        return str(st.secrets[name])
    except Exception:
        return default


def save_lead(data: dict) -> bool:
    """Guarda la solicitud en la tabla leads de Supabase."""
    url = secret("SUPABASE_URL", SUPABASE_URL).rstrip("/")
    key = secret("SUPABASE_KEY", SUPABASE_KEY)
    try:
        r = requests.post(f"{url}/rest/v1/leads",
                          headers={"apikey": key, "Authorization": f"Bearer {key}",
                                   "Content-Type": "application/json", "Prefer": "return=minimal"},
                          json=data, timeout=8)
        return r.status_code in (200, 201, 204)
    except requests.RequestException:
        return False


def notify_email(data: dict) -> bool:
    """Envía un aviso con cada solicitud nueva. NOTIFY_EMAIL acepta varios correos separados por coma."""
    user, password, to = secret("SMTP_USER"), secret("SMTP_PASSWORD"), secret("NOTIFY_EMAIL")
    if not (user and password and to):
        return False
    msg = EmailMessage()
    msg["Subject"] = f"Nueva solicitud SAVA: {data['name']} ({data.get('product') or 'sin producto'})"
    msg["From"] = f"SAVA Web <{user}>"
    recipients = [x.strip() for x in to.replace(";", ",").split(",") if x.strip()]
    msg["To"] = ", ".join(recipients)
    if data.get("email"):
        msg["Reply-To"] = data["email"]
    rows = [("Nombre", data["name"]), ("Correo", data.get("email")), ("Celular", data.get("phone")),
            ("Negocio", data.get("company")), ("Producto", data.get("product")),
            ("Quiere novedades", "Sí" if data.get("newsletter") else "No"), ("Idioma", data.get("lang")),
            ("Mensaje", data["message"])]
    msg.set_content("\n".join(f"{k}: {v or '-'}" for k, v in rows) + "\n\nEnviado desde savasoftware.streamlit.app")
    try:
        with smtplib.SMTP_SSL(secret("SMTP_HOST", "smtp.gmail.com"), int(secret("SMTP_PORT", "465")), timeout=10) as s:
            s.login(user, password)
            s.send_message(msg)
        return True
    except Exception:
        return False


L = T["contact_labels"]
with st.container(key="contact_box"):
    info = "".join(f"<span><small>{k}</small>{v}</span>" for k, v in T["contact_info"])
    html(f"""<div class="info-row">{info}</div>
      <div class="wa-row"><a class="btn btn-wa" href="{wa_link(T['wa_default'])}" target="_blank">{L['open_wa']}</a></div>""")
    with st.container():
        with st.form("lead_form", clear_on_submit=False, border=False):
            c1, c2 = st.columns(2)
            name = c1.text_input(L["name"], max_chars=100)
            phone = c2.text_input(L["phone"], max_chars=30)
            email = c1.text_input(L["email"], max_chars=255)
            company = c2.text_input(L["company"], max_chars=100)
            product = st.selectbox(L["product"], ["SAVA " + p["name"].title() for p in T["products"]] + [L["not_sure"]])
            message = st.text_area(L["message"], max_chars=1000, height=90)
            consent = st.checkbox(L["consent"])
            newsletter = st.checkbox(L["newsletter"])
            sent = full_width(st.form_submit_button, L["submit"])
        if sent:
            errors = []
            if not name.strip():
                errors.append(L["err_name"])
            if not phone.strip() and not email.strip():
                errors.append(L["err_contact"])
            if email.strip() and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email.strip()):
                errors.append(L["err_email"])
            if not consent:
                errors.append(L["err_consent"])
            if errors:
                st.error("\n\n".join(errors))
            else:
                msg_txt = message.strip() or ("Solicitud de diagnóstico" if lang == "es" else "Assessment request")
                lead = {"name": name.strip(), "email": email.strip() or None, "phone": phone.strip() or None,
                        "company": company.strip() or None, "product": product, "message": msg_txt,
                        "lang": lang, "consent": True, "newsletter": bool(newsletter)}
                saved = save_lead(lead)
                notify_email(lead)
                wa_text = f"{T['wa_default']}\n\n{name.strip()} · {company.strip()} · {product}\n{message.strip()}"
                if saved:
                    st.success(L["ok"])
                else:
                    st.success(L["ok_nosave"])
                full_width(st.link_button, L["open_wa"], wa_link(wa_text))

# ---------------------------------------------------------------- pie de página
foot_links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav"][1:])
html(f"""
<div class="foot"><div class="wrap">
  <div class="row">
    <div><img src="{b64('logo_blanco.png')}" alt="SAVA Software"><p>{T['footer_tag']}</p></div>
    <div>{foot_links}</div>
    <div><b class="follow">{T['follow']}</b>{social_row()}
      <a href="mailto:{EMAIL}">{EMAIL}</a><a href="{wa_link(T['wa_default'])}" target="_blank">WhatsApp {PHONE_DISPLAY}</a></div>
  </div>
  <details><summary>{T['privacy_title']}</summary><p style="max-width:900px;margin-top:10px">{T['privacy']}</p></details>
  <div class="copy">{T['footer_rights']}</div>
</div></div>
""")

html(f'<a class="wa-float" href="{wa_link(T["wa_default"])}" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_SVG["whatsapp"]}</a>')
