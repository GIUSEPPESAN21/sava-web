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

## Guardar los mensajes del formulario (opcional)

Sin configuración, el formulario abre WhatsApp con el mensaje listo y no guarda datos. Para guardar también cada solicitud en la tabla `leads` de Supabase (la misma de la página anterior), agrega estos secrets en Streamlit Cloud (**Settings → Secrets**):

```toml
SUPABASE_URL = "https://TU-PROYECTO.supabase.co"
SUPABASE_ANON_KEY = "tu-clave-anon"
```

La tabla debe tener las columnas `name`, `email`, `company` y `message`, y una política que permita insertar con la clave anon.

---

## English

SAVA Software website built with Streamlit, in Spanish and English. Run locally with `pip install -r requirements.txt` and `streamlit run app.py`. To deploy, create an app at https://share.streamlit.io pointing to this repo, branch `main`, file `app.py`. Contact-form storage in Supabase is optional (see the secrets above).
