"""
Funciones de conversión.

El algoritmo calcula siempre la ruta usando kilómetros.
Estas funciones transforman la distancia final a otros valores derivados.
"""


def kilometros_a_metros(distancia_km: float) -> float:
    return distancia_km * 1000


def kilometros_a_millas(distancia_km: float) -> float:
    return distancia_km * 0.621371


def formatear_clp(valor: float) -> str:
    return f"${valor:,.0f} CLP".replace(",", ".")
