# SAVA Software · Página web

Página web de SAVA Software (software e IA para pymes), hecha en Streamlit, en español e inglés (`?lang=es` / `?lang=en`).

**Productos:** SAVA Stock (inventario y ventas), SAVA Flow (automatización e IA), SAVA Setup (instalación y capacitación) y SAVA Care (soporte mensual).

## Estructura

| Archivo | Para qué sirve |
|---|---|
| `app.py` | Diseño de la página (secciones, precios, cotizador y botones de contacto) |
| `content.py` | Todos los textos en español e inglés: edita aquí precios (`PRICES`), productos, preguntas y datos de contacto |
| `assets/style.css` | Colores de marca, tipografía (Inter), animaciones y diseño para celular |
| `assets/fx.js` | Animaciones al bajar, contadores y cotizador en vivo (si se bloquea, la página se ve completa igual) |
| `assets/` | Logos e ícono |

## Contacto

La sección **Agenda tu diagnóstico gratis** lleva directo a WhatsApp (con el mensaje ya escrito) y al chat de Instagram de @savasoftware (`INSTAGRAM_DM` en `content.py`). Cada plan de precios y el cotizador también abren WhatsApp con el plan elegido.

## Probar en tu computador

Pruebas automáticas (carga de la página, precios y botones de contacto): `pip install pytest` y luego `python -m pytest -q`.


```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicar en Streamlit Community Cloud

1. Entra a https://share.streamlit.io con tu cuenta de GitHub.
2. Pulsa **Create app**, elige este repositorio, la rama `main` y el archivo `app.py`.
3. En **App URL** escribe un nombre corto, por ejemplo `savasoftware`, y pulsa **Deploy**.

## Redes sociales

Pega los enlaces en `content.py` (`TIKTOK`, `YOUTUBE`, `INSTAGRAM`). Los íconos aparecen solos en la barra superior y en el pie de página.

---

## English

SAVA Software website built with Streamlit, in Spanish and English. Run locally with `pip install -r requirements.txt` and `streamlit run app.py`. To deploy, create an app at https://share.streamlit.io pointing to this repo, branch `main`, file `app.py`. Contact goes straight to WhatsApp and Instagram.
