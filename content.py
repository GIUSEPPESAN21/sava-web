"""Textos de la página de SAVA Software en español (es) e inglés (en).

Para cambiar un texto, edítalo aquí; app.py solo se encarga del diseño.
"""

WHATSAPP_NUMBER = "573222074527"
EMAIL = "joseph.sanchez@uniminuto.edu.co"
PHONE_DISPLAY = "+57 322 207 4527"
LINKEDIN_COMPANY = "https://www.linkedin.com/company/savasoftware/"
# Redes sociales: pega aquí el enlace de cada perfil. Si queda vacío, el botón no aparece.
TIKTOK = "https://www.tiktok.com/@sava_tech_ia"
YOUTUBE = "https://www.youtube.com/@Giuseppe_san"
INSTAGRAM = ""
LINKEDIN_CEO = "https://www.linkedin.com/in/joseph-javier-s%C3%A1nchez-acu%C3%B1a-150410275"


TEXT = {
    "es": {
        "page_title": "SAVA Software | Software e IA para pymes",
        "nav": [("inicio", "Inicio"), ("productos", "Productos"), ("planes", "Planes"),
                ("nosotros", "Nosotros"), ("contacto", "Contacto")],
        "nav_cta": "Diagnóstico gratis",
        "hero_eyebrow": "SOFTWARE + IA PARA PYMES · VALLE DEL CAUCA",
        "hero_title": "CONTROLA TU INVENTARIO.<br>VENDE MÁS.<br><span class='hl'>SIN COMPLICARTE.</span>",
        "hero_sub": ["Software a la medida", "Inteligencia artificial", "Instalado en tu negocio"],
        "hero_cta1": "Agenda tu diagnóstico gratis",
        "hero_cta2": "Ver productos",
        "wa_default": "Hola SAVA, quiero agendar un diagnóstico gratuito para mi negocio.",
        "stats": [("30 MIN", "diagnóstico gratis"), ("HASTA 10", "personas capacitadas"),
                  ("$950.000", "de entrada (COP)"), ("ES · EN", "atención bilingüe")],
        "value": [("A tu medida", "Tu marca · Tus procesos"), ("Con IA", "Reportes · Alertas · Pedidos"),
                  ("Te acompañamos", "Instalación · Capacitación · Soporte")],
        "products_kicker": "PRODUCTOS Y SERVICIOS",
        "products_title": "CUATRO PIEZAS. <span class='hl'>UN NEGOCIO EN ORDEN.</span>",
        "products": [
            {"name": "STOCK", "tag": "SOFTWARE", "icon": "stock",
             "keys": ["Inventario", "Ventas", "Códigos de barras", "Reportes PDF"],
             "price": "Licencia $4.000.000 · o $950.000 + Care"},
            {"name": "FLOW", "tag": "SOFTWARE", "icon": "flow",
             "keys": ["WhatsApp", "Pedidos", "Recordatorios", "IA"],
             "price": "Desde $950.000 + Care"},
            {"name": "SETUP", "tag": "SERVICIO", "icon": "setup",
             "keys": ["Instalación", "Carga de inventario", "Capacitación x10"],
             "price": "$1.250.000 – $1.500.000"},
            {"name": "CARE", "tag": "SERVICIO", "icon": "care",
             "keys": ["Soporte", "Fallas", "Mejoras mensuales"],
             "price": "$70.000 – $90.000 / mes"},
        ],
        "plans_kicker": "PLANES",
        "plans_title": "ELIGE CÓMO <span class='hl'>EMPEZAR</span>",
        "plans": [
            {"name": "SUSCRIPCIÓN", "price": "$950.000", "unit": "Entrada + SAVA Care desde $70.000/mes",
             "items": ["SAVA Stock o Flow a tu medida", "Soporte y mejoras incluidos", "Mes a mes, sin permanencia"],
             "featured": True, "badge": "MÁS ELEGIDO"},
            {"name": "LICENCIA", "price": "$4.000.000", "unit": "pago único",
             "items": ["SAVA Stock o Flow a tu medida", "Uso permanente", "SAVA Care opcional"],
             "featured": False, "badge": ""},
        ],
        "plans_addon": "+ <b>SAVA Setup</b> · Instalación y capacitación · $1.250.000 – $1.500.000",
        "plans_note": "Precios en COP · Noviembre 2026 · Compatible con Alegra, Siigo y tu facturador",
        "steps_title": "ASÍ TRABAJAMOS",
        "steps": ["DIAGNÓSTICO", "DEMO", "A TU MEDIDA", "SETUP", "CARE"],
        "about_kicker": "NOSOTROS",
        "about_name": "Joseph Javier Sánchez Acuña",
        "about_role": "CEO y fundador",
        "about_bio": ["Ingeniería industrial", "Software", "IA para pymes", "UNIMINUTO · Uniandes"],
        "about_team": ["Marketing", "Ventas", "Desarrollo", "Soporte", "Instalación"],
        "contact_kicker": "CONTACTO",
        "contact_title": "AGENDA TU <span class='hl'>DIAGNÓSTICO GRATIS</span>",
        "contact_sub": ["30 minutos", "Gratis", "Sin compromiso"],
        "contact_labels": {"name": "Nombre *", "email": "Correo", "company": "Negocio", "product": "¿Qué te interesa?",
                           "message": "Cuéntanos de tu negocio (opcional)", "phone": "WhatsApp *",
                           "consent": "Autorizo a SAVA a usar mis datos para responder esta solicitud (Ley 1581 de 2012). *",
                           "newsletter": "Quiero recibir novedades y promociones por correo.",
                           "submit": "QUIERO MI DIAGNÓSTICO",
                           "err_name": "Escribe tu nombre.", "err_contact": "Déjanos tu WhatsApp o tu correo para responderte.",
                           "err_email": "Revisa el correo: parece incompleto.", "err_consent": "Marca la casilla de autorización de datos para poder enviarlo.",
                           "ok": "¡Listo! Recibimos tu solicitud y te contactaremos pronto.",
                           "ok_nosave": "¡Listo! Para asegurar tu cita, termina el envío por WhatsApp.",
                           "open_wa": "Escribir por WhatsApp", "not_sure": "Aún no lo sé"},
        "contact_info": [("WHATSAPP", PHONE_DISPLAY), ("CORREO", EMAIL), ("UBICACIÓN", "Buga, Valle del Cauca")],
        "footer_tag": "Software e IA para pymes · Inventarios · Ventas · Procesos",
        "footer_rights": "© 2026 SAVA Software · Buga, Valle del Cauca, Colombia",
        "follow": "SÍGUENOS",
        "privacy_title": "Tratamiento de datos personales",
        "privacy": "SAVA Software, representada por Joseph Javier Sánchez Acuña, trata los datos que envías en este formulario (nombre, correo, WhatsApp, negocio y mensaje) solo para responder tu solicitud y, si lo autorizas, enviarte novedades de SAVA, conforme a la Ley 1581 de 2012. Puedes conocer, actualizar, rectificar o pedir la eliminación de tus datos escribiendo a " + EMAIL + ".",
    },
    "en": {
        "page_title": "SAVA Software | Software and AI for small businesses",
        "nav": [("inicio", "Home"), ("productos", "Products"), ("planes", "Pricing"),
                ("nosotros", "About"), ("contacto", "Contact")],
        "nav_cta": "Free assessment",
        "hero_eyebrow": "SOFTWARE + AI FOR SMALL BUSINESSES · COLOMBIA",
        "hero_title": "CONTROL YOUR INVENTORY.<br>SELL MORE.<br><span class='hl'>KEEP IT SIMPLE.</span>",
        "hero_sub": ["Custom software", "Artificial intelligence", "Installed on site"],
        "hero_cta1": "Book your free assessment",
        "hero_cta2": "See products",
        "wa_default": "Hi SAVA, I would like to book a free assessment for my business.",
        "stats": [("30 MIN", "free assessment"), ("UP TO 10", "people trained"),
                  ("COP 950K", "to get started"), ("ES · EN", "bilingual support")],
        "value": [("Tailor-made", "Your brand · Your processes"), ("With AI", "Reports · Alerts · Orders"),
                  ("We stay with you", "Installation · Training · Support")],
        "products_kicker": "PRODUCTS AND SERVICES",
        "products_title": "FOUR PIECES. <span class='hl'>ONE ORGANIZED BUSINESS.</span>",
        "products": [
            {"name": "STOCK", "tag": "SOFTWARE", "icon": "stock",
             "keys": ["Inventory", "Sales", "Barcodes", "PDF reports"],
             "price": "COP 4M license · or COP 950K + Care"},
            {"name": "FLOW", "tag": "SOFTWARE", "icon": "flow",
             "keys": ["WhatsApp", "Orders", "Reminders", "AI"],
             "price": "From COP 950K + Care"},
            {"name": "SETUP", "tag": "SERVICE", "icon": "setup",
             "keys": ["Installation", "Inventory load", "Training x10"],
             "price": "COP 1.25M – 1.5M"},
            {"name": "CARE", "tag": "SERVICE", "icon": "care",
             "keys": ["Support", "Bug fixes", "Monthly upgrades"],
             "price": "COP 70K – 90K / month"},
        ],
        "plans_kicker": "PRICING",
        "plans_title": "CHOOSE HOW TO <span class='hl'>START</span>",
        "plans": [
            {"name": "SUBSCRIPTION", "price": "COP 950K", "unit": "Upfront + SAVA Care from COP 70K/month",
             "items": ["Custom SAVA Stock or Flow", "Support and upgrades included", "Month to month, no lock-in"],
             "featured": True, "badge": "MOST POPULAR"},
            {"name": "LICENSE", "price": "COP 4M", "unit": "one-time payment",
             "items": ["Custom SAVA Stock or Flow", "Permanent use", "SAVA Care optional"],
             "featured": False, "badge": ""},
        ],
        "plans_addon": "+ <b>SAVA Setup</b> · On-site installation and training · COP 1.25M – 1.5M",
        "plans_note": "Prices in COP · November 2026 · Works with Alegra, Siigo and your e-invoicing tool",
        "steps_title": "HOW WE WORK",
        "steps": ["ASSESSMENT", "DEMO", "CUSTOMIZE", "SETUP", "CARE"],
        "about_kicker": "ABOUT",
        "about_name": "Joseph Javier Sánchez Acuña",
        "about_role": "CEO and founder",
        "about_bio": ["Industrial engineering", "Software", "AI for small businesses", "UNIMINUTO · Uniandes"],
        "about_team": ["Marketing", "Sales", "Development", "Support", "Installation"],
        "contact_kicker": "CONTACT",
        "contact_title": "BOOK YOUR <span class='hl'>FREE ASSESSMENT</span>",
        "contact_sub": ["30 minutes", "Free", "No strings attached"],
        "contact_labels": {"name": "Name *", "email": "Email", "company": "Business", "product": "What are you interested in?",
                           "message": "Tell us about your business (optional)", "phone": "WhatsApp *",
                           "consent": "I authorize SAVA to use my data to answer this request (Colombian Law 1581 of 2012). *",
                           "newsletter": "I want to receive news and offers by email.",
                           "submit": "BOOK MY ASSESSMENT",
                           "err_name": "Please add your name.", "err_contact": "Leave your WhatsApp or email so we can reply.",
                           "err_email": "Please check your email address.", "err_consent": "Please tick the data authorization box to send it.",
                           "ok": "Done! We received your request and will contact you soon.",
                           "ok_nosave": "Done! To confirm your slot, finish on WhatsApp.",
                           "open_wa": "Message us on WhatsApp", "not_sure": "Not sure yet"},
        "contact_info": [("WHATSAPP", PHONE_DISPLAY), ("EMAIL", EMAIL), ("LOCATION", "Buga, Valle del Cauca, Colombia")],
        "footer_tag": "Software and AI for small businesses · Inventory · Sales · Processes",
        "footer_rights": "© 2026 SAVA Software · Buga, Valle del Cauca, Colombia",
        "follow": "FOLLOW US",
        "privacy_title": "Personal data policy",
        "privacy": "SAVA Software, represented by Joseph Javier Sánchez Acuña, processes the data you send in this form (name, email, WhatsApp, business and message) only to answer your request and, if you agree, send you SAVA news, in accordance with Colombian Law 1581 of 2012. You can access, update, correct or request deletion of your data by writing to " + EMAIL + ".",
    },
}


