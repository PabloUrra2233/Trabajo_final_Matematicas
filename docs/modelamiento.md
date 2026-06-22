# Modelamiento matemático

## Grafo ponderado

El problema se representa mediante un grafo ponderado no dirigido:

\[
G = (V, E, w)
\]

donde:

- \(V\) es el conjunto de ciudades.
- \(E\) es el conjunto de conexiones reales entre ciudades.
- \(w : E \rightarrow \mathbb{R}^{+}\) asigna a cada conexión una distancia positiva en kilómetros.

## Conjunto de vértices

\[
V = \{
Paris, Londres, Bruselas, Amsterdam, Berlin, Praga, Viena, Budapest,
Zagreb, Ljubljana, Venecia, Milan, Zurich, Munich, Frankfurt
\}
\]

## Conjunto de aristas

Cada arista representa una conexión terrestre o vial entre dos ciudades. Por ejemplo:

\[
(Paris, Bruselas), (Bruselas, Amsterdam), (Berlin, Praga)
\]

El archivo `data/conexiones.csv` contiene el conjunto completo de aristas.

## Función de peso

La función de peso está definida por:

\[
w(u, v) = \text{distancia en kilómetros entre las ciudades } u \text{ y } v
\]

Por ejemplo:

\[
w(Paris, Bruselas) = 312
\]

## Camino

Un camino desde una ciudad de origen \(s\) hasta una ciudad de destino \(t\) se representa como:

\[
P = (s = v_0, v_1, v_2, ..., v_k = t)
\]

El costo total del camino es:

\[
C(P) = \sum_{i=0}^{k-1} w(v_i, v_{i+1})
\]

## Ruta óptima

La ruta óptima corresponde al camino de menor costo:

\[
P^* = \arg\min_{P} C(P)
\]

## Algoritmo utilizado

Se utiliza el algoritmo de Dijkstra porque todos los pesos del grafo son positivos. Esto lo hace adecuado para encontrar el camino mínimo entre una ciudad de origen y una ciudad de destino.

## Comparación con Bellman-Ford

Bellman-Ford también permite encontrar caminos mínimos y soporta pesos negativos. Sin embargo, en este proyecto las distancias son siempre positivas, por lo que Dijkstra resulta más adecuado y eficiente para este caso.
