# src/graph_manager.py

import csv
from pathlib import Path

import networkx as nx


def cargar_ciudades(ruta_ciudades):
    ciudades = {}

    with Path(ruta_ciudades).open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            ciudad = fila["ciudad"].strip()

            ciudades[ciudad] = {
                "pais": fila["pais"].strip(),
                "latitud": float(fila["latitud"]),
                "longitud": float(fila["longitud"]),
                "x_mapa": float(fila["x_mapa"]),
                "y_mapa": float(fila["y_mapa"]),
            }

    return ciudades


def cargar_grafo(ruta_ciudades, ruta_conexiones):
    ciudades = cargar_ciudades(ruta_ciudades)
    grafo = nx.Graph()

    for ciudad, datos in ciudades.items():
        grafo.add_node(
            ciudad,
            pais=datos["pais"],
            latitud=datos["latitud"],
            longitud=datos["longitud"],
            x_mapa=datos["x_mapa"],
            y_mapa=datos["y_mapa"],
        )

    with Path(ruta_conexiones).open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            origen = fila["origen"].strip()
            destino = fila["destino"].strip()
            distancia = float(fila["distancia_km"])

            if origen not in ciudades:
                raise ValueError(f"La ciudad de origen no existe en ciudades.csv: {origen}")

            if destino not in ciudades:
                raise ValueError(f"La ciudad de destino no existe en ciudades.csv: {destino}")

            if distancia <= 0:
                raise ValueError("La distancia debe ser mayor que cero.")

            grafo.add_edge(
                origen,
                destino,
                weight=distancia,
                fuente=fila["fuente"].strip(),
            )

    return grafo


def obtener_ciudades(grafo):
    return sorted(grafo.nodes())


def obtener_posiciones_mapa(grafo):
    posiciones = {}

    for ciudad, datos in grafo.nodes(data=True):
        posiciones[ciudad] = (
            datos["x_mapa"],
            datos["y_mapa"],
        )

    return posiciones


def obtener_resumen_grafo(grafo):
    return {
        "cantidad_ciudades": grafo.number_of_nodes(),
        "cantidad_conexiones": grafo.number_of_edges(),
        "es_conexo": nx.is_connected(grafo),
    }


def validar_requisitos_basicos(grafo):
    errores = []

    if grafo.number_of_nodes() != 15:
        errores.append("El grafo debe tener exactamente 15 ciudades.")

    if grafo.number_of_edges() < 20:
        errores.append("El grafo debe tener al menos 20 conexiones.")

    if not nx.is_connected(grafo):
        errores.append("El grafo debe ser conexo.")

    return errores