# --- Estilo "Mayúscula Inicial": los textos en MAYÚSCULAS se pasan a minúsculas y el CSS
# (text-transform: capitalize) pone la primera letra de cada palabra en mayúscula.
import re as _re

_KEEP = {"SAVA": "SAVA", "IA": "IA", "AI": "AI", "COP": "COP", "PDF": "PDF",
         "WHATSAPP": "WhatsApp", "4M": "4M", "950K": "950K", "1.25M": "1.25M", "1.5M": "1.5M"}


def _soft(s: str) -> str:
    letters = _re.sub(r"<[^>]+>|[^A-Za-zÁÉÍÓÚÑÜáéíóúñü]", "", s)
    if not letters or letters != letters.upper() or s.strip() in ("ES · EN",):
        return s
    def word(m):
        w = m.group(0)
        return _KEEP.get(w, w.lower())
    parts = _re.split(r"(<[^>]+>)", s)
    return "".join(p if p.startswith("<") else _re.sub(r"[^\s·,.:;!?()→\-–/+]+", word, p) for p in parts)


def _walk(x):
    if isinstance(x, str):
        return _soft(x)
    if isinstance(x, list):
        return [_walk(i) for i in x]
    if isinstance(x, tuple):
        return tuple(_walk(i) for i in x)
    if isinstance(x, dict):
        return {k: _walk(v) for k, v in x.items()}
    return x


TEXT = _walk(TEXT)
