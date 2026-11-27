"""Página web de SAVA Software (Streamlit).

Ejecutar en local:  streamlit run app.py
Los textos y precios están en content.py, el diseño en assets/style.css
y las animaciones y el cotizador en assets/fx.js.
"""
import base64
import html as _html
import importlib
import json
from pathlib import Path
from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

import content

importlib.reload(content)  # Streamlit Cloud: siempre usa la última versión de content.py
from content import (EMAIL, INSTAGRAM, INSTAGRAM_DM, LINKEDIN_COMPANY, PHONE_DISPLAY, PRICES, TEXT,  # noqa: E402
                     TIKTOK, WHATSAPP_NUMBER, YOUTUBE)

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
    # Sin sangrías: Markdown trata como código las líneas con 4 espacios al inicio.
    st.markdown("\n".join(line.strip() for line in block.splitlines()), unsafe_allow_html=True)


def cop(n: int) -> str:
    """Pesos colombianos: $950.000 en español y $950,000 en inglés."""
    txt = f"{n:,}"
    return "$" + (txt.replace(",", ".") if lang == "es" else txt)


def money(n: int, size: str = "") -> str:
    return f'<span class="money {size}">{cop(n)}<span class="code">COP</span></span>'


def wa_link(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"


WA_DEFAULT = wa_link(T["wa_default"])
care_m = cop(PRICES["care"])

SOCIAL_SVG = {
    "whatsapp": '<svg viewBox="0 0 24 24"><path d="M20.5 3.5A11 11 0 0 0 3.2 17.1L2 22l5-1.3A11 11 0 0 0 20.5 3.5zM12 20.1a9 9 0 0 1-4.6-1.3l-.3-.2-3 .8.8-2.9-.2-.3A9 9 0 1 1 12 20.1zm5-6.7c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1l-.9 1.1c-.2.2-.3.2-.6.1a7.4 7.4 0 0 1-3.7-3.2c-.3-.5.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-2c-.2-.5-.4-.5-.6-.5h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.6-.6 1.8-1.3.2-.6.2-1.2.2-1.3-.1-.1-.2-.2-.5-.3z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.7 4.8 6.1V21h-4v-5.4c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2-2.8V9.1a6.3 6.3 0 1 0 5.4 6.3V8.6a8 8 0 0 0 4.4 1.3V6.5a4.5 4.5 0 0 1-4.4-4.5z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2c-2.7 0-3 0-4.1.1C4.2 2.3 2.3 4.2 2.1 7.9 2 9 2 9.3 2 12s0 3 .1 4.1c.2 3.7 2.1 5.6 5.8 5.8 1.1.1 1.4.1 4.1.1s3 0 4.1-.1c3.7-.2 5.6-2.1 5.8-5.8.1-1.1.1-1.4.1-4.1s0-3-.1-4.1c-.2-3.7-2.1-5.6-5.8-5.8C15 2 14.7 2 12 2z"/></svg>',
}


def social_row(cls: str = "social-icons") -> str:
    items = [("whatsapp", WA_DEFAULT, "WhatsApp"), ("instagram", INSTAGRAM, "Instagram"),
             ("tiktok", TIKTOK, "TikTok"), ("youtube", YOUTUBE, "YouTube"), ("linkedin", LINKEDIN_COMPANY, "LinkedIn")]
    links = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}" title="{n}">{SOCIAL_SVG[k]}</a>'
                    for k, u, n in items if u)
    return f'<div class="{cls}">{links}</div>'


