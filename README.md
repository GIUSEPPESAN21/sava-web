# SAVA Software · Página web

Página web de SAVA Software (software e IA para pymes), hecha en Streamlit, en español e inglés (`?lang=es` / `?lang=en`).

**Productos:** SAVA Stock (inventario y ventas), SAVA Flow (automatización e IA), SAVA Setup (instalación y capacitación) y SAVA Care (soporte mensual).

## Estructura

| Archivo | Para qué sirve |
|---|---|
| `app.py` | Diseño de la página y formulario de contacto |
| `content.py` | Todos los textos en español e inglés: edita aquí precios, productos y datos de contacto |
| `assets/style.css` | Colores, tipografía y diseño para celular |
| `assets/` | Logos, ícono y foto |
| `.streamlit/config.toml` | Tema de Streamlit |

## Probar en tu computador

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicar en Streamlit Community Cloud

1. Entra a https://share.streamlit.io con tu cuenta de GitHub.
2. Pulsa **Create app**, elige este repositorio, la rama `main` y el archivo `app.py`.
3. En **App URL** escribe un nombre corto, por ejemplo `savasoftware`, y pulsa **Deploy**.

## Base de datos de solicitudes

Cada envío del formulario (con autorización de datos) se guarda en la tabla `leads` del proyecto de Supabase **sava-web**: nombre, correo, celular, negocio, producto de interés, mensaje, idioma, si quiere novedades y un estado (`nuevo`, `contactado`, `diagnostico`, `demo`, `cliente`, `descartado`). La página solo puede **insertar**; para ver o editar las solicitudes entra a supabase.com → proyecto sava-web → Table Editor → `leads`.

## Aviso por correo con cada solicitud

En Streamlit Cloud → tu app → **Settings → Secrets**, pega esto con tus datos:

```toml
NOTIFY_EMAIL = "tu-correo-personal@gmail.com"   # a dónde llegan los avisos
SMTP_USER = "tu-correo-personal@gmail.com"      # cuenta Gmail que envía
SMTP_PASSWORD = "xxxx xxxx xxxx xxxx"           # contraseña de aplicación de Google
```

La contraseña de aplicación se crea en https://myaccount.google.com/apppasswords (requiere verificación en dos pasos). No uses tu contraseña normal.

## Redes sociales

Pega los enlaces en `content.py` (`TIKTOK`, `YOUTUBE`, `INSTAGRAM`). Los íconos aparecen solos en la barra superior, en «Nosotros» y en el pie de página.

---

## English

SAVA Software website built with Streamlit, in Spanish and English. Run locally with `pip install -r requirements.txt` and `streamlit run app.py`. To deploy, create an app at https://share.streamlit.io pointing to this repo, branch `main`, file `app.py`. Contact-form storage in Supabase is optional (see the secrets above).
