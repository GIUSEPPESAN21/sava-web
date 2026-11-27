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
INSTAGRAM = "https://www.instagram.com/savasoftware"
LINKEDIN_CEO = "https://www.linkedin.com/in/joseph-javier-s%C3%A1nchez-acu%C3%B1a-150410275"
SITE_URL = "https://savasoftware.streamlit.app"

# Precios oficiales en pesos colombianos (COP), vigentes desde el 26 de noviembre de 2026.
# Cambia un número aquí y se actualiza en toda la página (tarjetas, planes y cotizador).
PRICES = {"license": 4_000_000, "subscription": 950_000, "flow": 800_000, "setup": 400_000, "care": 85_000}


TEXT = {
    "es": {
        "nav2": [("productos", "Productos"), ("proceso", "Cómo trabajamos"), ("planes", "Precios"),
                 ("faq", "Preguntas"), ("contacto", "Contacto")],
        "hero_pill": "Software + IA para pymes · Buga · Tuluá · Cali",
        "hero_h1": "Controla tu inventario.<br>Vende más.<br><span class='hl'>Sin complicarte.</span>",
        "hero_rot_pre": "Con",
        "hero_rot": ["software a tu medida", "inteligencia artificial", "instalación en tu negocio", "soporte cada mes"],
        "hero_lead": "Un programa con tu marca que te dice cada día qué tienes, qué vendiste y qué debes pedir. Lo instalamos en tu negocio y capacitamos a tu equipo.",
        "hero_trust": "Compatible con Alegra, Siigo y tu facturador electrónico",
        "stats2": [(30, " min", "Diagnóstico gratis"), (48, " h", "Demo con tus productos"),
                   (10, "", "Personas capacitadas"), ("subscription", "", "COP para empezar")],
        "mock": {"app": "SAVA Stock", "title": "Ventas de hoy", "total": 1_284_000, "tickets": "23 ventas · 41 unidades",
                 "alert_t": "Stock bajo", "alert": "Bolso tote rosa · quedan 2", "alert_btn": "Pedir",
                 "wa": "Resumen del día enviado a tu WhatsApp", "live": "En vivo",
                 "items": [("Bolso tote rosa", 2, "low"), ("Billetera café", 14, "ok"), ("Morral negro", 9, "ok")],
                 "days": ["L", "M", "M", "J", "V", "S", "D"], "units": "und."},
        "marquee": ["Inventario", "Ventas", "Códigos de barras", "Reportes PDF", "Alertas de stock",
                    "Pedidos por WhatsApp", "Inteligencia artificial", "Tu marca", "Capacitación", "Soporte"],
        "prod_kicker": "Productos y servicios",
        "prod_title": "Cuatro piezas. <span class='hl'>Un negocio en orden.</span>",
        "prod_desc": {"stock": "Inventario y ventas a la medida, con tu logo y tus colores.",
                      "flow": "Automatiza pedidos, recordatorios y reportes con IA.",
                      "setup": "Lo dejamos funcionando en tu negocio y capacitamos a tu equipo.",
                      "care": "Soporte, copias de seguridad y mejoras cada mes."},
        "prod_price": {"stock": ("Licencia", "o suscripción desde"), "flow": ("Desde", "+ SAVA Care"),
                       "setup": ("Pago único", ""), "care": ("Al mes", "")},
        "proc_kicker": "Cómo trabajamos",
        "proc_title": "De la primera visita a tu programa <span class='hl'>funcionando</span>",
        "proc": [("Diagnóstico", "30 minutos gratis en tu negocio"), ("Demo", "Con tus propios productos en 48 horas"),
                 ("A tu medida", "Tu marca, tus procesos y tus reportes"), ("Setup", "Instalación y capacitación de hasta 10 personas"),
                 ("Care", "Soporte y mejoras cada mes")],
        "price_kicker": "Precios en pesos colombianos",
        "price_title": "Elige cómo <span class='hl'>empezar</span>",
        "plans2": [
            {"key": "subscription", "name": "Suscripción", "sub": "SAVA Stock", "prefix": "", "once": "de entrada",
             "care": "included", "fit": "Ideal para negocios de hasta 10 personas", "badge": "Más elegido", "featured": True,
             "items": ["Programa con tu marca", "Carga de tu catálogo", "Soporte y mejoras incluidos", "Entrada en 1 o 2 cuotas"]},
            {"key": "license", "name": "Licencia", "sub": "SAVA Stock", "prefix": "", "once": "pago único",
             "care": "optional", "fit": "Ideal para empresas de más de 10 personas", "badge": "", "featured": False,
             "items": ["El programa queda de tu empresa", "Uso permanente", "Hasta 3 cuotas", "Soporte opcional"]},
            {"key": "flow", "name": "Flow", "sub": "Automatización con IA", "prefix": "Desde", "once": "de entrada",
             "care": "included", "fit": "Ideal si recibes pedidos por WhatsApp", "badge": "", "featured": False,
             "items": ["Pedidos y recordatorios por WhatsApp", "Reportes automáticos al celular", "Conexión con tus hojas de cálculo", "Soporte y mejoras incluidos"]},
        ],
        "care_inc": "+ {m} al mes de SAVA Care", "care_opt": "SAVA Care opcional: {m} al mes", "per_month": "/mes",
        "setup_bar": "<b>SAVA Setup</b> · Instalación, carga de inventario y capacitación de hasta 10 personas",
        "price_note": "Precios en pesos colombianos (COP) · Noviembre de 2026 · SAVA trabaja junto a tu facturador electrónico; no emite factura ante la DIAN.",
        "calc": {"kicker": "Cotizador", "title": "Arma tu plan en segundos", "q": "¿Qué necesitas?",
                 "opts": [["subscription", "Suscripción SAVA Stock"], ["license", "Licencia SAVA Stock"], ["flow", "SAVA Flow"]],
                 "setup": "Instalación y capacitación (SAVA Setup)", "care": "Soporte y mejoras (SAVA Care)",
                 "care_req": "Incluido en este plan", "today": "Pagas al empezar", "month": "Cada mes",
                 "year": "Total primer año", "none": "Sin mensualidad", "from": "desde", "cta": "Pedir esta cotización por WhatsApp",
                 "wa": "Hola SAVA, quiero cotizar {plan}{setup}{care}. Pago inicial {today}{month}.", "with_setup": " con instalación",
                 "with_care": " y SAVA Care", "monthly_txt": " y {m} al mes", "locale": "es-CO"},
        "faq_kicker": "Preguntas frecuentes",
        "faq_title": "Lo que más nos <span class='hl'>preguntan</span>",
        "faq": [
            ("¿SAVA reemplaza mi facturador electrónico?", "No. SAVA no emite factura electrónica ante la DIAN: controla tu inventario, tus ventas y tus reportes, y trabaja junto a Alegra, Siigo o el facturador que ya usas."),
            ("¿Qué diferencia hay entre la suscripción y la licencia?", "Con la suscripción pagas {sub} de entrada y {care} al mes de SAVA Care, que incluye soporte y mejoras. Con la licencia pagas {lic} una sola vez y el programa queda de tu empresa; SAVA Care es opcional."),
            ("¿Qué incluye SAVA Care?", "Alojamiento, copias de seguridad, corrección de fallas, soporte por WhatsApp y mejoras al programa. Se paga mes a mes."),
            ("¿Puedo pagar en cuotas?", "Sí. La entrada de la suscripción se puede pagar en 2 cuotas y la licencia hasta en 3."),
            ("¿Funciona en el celular?", "Sí. Puedes vender, revisar tu inventario y ver tus reportes desde el computador o desde el celular."),
            ("¿Dónde trabajan?", "En Buga, Tuluá y Cali, con instalación y capacitación presencial en tu negocio."),
        ],
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
             "price": "Desde $800.000 + Care"},
            {"name": "SETUP", "tag": "SERVICIO", "icon": "setup",
             "keys": ["Instalación", "Carga de inventario", "Capacitación x10"],
             "price": "$400.000"},
            {"name": "CARE", "tag": "SERVICIO", "icon": "care",
             "keys": ["Soporte", "Fallas", "Mejoras mensuales"],
             "price": "$85.000 / mes"},
        ],
        "plans_kicker": "PLANES",
        "plans_title": "ELIGE CÓMO <span class='hl'>EMPEZAR</span>",
        "plans": [
            {"name": "STOCK · SUSCRIPCIÓN", "price": "$950.000", "unit": "Entrada + SAVA Care $85.000/mes",
             "items": ["SAVA Stock a tu medida", "SAVA Care incluido: soporte y mejoras", "Mes a mes, sin permanencia"],
             "featured": True, "badge": "MÁS ELEGIDO"},
            {"name": "STOCK · LICENCIA", "price": "$4.000.000", "unit": "pago único",
             "items": ["SAVA Stock a tu medida", "Uso permanente", "SAVA Care opcional · $85.000/mes"],
             "featured": False, "badge": ""},
            {"name": "FLOW", "price": "$800.000", "unit": "Desde · entrada + SAVA Care $85.000/mes",
             "items": ["Automatización con IA", "Pedidos y reportes por WhatsApp", "SAVA Care incluido"],
             "featured": False, "badge": ""},
        ],
        "plans_addon": "+ <b>SAVA Setup</b> · Instalación, carga de inventario y capacitación de hasta 10 personas · $400.000",
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
        "nav2": [("productos", "Products"), ("proceso", "How we work"), ("planes", "Pricing"),
                 ("faq", "FAQ"), ("contacto", "Contact")],
        "hero_pill": "Software + AI for small businesses · Valle del Cauca, Colombia",
        "hero_h1": "Control your inventory.<br>Sell more.<br><span class='hl'>Keep it simple.</span>",
        "hero_rot_pre": "With",
        "hero_rot": ["custom software", "artificial intelligence", "on-site installation", "monthly support"],
        "hero_lead": "Software with your brand that tells you every day what you have, what you sold and what to reorder. We install it in your business and train your team.",
        "hero_trust": "Works with Alegra, Siigo and your e-invoicing tool",
        "stats2": [(30, " min", "Free assessment"), (48, " h", "Demo with your products"),
                   (10, "", "People trained"), ("subscription", "", "COP to get started")],
        "mock": {"app": "SAVA Stock", "title": "Today's sales", "total": 1_284_000, "tickets": "23 sales · 41 units",
                 "alert_t": "Low stock", "alert": "Pink tote bag · 2 left", "alert_btn": "Reorder",
                 "wa": "Daily summary sent to your WhatsApp", "live": "Live",
                 "items": [("Pink tote bag", 2, "low"), ("Brown wallet", 14, "ok"), ("Black backpack", 9, "ok")],
                 "days": ["M", "T", "W", "T", "F", "S", "S"], "units": "pcs"},
        "marquee": ["Inventory", "Sales", "Barcodes", "PDF reports", "Stock alerts", "WhatsApp orders",
                    "Artificial intelligence", "Your brand", "Training", "Support"],
        "prod_kicker": "Products and services",
        "prod_title": "Four pieces. <span class='hl'>One organized business.</span>",
        "prod_desc": {"stock": "Custom inventory and sales software with your logo and colors.",
                      "flow": "Automate orders, reminders and reports with AI.",
                      "setup": "We get it running in your business and train your team.",
                      "care": "Support, backups and upgrades every month."},
        "prod_price": {"stock": ("License", "or subscription from"), "flow": ("From", "+ SAVA Care"),
                       "setup": ("One-time", ""), "care": ("Per month", "")},
        "proc_kicker": "How we work",
        "proc_title": "From the first visit to your software <span class='hl'>up and running</span>",
        "proc": [("Assessment", "30 free minutes at your business"), ("Demo", "With your own products in 48 hours"),
                 ("Customize", "Your brand, processes and reports"), ("Setup", "Installation and training for up to 10 people"),
                 ("Care", "Support and upgrades every month")],
        "price_kicker": "Prices in Colombian pesos",
        "price_title": "Choose how to <span class='hl'>start</span>",
        "plans2": [
            {"key": "subscription", "name": "Subscription", "sub": "SAVA Stock", "prefix": "", "once": "upfront",
             "care": "included", "fit": "Best for businesses of up to 10 people", "badge": "Most popular", "featured": True,
             "items": ["Software with your brand", "Your catalog loaded", "Support and upgrades included", "Pay upfront in 1 or 2 installments"]},
            {"key": "license", "name": "License", "sub": "SAVA Stock", "prefix": "", "once": "one-time payment",
             "care": "optional", "fit": "Best for companies with more than 10 people", "badge": "", "featured": False,
             "items": ["Your company owns the software", "Permanent use", "Up to 3 installments", "Optional support"]},
            {"key": "flow", "name": "Flow", "sub": "AI automation", "prefix": "From", "once": "upfront",
             "care": "included", "fit": "Best if you get orders on WhatsApp", "badge": "", "featured": False,
             "items": ["WhatsApp orders and reminders", "Automatic reports on your phone", "Connected to your spreadsheets", "Support and upgrades included"]},
        ],
        "care_inc": "+ {m} per month for SAVA Care", "care_opt": "SAVA Care optional: {m} per month", "per_month": "/month",
        "setup_bar": "<b>SAVA Setup</b> · Installation, inventory load and training for up to 10 people",
        "price_note": "Prices in Colombian pesos (COP) · November 2026 · SAVA works alongside your e-invoicing tool; it does not issue DIAN invoices.",
        "calc": {"kicker": "Quote builder", "title": "Build your plan in seconds", "q": "What do you need?",
                 "opts": [["subscription", "SAVA Stock subscription"], ["license", "SAVA Stock license"], ["flow", "SAVA Flow"]],
                 "setup": "Installation and training (SAVA Setup)", "care": "Support and upgrades (SAVA Care)",
                 "care_req": "Included in this plan", "today": "You pay to start", "month": "Every month",
                 "year": "First-year total", "none": "No monthly fee", "from": "from", "cta": "Request this quote on WhatsApp",
                 "wa": "Hi SAVA, I would like a quote for {plan}{setup}{care}. Upfront {today}{month}.", "with_setup": " with installation",
                 "with_care": " and SAVA Care", "monthly_txt": " and {m} per month", "locale": "en-US"},
        "faq_kicker": "FAQ",
        "faq_title": "What people <span class='hl'>ask us</span>",
        "faq": [
            ("Does SAVA replace my e-invoicing tool?", "No. SAVA does not issue DIAN electronic invoices: it manages your inventory, sales and reports, and works alongside Alegra, Siigo or the tool you already use."),
            ("What is the difference between the subscription and the license?", "With the subscription you pay {sub} upfront and {care} per month for SAVA Care, which includes support and upgrades. With the license you pay {lic} once and your company owns the software; SAVA Care is optional."),
            ("What does SAVA Care include?", "Hosting, backups, bug fixes, WhatsApp support and software upgrades. It is billed month to month."),
            ("Can I pay in installments?", "Yes. The subscription upfront fee can be split in 2 payments and the license in up to 3."),
            ("Does it work on my phone?", "Yes. You can sell, check your inventory and see your reports from a computer or a phone."),
            ("Where do you work?", "In Buga, Tuluá and Cali (Valle del Cauca, Colombia), with on-site installation and training."),
        ],
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
                  ("COP 950,000", "to get started"), ("ES · EN", "bilingual support")],
        "value": [("Tailor-made", "Your brand · Your processes"), ("With AI", "Reports · Alerts · Orders"),
                  ("We stay with you", "Installation · Training · Support")],
        "products_kicker": "PRODUCTS AND SERVICES",
        "products_title": "FOUR PIECES. <span class='hl'>ONE ORGANIZED BUSINESS.</span>",
        "products": [
            {"name": "STOCK", "tag": "SOFTWARE", "icon": "stock",
             "keys": ["Inventory", "Sales", "Barcodes", "PDF reports"],
             "price": "COP 4,000,000 license · or COP 950,000 + Care"},
            {"name": "FLOW", "tag": "SOFTWARE", "icon": "flow",
             "keys": ["WhatsApp", "Orders", "Reminders", "AI"],
             "price": "From COP 800,000 + Care"},
            {"name": "SETUP", "tag": "SERVICE", "icon": "setup",
             "keys": ["Installation", "Inventory load", "Training x10"],
             "price": "COP 400,000"},
            {"name": "CARE", "tag": "SERVICE", "icon": "care",
             "keys": ["Support", "Bug fixes", "Monthly upgrades"],
             "price": "COP 85,000 / month"},
        ],
        "plans_kicker": "PRICING",
        "plans_title": "CHOOSE HOW TO <span class='hl'>START</span>",
        "plans": [
            {"name": "STOCK · SUBSCRIPTION", "price": "COP 950,000", "unit": "Upfront + SAVA Care COP 85,000/month",
             "items": ["Custom SAVA Stock", "SAVA Care included: support and upgrades", "Month to month, no lock-in"],
             "featured": True, "badge": "MOST POPULAR"},
            {"name": "STOCK · LICENSE", "price": "COP 4,000,000", "unit": "one-time payment",
             "items": ["Custom SAVA Stock", "Permanent use", "SAVA Care optional · COP 85,000/month"],
             "featured": False, "badge": ""},
            {"name": "FLOW", "price": "COP 800,000", "unit": "From · upfront + SAVA Care COP 85,000/month",
             "items": ["AI-powered automation", "Orders and reports on WhatsApp", "SAVA Care included"],
             "featured": False, "badge": ""},
        ],
        "plans_addon": "+ <b>SAVA Setup</b> · Installation, inventory load and training for up to 10 people · COP 400,000",
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

_KEEP = {"SAVA": "SAVA", "IA": "IA", "AI": "AI", "FAQ": "FAQ", "COP": "COP", "PDF": "PDF",
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
