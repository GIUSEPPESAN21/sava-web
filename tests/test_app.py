"""Pruebas automáticas de la página. Ejecutar con:  python -m pytest -q"""
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "app.py")


def run(lang="es"):
    at = AppTest.from_file(APP, default_timeout=30)
    at.query_params["lang"] = lang
    at.run()
    return at


def campo(at, etiqueta):
    return next(w for w in at.text_input if w.label.lower().startswith(etiqueta.lower()))


def test_carga_en_espanol_e_ingles():
    for lang in ("es", "en"):
        at = run(lang)
        assert not at.exception, at.exception
        assert len(at.text_input) == 4 and len(at.checkbox) == 2


def test_formulario_vacio_muestra_errores_claros():
    at = run("es")
    at.button[0].click().run()
    texto = " ".join(e.value for e in at.error)
    assert "nombre" in texto.lower()
    assert "whatsapp o tu correo" in texto.lower()
    assert "autorización" in texto.lower()


def test_correo_invalido():
    at = run("es")
    campo(at, "Nombre").input("Prueba")
    campo(at, "Correo").input("correo-malo")
    at.checkbox[0].check()
    at.button[0].click().run()
    assert any("correo" in e.value.lower() for e in at.error)


def test_formulario_completo_se_envia():
    at = run("es")
    campo(at, "Nombre").input("Prueba")
    campo(at, "WhatsApp").input("3001234567")
    at.checkbox[0].check()
    at.button[0].click().run()
    assert not at.error
    assert at.success, "debería mostrar el mensaje de confirmación"
