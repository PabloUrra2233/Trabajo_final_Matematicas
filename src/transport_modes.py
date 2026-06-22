"""
Estimaciones según modo de transporte.

Estas funciones NO modifican la ruta óptima.
Solo interpretan la distancia total calculada por Dijkstra.
"""

from config import (
    CALORIAS_POR_KM_CAMINANDO,
    PRECIOS_COMBUSTIBLE_CLP,
    VELOCIDAD_CAMINATA_KM_H,
)


def estimar_auto(distancia_km: float, rendimiento_km_l: float, octanaje: str) -> dict:
    if rendimiento_km_l <= 0:
        raise ValueError("El rendimiento debe ser mayor que cero.")

    if octanaje not in PRECIOS_COMBUSTIBLE_CLP:
        raise ValueError(f"Octanaje no válido: {octanaje}")

    precio_litro = PRECIOS_COMBUSTIBLE_CLP[octanaje]
    litros = distancia_km / rendimiento_km_l
    costo = litros * precio_litro

    return {
        "litros": litros,
        "precio_litro": precio_litro,
        "costo": costo,
    }


def estimar_caminata(distancia_km: float) -> dict:
    horas = distancia_km / VELOCIDAD_CAMINATA_KM_H
    calorias = distancia_km * CALORIAS_POR_KM_CAMINANDO

    return {
        "horas": horas,
        "calorias": calorias,
    }
