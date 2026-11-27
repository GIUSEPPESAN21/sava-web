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
from content import (EMAIL, INSTAGRAM, LINKEDIN_CEO, LINKEDIN_COMPANY, PHONE_DISPLAY, PRICES, TEXT, TIKTOK,  # noqa: E402
                     WHATSAPP_NUMBER, YOUTUBE)
import json  # noqa: E402
import streamlit.components.v1 as components  # noqa: E402

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
    # Sin sangrías: Markdown trata como código las líneas con 4 espacios al inicio.
    st.markdown("\n".join(line.strip() for line in block.splitlines()), unsafe_allow_html=True)


def cop(n: int) -> str:
    """Pesos colombianos: $950.000 en español y $950,000 en inglés."""
    txt = f"{n:,}"
    return "$" + (txt.replace(",", ".") if lang == "es" else txt)


def money(n: int, size: str = "") -> str:
    return f'<span class="money {size}"><span class="cur">$</span>{cop(n)[1:]}<span class="code">COP</span></span>'


def wa_link(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"


SOCIAL_SVG = {
    "whatsapp": '<svg viewBox="0 0 24 24"><path d="M20.5 3.5A11 11 0 0 0 3.2 17.1L2 22l5-1.3A11 11 0 0 0 20.5 3.5zM12 20.1a9 9 0 0 1-4.6-1.3l-.3-.2-3 .8.8-2.9-.2-.3A9 9 0 1 1 12 20.1zm5-6.7c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1l-.9 1.1c-.2.2-.3.2-.6.1a7.4 7.4 0 0 1-3.7-3.2c-.3-.5.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-2c-.2-.5-.4-.5-.6-.5h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.6-.6 1.8-1.3.2-.6.2-1.2.2-1.3-.1-.1-.2-.2-.5-.3z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.7 4.8 6.1V21h-4v-5.4c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2-2.8V9.1a6.3 6.3 0 1 0 5.4 6.3V8.6a8 8 0 0 0 4.4 1.3V6.5a4.5 4.5 0 0 1-4.4-4.5z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2c-2.7 0-3 0-4.1.1C4.2 2.3 2.3 4.2 2.1 7.9 2 9 2 9.3 2 12s0 3 .1 4.1c.2 3.7 2.1 5.6 5.8 5.8 1.1.1 1.4.1 4.1.1s3 0 4.1-.1c3.7-.2 5.6-2.1 5.8-5.8.1-1.1.1-1.4.1-4.1s0-3-.1-4.1c-.2-3.7-2.1-5.6-5.8-5.8C15 2 14.7 2 12 2z"/></svg>',
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
care_m = cop(PRICES["care"])

# ---------------------------------------------------------------- barra superior
links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav2"])
lang_switch = (
    f'<a class="{"on" if lang == "es" else ""}" href="?lang=es" target="_self">ES</a>'
    f'<a class="{"on" if lang == "en" else ""}" href="?lang=en" target="_self">EN</a>'
)
html(f"""
<div class="nav" id="top"><div class="wrap">
<a class="brand" href="#inicio" target="_self"><img src="{b64('logo_blanco.png')}" alt="SAVA Software"></a>
<div class="links">{links}</div>
<div class="right">{social_row("social-icons nav-social")}<span class="lang">{lang_switch}</span>
<a class="btn btn-blue btn-sm shine" href="{wa_link(T['wa_default'])}" target="_blank">{T['nav_cta']}</a></div>
</div></div>
""")

# ---------------------------------------------------------------- portada
M = T["mock"]
rot = "".join(f"<span>{w}</span>" for w in T["hero_rot"] + T["hero_rot"][:1])
bars = [38, 52, 46, 64, 58, 82, 71]
bar_html = "".join(f'<div class="bar" style="--h:{h}%;--d:{i * 0.08:.2f}s"><i></i><small>{d}</small></div>'
                   for i, (h, d) in enumerate(zip(bars, M["days"])))
items_html = "".join(
    f'<div class="row-it"><span class="dot {st_}"></span><span class="nm">{n}</span>'
    f'<span class="qty {st_}">{q} {M["units"]}</span></div>' for n, q, st_ in M["items"])


def stat_value(v):
    if isinstance(v, str):
        return f'<b data-count="{PRICES[v]}" data-prefix="$" data-locale="{T["calc"]["locale"]}">{cop(PRICES[v])}</b>'
    return f'<b data-count="{v}">{v}</b>'


stats = "".join(f'<div class="stat" data-reveal>{stat_value(v)}<em>{suf}</em><span>{t}</span></div>' for v, suf, t in T["stats2"])
html(f"""
<section class="hero" id="inicio">
<div class="aurora"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="gridlines"></div>
<div class="wrap">
<div class="hero-grid">
<div class="hero-copy">
<div class="pill"><span class="pulse"></span>{T['hero_pill']}</div>
<h1 class="h1">{T['hero_h1']}</h1>
<div class="rotator">{T['hero_rot_pre']} <span class="rot"><span class="rot-in">{rot}</span></span></div>
<p class="lead">{T['hero_lead']}</p>
<div class="ctas">
<a class="btn btn-blue btn-lg shine" href="#contacto" target="_self">{T['hero_cta1']} <span class="arr">→</span></a>
<a class="btn btn-ghost btn-lg" href="#planes" target="_self">{T['nav2'][2][1]}</a>
</div>
<div class="trust"><span class="ok">✓</span>{T['hero_trust']}</div>
</div>
<div class="hero-visual">
<img class="bird" src="{b64('colibri_blanco.png')}" alt="">
<div class="mock">
<div class="mock-top"><span class="dots"><i></i><i></i><i></i></span><b>{M['app']}</b><span class="live"><span class="pulse"></span>{M['live']}</span></div>
<div class="mock-body">
<small>{M['title']}</small>
<div class="big" data-count="{M['total']}" data-prefix="$" data-locale="{T['calc']['locale']}">{cop(M['total'])}</div>
<div class="sub">{M['tickets']}</div>
<div class="bars">{bar_html}</div>
<div class="list">{items_html}</div>
</div>
</div>
<div class="toast t-alert"><span class="ti">!</span><div><b>{M['alert_t']}</b><span>{M['alert']}</span></div><a>{M['alert_btn']}</a></div>
<div class="toast t-wa">{SOCIAL_SVG['whatsapp']}<span>{M['wa']}</span><span class="tick">✓✓</span></div>
</div>
</div>
<div class="stats">{stats}</div>
</div>
</section>
""")

# ---------------------------------------------------------------- cinta de palabras clave
words = "".join(f"<span>{w}</span><i>✦</i>" for w in T["marquee"])
html(f'<div class="marquee"><div class="track">{words}{words}</div></div>')

# ---------------------------------------------------------------- productos
pp = T["prod_price"]
prod_prices = {
    "stock": f'<small>{pp["stock"][0]}</small>{money(PRICES["license"])}<small>{pp["stock"][1]} {cop(PRICES["subscription"])}</small>',
    "flow": f'<small>{pp["flow"][0]}</small>{money(PRICES["flow"])}<small>{pp["flow"][1]}</small>',
    "setup": f'<small>{pp["setup"][0]}</small>{money(PRICES["setup"])}',
    "care": f'<small>{pp["care"][0]}</small>{money(PRICES["care"])}',
}
cards = ""
for i, p in enumerate(T["products"]):
    k = p["icon"]
    cards += f"""
<div class="card prod spot" data-reveal style="--d:{i * 0.08:.2f}s">
<div class="ico">{ICONS[k]}</div>
<span class="tag">{p['tag']}</span>
<div class="pname"><small>SAVA</small>{p['name']}</div>
<p class="pdesc">{T['prod_desc'][k]}</p>
<div class="keys">{"".join(f"<span>{x}</span>" for x in p['keys'])}</div>
<div class="price">{prod_prices[k]}</div>
</div>"""
html(f"""
<section class="sec bg2" id="productos"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{T['prod_kicker']}</div><h2 class="h2">{T['prod_title']}</h2></div>
<div class="cards c4">{cards}</div>
</div></section>
""")

# ---------------------------------------------------------------- proceso
proc = "".join(f'<div class="pstep" data-reveal style="--d:{i * 0.1:.2f}s"><div class="node">{i:02d}</div>'
               f'<div class="pt">{t}</div><p>{d}</p></div>' for i, (t, d) in enumerate(T["proc"], start=1))
html(f"""
<section class="sec dark" id="proceso"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{T['proc_kicker']}</div><h2 class="h2">{T['proc_title']}</h2></div>
<div class="timeline"><div class="line"><i></i></div>{proc}</div>
</div></section>
""")

# ---------------------------------------------------------------- precios
plans = ""
for i, p in enumerate(T["plans2"]):
    items = "".join(f"<li>{x}</li>" for x in p["items"])
    badge = f'<span class="badge">{p["badge"]}</span>' if p["badge"] else ""
    care_line = (T["care_inc"] if p["care"] == "included" else T["care_opt"]).format(m=care_m)
    prefix = '<span class="pre">' + (p["prefix"] or "&nbsp;") + '</span>'
    plans += f"""
<div class="card plan spot {'featured' if p['featured'] else ''}" data-reveal style="--d:{i * 0.1:.2f}s">{badge}
<div class="pl-sub">{p['sub']}</div>
<div class="pl-name">{p['name']}</div>
<div class="amount">{prefix}{money(PRICES[p['key']], 'xl')}</div>
<div class="unit">{p['once']}</div>
<div class="care-line {p['care']}">{care_line}</div>
<ul>{items}</ul>
<div class="fit">{p['fit']}</div>
</div>"""
html(f"""
<section class="sec" id="planes"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{T['price_kicker']}</div><h2 class="h2">{T['price_title']}</h2></div>
<div class="cards c3 plans">{plans}</div>
<div class="addon" data-reveal><span class="ico sm">{ICONS['setup']}</span><span>{T['setup_bar']}</span><span class="addon-price">{money(PRICES['setup'])}</span></div>
</div></section>
""")

# ---------------------------------------------------------------- cotizador (HTML + JS en un iframe)
C = T["calc"]
calc_cfg = json.dumps({"prices": PRICES, "t": C, "wa": WHATSAPP_NUMBER}, ensure_ascii=False)
calc_css = (ASSETS / "calc.css").read_text(encoding="utf-8")
calc_js = (ASSETS / "calc.js").read_text(encoding="utf-8")
opts = "".join(f'<button type="button" class="opt" data-k="{k}">{lbl}</button>' for k, lbl in C["opts"])
html(f'<div class="calc-head" data-reveal><div class="kicker">{C["kicker"]}</div><h3 class="h3c">{C["title"]}</h3></div>')
components.html(f"""<!doctype html><html><head><meta charset="utf-8"><style>{calc_css}</style></head><body>
<div class="calc">
<div class="left">
<div class="q">{C['q']}</div><div class="opts">{opts}</div>
<label class="tg" id="tg-setup"><input type="checkbox" id="setup"><span class="sw"></span><span class="tl">{C['setup']}</span><span class="tp" id="p-setup"></span></label>
<label class="tg" id="tg-care"><input type="checkbox" id="care"><span class="sw"></span><span class="tl">{C['care']}</span><span class="tp" id="p-care"></span></label>
<div class="req" id="req">{C['care_req']}</div>
</div>
<div class="right">
<div class="res"><small>{C['today']}</small><b id="r-today">$0</b></div>
<div class="res"><small>{C['month']}</small><b id="r-month">$0</b></div>
<div class="res soft"><small>{C['year']}</small><b id="r-year">$0</b></div>
<a class="cta" id="cta" target="_blank" rel="noopener">{C['cta']}</a>
</div></div>
<script>window.CFG={calc_cfg};</script><script>{calc_js}</script></body></html>""", height=360)
html(f'<div class="wrap"><p class="price-note">{T["price_note"]}</p></div>')

# ---------------------------------------------------------------- preguntas frecuentes
faq = ""
for q, a in T["faq"]:
    a = a.format(sub=cop(PRICES["subscription"]), care=care_m, lic=cop(PRICES["license"]))
    faq += f'<details class="qa" data-reveal><summary>{q}<span class="pm"></span></summary><div class="ans"><p>{a}</p></div></details>'
html(f"""
<section class="sec bg2" id="faq"><div class="wrap narrow">
<div class="head" data-reveal><div class="kicker">{T['faq_kicker']}</div><h2 class="h2">{T['faq_title']}</h2></div>
<div class="faq">{faq}</div>
</div></section>
""")

# ---------------------------------------------------------------- nosotros
html(f"""
<section class="sec about-sec" id="nosotros"><div class="wrap">
<div class="about" data-reveal>
<div class="ph"><img src="{b64('joseph.jpg')}" alt="{T['about_name']}"></div>
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
<h2 class="h2">{T['contact_title']}</h2>
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
foot_links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav2"])
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

# ---------------------------------------------------------------- animaciones (mejora progresiva)
# Si el navegador bloquea este script, la página se ve completa igual: solo no hay animaciones al bajar.
components.html(f"<script>{(ASSETS / 'fx.js').read_text(encoding='utf-8')}</script>", height=0)
