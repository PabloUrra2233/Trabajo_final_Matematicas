# Informe técnico

## Proyecto Final Matemática Discreta

### Ruta óptima entre ciudades mediante grafos ponderados

**Integrantes:** Pablo Urra y Bernardo Sandoval
**Repositorio:** https://github.com/PabloUrra2233/Trabajo_final_Matematicas

---

## 1. Introducción

Nuestro proyecto tiene como meta modelar una red de ciudades usando un grafo ponderado y desarrollando una aplicación en Python que nos permita calcular la ruta óptima entre una ciudad de origen y una ciudad de destino.

Para el desarrollo del proyecto se seleccionaron 15 ciudades europeas no chilenas. Cada ciudad esta representada como un vértice del grafo y las conexiones entre ciudades fueron representadas como aristas. El peso de cada arista corresponde a una distancia aproximada en kilómetros, manteniendo un criterio único de ponderación durante todo el proyecto.

Nuestra aplicación nos permitirá seleccionar una ciudad cualquiera y una ciudad de destino usando una interfaz gráfica, calcular el camino mínimo entre ambas, mostrar la secuencia de ciudades que componen la ruta, presentar el costo total del recorrido y visualizar gráficamente el grafo con la ruta óptima resaltada. 

---

## 2. Modelamiento matemático

El problema se representa mediante un grafo ponderado no dirigido:

[
G = (V, E, w)
]

donde:

* (V) corresponde al conjunto de ciudades seleccionadas.
* (E) corresponde al conjunto de conexiones entre ciudades.
* (w : E \rightarrow \mathbb{R}^{+}) es una función que asigna a cada arista un peso positivo.
* El peso (w(u,v)) representa la distancia aproximada en kilómetros entre las ciudades (u) y (v).

### Conjunto de vértices

El conjunto de vértices utilizado es:

[
V = {
Paris, Londres, Bruselas, Amsterdam, Frankfurt, Berlin, Praga, Munich, Zurich, Milan, Venecia, Ljubljana, Zagreb, Budapest, Viena
}
]

Cada elemento del conjunto representa una ciudad del grafo.

### Conjunto de aristas

El conjunto (E) está formado por conexiones entre pares de ciudades. Algunos ejemplos de aristas son:

[
(Paris, Bruselas), (Bruselas, Amsterdam), (Berlin, Praga), (Milan, Venecia)
]

Cada arista representa una conexión entre dos ciudades y posee un peso asociado en kilómetros. El archivo `data/conexiones.csv` contiene las conexiones utilizadas por la aplicación.

### Función de peso

La función de peso se define como:

[
w(u,v) = \text{distancia en kilómetros entre las ciudades } u \text{ y } v
]

Por ejemplo:

[
w(Paris, Bruselas) = 312
]

Esto significa que la distancia aproximada entre Paris y Bruselas es de 312 kilómetros.

### Camino y ruta óptima

Un camino entre una ciudad de origen (s) y una ciudad de destino (t) se representa como:

[
P = (s = v_0, v_1, v_2, ..., v_k = t)
]

El costo total de un camino lo calculamos sumando los pesos de sus aristas:

[
C(P) = \sum_{i=0}^{k-1} w(v_i, v_{i+1})
]

La ruta óptima corresponde al camino de menor costo total:

[
P^* = \arg\min_P C(P)
]

En este proyecto, la ruta óptima corresponde al recorrido con menor distancia total en kilómetros.

---

## 3. Propiedades del grafo

El grafo utilizado es:

* **No dirigido**, porque las conexiones entre ciudades pueden recorrerse en ambos sentidos.
* **Ponderado**, porque cada arista posee un peso asociado.
* **Conexo**, porque existe al menos un camino entre cualquier par de ciudades.
* **Finito**, porque contiene una cantidad limitada de vértices y aristas.

Una proposición lógica asociada al grafo es:

[
\forall u,v \in V,\ \exists P(u,v)
]

Esto significa que para todo par de ciudades (u) y (v) pertenecientes al conjunto de vértices, existe al menos un camino que las conecta.

Otra condición importante es:

[
\forall (u,v) \in E,\ w(u,v) > 0
]

Esto significa que todos los pesos de las aristas son positivos, esta condición es necesaria para poder aplicar el algoritmo de Dijkstra.

---

## 4. Algoritmo utilizado

Para calcular la ruta óptima implemente el algoritmo de Dijkstra. Este algoritmo permite encontrar el camino mínimo desde un nodo origen hacia los demás nodos de un grafo ponderado con pesos no negativos.

Elegimos Dijkstra porque en este proyecto todos los pesos representan distancias en kilómetros, por lo tanto nos quedan valores positivos. Esto hace que el algoritmo sea adecuado para resolver el problema planteado.

### Funcionamiento general de Dijkstra

El algoritmo funciona de la siguiente manera:

1. Se asigna distancia 0 a la ciudad de origen.
2. Se asigna distancia infinita al resto de ciudades.
3. Se utiliza una cola de prioridad para seleccionar la ciudad no visitada con menor distancia acumulada.
4. Se revisan sus vecinos y se actualizan las distancias si se encuentra un camino más corto.
5. Se repite el proceso hasta llegar a la ciudad de destino.
6. Se reconstruye la ruta óptima utilizando los nodos anteriores guardados durante el proceso.

