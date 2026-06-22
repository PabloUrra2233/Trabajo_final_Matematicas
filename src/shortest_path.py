"""
Algoritmo de camino mínimo.

Se implementa Dijkstra manualmente para que el grupo pueda explicar el algoritmo
sin depender completamente de una función ya hecha de NetworkX.
"""

import heapq
import math

import networkx as nx


def dijkstra(grafo: nx.Graph, origen: str, destino: str) -> tuple[list[str], float]:
    if origen not in grafo:
        raise ValueError(f"La ciudad de origen no existe en el grafo: {origen}")

    if destino not in grafo:
        raise ValueError(f"La ciudad de destino no existe en el grafo: {destino}")

    distancias = {nodo: math.inf for nodo in grafo.nodes}
    anteriores = {nodo: None for nodo in grafo.nodes}
    visitados = set()

    distancias[origen] = 0
    cola_prioridad = [(0, origen)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        if nodo_actual == destino:
            break

        for vecino in grafo.neighbors(nodo_actual):
            peso = grafo[nodo_actual][vecino]["weight"]
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    if math.isinf(distancias[destino]):
        raise nx.NetworkXNoPath(f"No existe ruta entre {origen} y {destino}")

    ruta = reconstruir_ruta(anteriores, origen, destino)
    return ruta, distancias[destino]


def reconstruir_ruta(anteriores: dict, origen: str, destino: str) -> list[str]:
    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)

        if actual == origen:
            break

        actual = anteriores[actual]

    ruta.reverse()

    if not ruta or ruta[0] != origen:
        raise nx.NetworkXNoPath(f"No se pudo reconstruir una ruta desde {origen} hasta {destino}")

    return ruta
