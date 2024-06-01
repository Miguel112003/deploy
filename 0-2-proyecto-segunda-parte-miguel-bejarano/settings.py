from datetime import date

# Archivo para el manejo de Constantes

RUTA_LOGO = "./static/logo_toxicomicos.png"
RUTA_EVENTOS = "./data/eventos.json"
RUTA_BOLETAS = "./data/boletas.json"
RUTA_ARTISTAS = "./data/artistas.json"
RUTA_CONTADORES = './data/contadores.json'
RUTA_PATROCINADORES = './data/patrocinadores.json'
RUTA_PDF_GENERADO = './boletas_generadas/Boleta_generada.pdf'
RUTA_QR = './static/Qr_verificacion.png'

FECHA_ACTUAL = date.today().strftime("%d/%m/%y")

CENTRADO_CSS_TEXTO = """
    <style>
        .centrado-texto {
            text-align: center;
        }
    </style>
"""
CENTRADO_CSS_IMAGEN = """
    <style>
    .centrado {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    </style>
"""