### Pseudocódigo

```text
Dijkstra(grafo, origen, destino):
    asignar distancia 0 al origen
    asignar infinito a las demás ciudades
    crear cola de prioridad con el origen

    mientras la cola no esté vacía:
        extraer la ciudad con menor distancia acumulada

        si la ciudad actual es el destino:
            terminar búsqueda

        para cada vecino de la ciudad actual:
            calcular nueva distancia
            si la nueva distancia es menor:
                actualizar distancia
                guardar ciudad anterior
                agregar vecino a la cola

    reconstruir y retornar la ruta óptima
```

### Comparación con Bellman-Ford

Una alternativa posible es el algoritmo de Bellman-Ford. Este también permite encontrar caminos mínimos y tiene la ventaja de aceptar pesos negativos. Sin embargo, en este proyecto los pesos corresponden a distancias, por lo que siempre son positivos.

Por esta razón, Dijkstra resulta más adecuado, ya que es más eficiente para grafos con pesos positivos y permite resolver correctamente el problema de ruta óptima entre ciudades.

---

## 5. Implementación de la aplicación

La aplicación fue desarrollada en Python utilizando una estructura modular. Los archivos principales son:

* `app.py`: contiene la interfaz gráfica.
* `graph_manager.py`: carga las ciudades y conexiones desde archivos CSV y construye el grafo.
* `shortest_path.py`: implementa el algoritmo de Dijkstra.
* `visualization.py`: genera la visualización del grafo y resalta la ruta óptima.
* `converters.py`: contiene funciones de conversión de kilómetros a metros y millas.
* `transport_modes.py`: calcula estimaciones adicionales para vehículo y caminata.
* `config.py`: almacena valores configurables, como precios de combustible y rendimiento estimado.

La información del grafo se almacena en archivos CSV:

* `data/ciudades.csv`: contiene las ciudades, país, coordenadas y posiciones para el mapa.
* `data/conexiones.csv`: contiene las conexiones, distancia en kilómetros y fuente o criterio utilizado.

La librería NetworkX se utiliza para representar el grafo computacionalmente. Matplotlib se usa para dibujar el grafo y CustomTkinter para construir la interfaz gráfica.

---

## 6. Interfaz gráfica

La interfaz permite al usuario:

* Seleccionar ciudad de origen.
* Seleccionar ciudad de destino.
* Elegir modo de transporte.
* Calcular la ruta óptima.
* Ver la distancia total.
* Visualizar el grafo completo.
* Visualizar la ruta óptima resaltada.

Cuando el usuario selecciona origen y destino, la aplicación ejecuta el algoritmo de Dijkstra y muestra el resultado. Además, se despliega una visualización del grafo donde la ruta óptima aparece diferenciada del resto de conexiones.

---

## 7. Resultados y pruebas

A continuación se presentan tres pruebas de funcionamiento de la aplicación.

### Prueba 1

* **Origen:** Paris
* **Destino:** Berlin
* **Modo:** Vehículo
* **Perfil:** Sedán
* **Octanaje:** 95

**Resultado esperado:**
La aplicación debe mostrar una ruta óptima entre Paris y Berlin, la distancia total en kilómetros, la estimación de litros de combustible, el costo aproximado y la visualización del grafo con la ruta resaltada.

---

### Prueba 2

* **Origen:** Londres
* **Destino:** Viena
* **Modo:** Vehículo
* **Perfil:** Auto compacto
* **Octanaje:** 93

**Resultado esperado:**
La aplicación debe encontrar una ruta que conecte Londres con Viena mediante ciudades intermedias. También debe mostrar el costo total del recorrido y modificar la estimación según el rendimiento del vehículo seleccionado.

---

### Prueba 3

* **Origen:** Milan
* **Destino:** Budapest
* **Modo:** Caminando

**Resultado esperado:**
La aplicación debe mostrar la ruta óptima, la distancia total, el tiempo estimado caminando y las calorías aproximadas asociadas al recorrido.

---

## 8. Conclusión

El proyecto permitió aplicar conceptos de matemática discreta, especialmente teoría de grafos, caminos, grafos ponderados, conectividad y algoritmos de camino mínimo. Mediante el uso de un grafo ponderado fue posible representar una red de ciudades y resolver el problema de encontrar la ruta de menor costo entre dos puntos.

El algoritmo de Dijkstra resultó adecuado para este caso, ya que todos los pesos utilizados son positivos. Además, la implementación modular permitió separar la carga de datos, el cálculo de rutas, la visualización y la interfaz gráfica.

Una dificultad importante fue organizar los datos de las ciudades y mantener un criterio consistente para los pesos del grafo. Como mejora futura, se podrían incorporar fuentes verificadas directamente mediante enlaces, permitir elegir distintos criterios de ponderación y mejorar la visualización del mapa.

En conclusión, la aplicación cumple con el objetivo de modelar una red de ciudades como grafo ponderado y calcular rutas óptimas mediante un algoritmo de camino mínimo.

