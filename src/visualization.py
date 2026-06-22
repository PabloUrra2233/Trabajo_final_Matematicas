# src/visualization.py

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from graph_manager import obtener_posiciones_mapa


RUTA_BASE = Path(__file__).resolve().parent.parent
RUTA_MAPA = RUTA_BASE / "assets" / "mapa_europa.png"


def dibujar_grafo(grafo, ruta_optima=None, tipo_visualizacion="mapa"):
    if tipo_visualizacion == "mapa":
        posiciones = obtener_posiciones_mapa(grafo)
    else:
        posiciones = nx.spring_layout(grafo, seed=12)

    fig, ax = plt.subplots(figsize=(14, 8))

    if tipo_visualizacion == "mapa":
        dibujar_mapa_fondo(ax)

    # Dibujar aristas normales
    nx.draw_networkx_edges(
        grafo,
        posiciones,
        edge_color="gray",
        width=1.2,
        alpha=0.8,
        ax=ax,
    )

    # Dibujar ruta óptima
    if ruta_optima and len(ruta_optima) > 1:
        aristas_ruta = list(zip(ruta_optima, ruta_optima[1:]))

        nx.draw_networkx_edges(
            grafo,
            posiciones,
            edgelist=aristas_ruta,
            width=4,
            edge_color="black",
            ax=ax,
        )

    # Dibujar nodos
    nx.draw_networkx_nodes(
        grafo,
        posiciones,
        node_size=970,
        node_color="#1f77b4",
        edgecolors="white",
        linewidths=1.5,
        ax=ax,
    )

    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(
        grafo,
        posiciones,
        font_size=7,
        font_color="white",
        ax=ax,
    )

    # Etiquetas de peso en aristas
    etiquetas = nx.get_edge_attributes(grafo, "weight")
    etiquetas = {arista: f"{peso:.0f}" for arista, peso in etiquetas.items()}

    nx.draw_networkx_edge_labels(
        grafo,
        posiciones,
        edge_labels=etiquetas,
        font_size=6,
        ax=ax,
        bbox={
            "boxstyle": "round,pad=0.15",
            "facecolor": "white",
            "edgecolor": "none",
            "alpha": 0.85,
        },
    )

    if tipo_visualizacion == "mapa":
        ax.set_title("Grafo de ciudades sobre mapa referencial")

        # Zoom automático según las posiciones de las ciudades
        xs = [pos[0] for pos in posiciones.values()]
        ys = [pos[1] for pos in posiciones.values()]

        margen_x = 10
        margen_y = 10

        ax.set_xlim(min(xs) - margen_x, max(xs) + margen_x)
        ax.set_ylim(min(ys) - margen_y, max(ys) + margen_y)

        ax.axis("off")
    else:
        ax.set_title("Grafo abstracto de ciudades")
        ax.axis("off")

    plt.tight_layout()
    plt.show()


def dibujar_mapa_fondo(ax):
    if not RUTA_MAPA.exists():
        print(f"No se encontró la imagen de mapa: {RUTA_MAPA}")
        return

    imagen = plt.imread(RUTA_MAPA)

    ax.imshow(
        imagen,
        extent=[0, 100, 0, 100],
        aspect="auto",
        alpha=0.85,
        zorder=0,
    )