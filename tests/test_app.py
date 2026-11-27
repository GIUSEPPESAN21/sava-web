"""Pruebas automáticas de la página. Ejecutar con:  python -m pytest -q"""
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "app.py")


def run(lang="es"):
    at = AppTest.from_file(APP, default_timeout=30)
    at.query_params["lang"] = lang
    at.run()
    return at


def page(at):
    return "\n".join(m.value for m in at.markdown)


def test_carga_en_espanol_e_ingles():
    for lang in ("es", "en"):
        at = run(lang)
        assert not at.exception, at.exception
        assert len(at.text_input) == 0, "ya no hay formulario: el contacto es por WhatsApp e Instagram"


def test_sin_seccion_nosotros():
    html = page(run("es"))
    assert 'id="nosotros"' not in html
    assert "joseph.jpg" not in html and "CEO y fundador" not in html


def test_botones_directos_a_whatsapp_e_instagram():
    html = page(run("es"))
    assert 'id="contacto"' in html
    assert "https://wa.me/573222074527?text=" in html
    assert "diagn%C3%B3stico%20gratis" in html, "el mensaje de WhatsApp debe ir escrito"
    assert "https://ig.me/m/savasoftware" in html


def test_precios_en_pesos_colombianos():
    html = page(run("es"))
    for precio in ("$950.000", "$4.000.000", "$800.000", "$400.000", "$85.000", "$475.000",
                   "$1.970.000", "$1.820.000"):
        assert precio in html, precio
    assert "COP" in html
    en = page(run("en"))
    assert "$950,000" in en and "$4,000,000" in en


def test_cotizador_en_la_pagina():
    html = page(run("es"))
    assert 'id="cotizador"' in html and "data-calc=" in html
    assert 'data-k="license"' in html
