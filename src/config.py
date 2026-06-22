"""
Configuraciones generales del proyecto.

Importante:
- El grafo usa kilómetros como unidad base.
- Los precios de combustible son estimaciones editables.
- Para la entrega final, el grupo debe justificar o actualizar estos valores.
"""

PRECIOS_COMBUSTIBLE_CLP = {
    "93": 1300,
    "95": 1380,
    "97": 1480,
}

PERFILES_VEHICULO = {
    "Auto compacto": {
        "rendimiento_km_l": 16,
        "descripcion": "Vehículo pequeño de bajo consumo estimado.",
    },
    "Sedán": {
        "rendimiento_km_l": 13,
        "descripcion": "Vehículo de consumo medio estimado.",
    },
    "SUV": {
        "rendimiento_km_l": 10,
        "descripcion": "Vehículo de mayor consumo estimado.",
    },
    "Camioneta": {
        "rendimiento_km_l": 8,
        "descripcion": "Vehículo pesado de alto consumo estimado.",
    },
}

VELOCIDAD_CAMINATA_KM_H = 5
CALORIAS_POR_KM_CAMINANDO = 60