ICONS = {
    "stock": '<svg viewBox="0 0 24 24"><path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/></svg>',
    "flow": '<svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h7a3 3 0 0 1 0 6h-4a3 3 0 0 0 0 6h7"/></svg>',
    "setup": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M8.5 10l2.5 2.5L15.5 8"/></svg>',
    "care": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L15.5 10"/></svg>',
    "bell": '<svg viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8"/><path d="M10.3 20a1.9 1.9 0 0 0 3.4 0"/></svg>',
    "chat": '<svg viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14h4"/></svg>',
    "brush": '<svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 1 0 0 18c1 0 1.6-.8 1.6-1.6 0-.5-.2-.8-.4-1.1-.3-.3-.4-.7-.4-1.1 0-.9.7-1.6 1.6-1.6H16a5 5 0 0 0 5-5c0-4.3-4-7.6-9-7.6z"/><circle cx="7.5" cy="11.5" r="1"/><circle cx="10.5" cy="7.5" r="1"/><circle cx="15.5" cy="8.5" r="1"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
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
<a class="brand" href="#inicio" target="_self"><img src="{b64('logo_blanco.png')}" alt="SAVA Software"></a>
<div class="links">{links}</div>
<div class="right">{social_row("social-icons nav-social")}<span class="lang">{lang_switch}</span>
<a class="btn btn-blue btn-sm shine" href="#contacto" target="_self"><span class="long">{T['nav_cta']}</span><span class="short">{T['nav_cta_short']}</span></a></div>
</div><div class="progress"><i></i></div></div>
""")


# ---------------------------------------------------------------- portada
def stat_value(v) -> str:
    if isinstance(v, str):
        n = PRICES[v]
        return f'<b data-count="{n}" data-prefix="$" data-locale="{T["calc"]["locale"]}">{cop(n)}</b>'
    return f'<b data-count="{v}">{v}</b>'


stats = "".join(f'<div class="stat">{stat_value(v)}<em>{suf}</em><span>{t}</span></div>' for v, suf, t in T["stats"])
chips = "".join(f'<span style="--i:{i}">{k}</span>' for i, k in enumerate(T["hero_sub"]))
words = "".join(f"<span>{w}</span><i>✦</i>" for w in T["marquee"])
html(f"""
<section class="hero" id="inicio">
<div class="aurora"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="gridlines"></div>
<div class="wrap">
<div class="emblem"><span class="halo"></span><span class="ring r1"></span><span class="ring r2"></span><img src="{b64('colibri_blanco.png')}" alt="SAVA"></div>
<div class="eyebrow"><span class="pulse"></span>{T['hero_eyebrow']}</div>
<div class="h1">{T['hero_title']}</div>
<div class="keys hero-keys">{chips}</div>
<div class="ctas">
<a class="btn btn-blue btn-lg shine" href="#contacto" target="_self">{T['hero_cta1']} <span class="arr">→</span></a>
<a class="btn btn-ghost btn-lg" href="#planes" target="_self">{T['hero_cta2']}</a>
</div>
<div class="stats">{stats}</div>
</div>
<div class="marquee"><div class="track">{words}{words}</div></div>
</section>
""")

# ---------------------------------------------------------------- propuesta de valor
value = "".join(f'<div class="val" data-reveal style="--d:{i * 0.1:.1f}s"><div class="vt">{t}</div><div class="vk">{d}</div></div>'
                for i, (t, d) in enumerate(T["value"]))
html(f'<section class="valuebar"><div class="wrap vals">{value}</div></section>')

# ---------------------------------------------------------------- productos
price_vars = {k: cop(v) for k, v in PRICES.items()}
cards = ""
for i, p in enumerate(T["products"]):
    k = p["key"]
    cards += f"""
<div class="card prod spot" data-reveal style="--d:{i * 0.08:.2f}s">
<div class="top"><div class="ico">{ICONS[k]}</div><span class="tag">{p['tag']}</span></div>
<div class="pname"><small>SAVA</small>{p['name']}</div>
<div class="keys">{"".join(f"<span>{x}</span>" for x in p['keys'])}</div>
<div class="price">{T['prod_price'][k].format(**price_vars)}</div>
</div>"""
steps = "".join(f'<span class="chip-step" style="--i:{i}"><b>{i + 1:02d}</b> {s}</span>'
                + ('<span class="arrow">→</span>' if i < len(T["steps"]) - 1 else "")
                for i, s in enumerate(T["steps"]))
html(f"""
<section class="sec bg2" id="productos"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{T['products_kicker']}</div><div class="h2">{T['products_title']}</div></div>
<div class="cards c4">{cards}</div>
<div class="flow" data-reveal><span class="flow-t">{T['steps_title']}</span>{steps}</div>
</div></section>
""")

# ---------------------------------------------------------------- así se ve (maqueta animada)
M = T["mock"]
bars = [38, 52, 46, 64, 58, 82, 71]
bar_html = "".join(f'<div class="bar" style="--h:{h}%;--d:{i * 0.08:.2f}s"><i></i><small>{d}</small></div>'
                   for i, (h, d) in enumerate(zip(bars, M["days"])))
items_html = "".join(f'<div class="row-it" style="--i:{i}"><span class="dot {s}"></span><span class="nm">{n}</span>'
                     f'<span class="qty {s}">{q} {M["units"]}</span></div>' for i, (n, q, s) in enumerate(M["items"]))
points = "".join(f'<div class="pt" data-reveal style="--d:{i * 0.12:.2f}s"><span class="pi">{ICONS[ic]}</span><div><b>{t}</b><span>{d}</span></div></div>'
                 for i, ((t, d), ic) in enumerate(zip(T["show_points"], ["bell", "chat", "brush"])))
html(f"""
<section class="sec dark" id="demo"><div class="aurora soft"><i class="a1"></i><i class="a2"></i></div><div class="wrap">
<div class="show">
<div class="show-copy">
<div class="head" data-reveal><div class="kicker">{T['show_kicker']}</div><div class="h2">{T['show_title']}</div></div>
<div class="points">{points}</div>
</div>
<div class="show-visual" data-reveal>
<div class="mock" data-tilt>
<div class="mock-top"><span class="dots"><i></i><i></i><i></i></span><b>{M['app']}</b><span class="live"><span class="pulse"></span>{M['live']}</span></div>
<div class="mock-body">
<small>{M['title']}</small>
<div class="big" data-count="{M['total']}" data-prefix="$" data-locale="{T['calc']['locale']}">{cop(M['total'])}</div>
<div class="sub">{M['tickets']}</div>
<div class="bars">{bar_html}</div>
<div class="list">{items_html}</div>
<div class="demo-note">{M['demo']}</div>
</div>
</div>
<div class="toasts">
<div class="toast t-alert"><span class="ti">!</span><div><b>{M['alert_t']}</b><span>{M['alert']}</span></div><span class="tb">{M['alert_btn']}</span></div>
<div class="toast t-wa">{SOCIAL_SVG['whatsapp']}<span>{M['wa']}</span><span class="tick">✓✓</span></div>
</div>
</div>
</div>
</div></section>
""")

# ---------------------------------------------------------------- precios
year1 = {
    "subscription": f'{cop(PRICES["subscription"] + 12 * PRICES["care"])}<span class="code">COP</span>',
    "license": f'{cop(PRICES["license"])}<span class="code">COP</span> <em>· {T["year1_nocare"]}</em>',
    "flow": f'<em>{T["year1_from"]}</em> {cop(PRICES["flow"] + 12 * PRICES["care"])}<span class="code">COP</span>',
}
plan_price_txt = {
    "subscription": f'{cop(PRICES["subscription"])} + {care_m}{T["per_month"]}',
    "license": cop(PRICES["license"]),
    "flow": f'{T["plans"][2]["pre"].lower()} {cop(PRICES["flow"])} + {care_m}{T["per_month"]}',
}
plans = ""
for i, p in enumerate(T["plans"]):
    k = p["key"]
    items = "".join(f"<li>{x}</li>" for x in p["items"])
    badge = f'<span class="badge">{p["badge"]}</span>' if p["badge"] else ""
    care_line = (T["care_inc"] if p["care"] == "included" else T["care_opt"]).format(m=care_m)
    pay = p["pay"].format(half=cop(PRICES["subscription"] // 2))
    wa = wa_link(T["plan_wa"].format(plan=p["name"], price=plan_price_txt[k]))
    plans += f"""
<div class="card plan spot {'featured' if p['featured'] else ''}" data-reveal style="--d:{i * 0.1:.1f}s">{badge}
<div class="pl-name">{p['name']}</div>
<div class="fit">{p['fit']}</div>
<div class="pre">{p['pre'] or '&nbsp;'}</div>
<div class="amount">{money(PRICES[k], 'xl')}</div>
<div class="unit">{pay}</div>
<div class="care-line {p['care']}">{care_line}</div>
<ul>{items}</ul>
<div class="y1"><small>{T['year1']}</small><b>{year1[k]}</b></div>
<a class="btn {'btn-blue shine' if p['featured'] else 'btn-line'} plan-btn" href="{wa}" target="_blank" rel="noopener">{T['plan_cta']} <span class="arr">→</span></a>
</div>"""
care_items = "".join(f"<li>{x}</li>" for x in T["care_items"])
html(f"""
<section class="sec" id="planes"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{T['plans_kicker']}</div><div class="h2">{T['plans_title']}</div><p class="lead">{T['plans_lead']}</p></div>
<div class="cards c3 plans">{plans}</div>
<div class="cards c2 extras">
<div class="card extra spot" data-reveal>
<div class="ex-top"><span class="ico">{ICONS['setup']}</span><div><div class="ex-t">{T['setup_title']}</div><div class="ex-p">{money(PRICES['setup'])}</div></div></div>
<p>{T['setup_desc']}</p><div class="ex-tail">{T['setup_tail']}</div>
</div>
<div class="card extra spot" data-reveal style="--d:.1s">
<div class="ex-top"><span class="ico">{ICONS['care']}</span><div><div class="ex-t">{T['care_title']}</div><div class="ex-p">{money(PRICES['care'])}<span class="pm">{T['per_month']}</span></div></div></div>
<ul class="ex-list">{care_items}</ul>
</div>
</div>
</div></section>
""")

# ---------------------------------------------------------------- cotizador (en la página, sin iframe)
C = T["calc"]
cfg = _html.escape(json.dumps({"prices": PRICES, "t": C, "wa": WHATSAPP_NUMBER}, ensure_ascii=False), quote=True)
opts = "".join(f'<button type="button" class="opt{" on" if k == "subscription" else ""}" data-k="{k}">{lbl}</button>'
               for k, lbl in C["opts"])
start_today = PRICES["subscription"]
start_month = PRICES["care"]
start_wa = wa_link(C["wa"].format(plan=C["opts"][0][1], setup="", care="", today=cop(start_today),
                                  month=C["monthly_txt"].format(m=cop(start_month))))
html(f"""
<section class="sec bg2" id="cotizador"><div class="wrap">
<div class="head" data-reveal><div class="kicker">{C['kicker']}</div><div class="h2">{C['title']}</div></div>
<div class="calc" data-calc="{cfg}" data-reveal>
<div class="c-left">
<div class="q">{C['q']}</div>
<div class="opts">{opts}</div>
<label class="tg"><input type="checkbox" class="c-setup"><span class="sw"></span><span class="tl">{C['setup']}</span><span class="tp">+ {cop(PRICES['setup'])}</span></label>
<label class="tg locked"><input type="checkbox" class="c-care" checked disabled><span class="sw"></span><span class="tl">{C['care']}</span><span class="tp">+ {care_m}{C['mo']}</span></label>
<div class="req">{C['care_req']}</div>
</div>
<div class="c-right">
<div class="res"><small>{C['today']}</small><b class="r-today">{cop(start_today)}<span class="code">COP</span></b></div>
<div class="res"><small>{C['month']}</small><b class="r-month">{cop(start_month)}<span class="code">COP</span></b></div>
<div class="res soft"><small>{C['year']}</small><b class="r-year">{cop(start_today + 12 * start_month)}<span class="code">COP</span></b></div>
<a class="btn btn-wa c-cta" href="{start_wa}" target="_blank" rel="noopener">{SOCIAL_SVG['whatsapp']}<span>{C['cta']}</span></a>
</div>
</div>
<p class="price-note">{T['price_note']}</p>
</div></section>
""")

# ---------------------------------------------------------------- preguntas frecuentes
faq = ""
for q, a in T["faq"]:
    a = a.format(sub=cop(PRICES["subscription"]), care=care_m, lic=cop(PRICES["license"]))
    faq += f'<details class="qa" data-reveal><summary>{q}<span class="pm"></span></summary><div class="ans"><p>{a}</p></div></details>'
html(f"""
<section class="sec" id="faq"><div class="wrap narrow">
<div class="head" data-reveal><div class="kicker">{T['faq_kicker']}</div><div class="h2">{T['faq_title']}</div></div>
<div class="faq">{faq}</div>
</div></section>
""")

# ---------------------------------------------------------------- agenda tu diagnóstico (WhatsApp e Instagram)
cta_chips = "".join(f"<span>{c}</span>" for c in T["cta_chips"])
html(f"""
<section class="cta-sec" id="contacto"><div class="wrap">
<div class="cta-box" data-reveal>
<div class="aurora soft"><i class="a1"></i><i class="a2"></i></div>
<img class="cta-bird" src="{b64('colibri_blanco.png')}" alt="">
<div class="kicker light">{T['cta_kicker']}</div>
<div class="h2">{T['cta_title']}</div>
<div class="keys cta-keys">{cta_chips}</div>
<p class="cta-lead">{T['cta_lead']}</p>
<div class="cta-btns">
<a class="big-btn wa" href="{WA_DEFAULT}" target="_blank" rel="noopener"><span class="bi">{SOCIAL_SVG['whatsapp']}</span><span class="bt"><b>{T['cta_wa']}</b><small>{T['cta_wa_sub']}</small></span><span class="ba">{ICONS['arrow']}</span></a>
<a class="big-btn ig" href="{INSTAGRAM_DM}" target="_blank" rel="noopener"><span class="bi">{SOCIAL_SVG['instagram']}</span><span class="bt"><b>{T['cta_ig']}</b><small>{T['cta_ig_sub']}</small></span><span class="ba">{ICONS['arrow']}</span></a>
</div>
<div class="cta-foot">WhatsApp {PHONE_DISPLAY} · Instagram @{content.INSTAGRAM_USER}</div>
</div>
</div></section>
""")

# ---------------------------------------------------------------- pie de página
foot_links = "".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in T["nav"])
html(f"""
<div class="foot"><div class="wrap">
<div class="row">
<div><img src="{b64('logo_blanco.png')}" alt="SAVA Software"><p>{T['footer_tag']}</p></div>
<div class="flinks">{foot_links}</div>
<div><b class="follow">{T['follow']}</b>{social_row()}
<a class="plain" href="{WA_DEFAULT}" target="_blank">WhatsApp {PHONE_DISPLAY}</a><a class="plain" href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
<details><summary>{T['privacy_title']}</summary><p>{T['privacy']}</p></details>
<div class="copy">{T['footer_rights']}</div>
</div></div>
""")

html(f'<a class="wa-float" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_SVG["whatsapp"]}</a>')

# ---------------------------------------------------------------- animaciones y cotizador (mejora progresiva)
# Si el navegador bloquea este script, la página se ve completa igual: solo no hay animaciones ni cálculo en vivo.
components.html(f"<script>{(ASSETS / 'fx.js').read_text(encoding='utf-8')}</script>", height=0)
