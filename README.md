# Proyecto Final Matemática Discreta

## Ruta Óptima entre Ciudades mediante Grafos Ponderados

### Integrantes

* Pablo Urra
* Bernardo Sandoval 

---

## Descripción del proyecto

Este proyecto consiste en modelar una red de ciudades mediante un grafo ponderado y desarrollar una aplicación en Python que permita calcular la ruta óptima entre una ciudad de origen y una ciudad de destino.

Las ciudades se representan como vértices, las conexiones entre ciudades como aristas y la distancia en kilómetros como peso de cada arista.

La aplicación permite:

* Seleccionar una ciudad de origen.
* Seleccionar una ciudad de destino.
* Calcular la ruta óptima entre ambas ciudades.
* Mostrar la secuencia de ciudades que componen el recorrido.
* Mostrar el costo total de la ruta en kilómetros.
* Visualizar el grafo y resaltar la ruta óptima.
* Mostrar estimaciones adicionales según modo de transporte.

---

## Tecnologías utilizadas

* Python
* NetworkX
* Matplotlib
* CustomTkinter
* CSV

---

## Estructura del proyecto

```text
Proyecto-Mate/
│
├── assets/
│   ├── .gitkeep
│   └── mapa_europa.png
│
├── data/
│   ├── ciudades.csv
│   └── conexiones.csv
│
├── docs/
│   ├── fuentes.md
│   ├── guia_commits.md
│   ├── informe.md
│   ├── modelamiento.md
│   └── pruebas.md
│
├── src/
│   ├── app.py
│   ├── config.py
│   ├── converters.py
│   ├── graph_manager.py
│   ├── shortest_path.py
│   ├── transport_modes.py
│   └── visualization.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Distribución de responsabilidades

### Pablo Urra

Responsable de la arquitectura lógica, modelamiento del grafo, algoritmo de camino mínimo, datos y visualización.

Archivos principales:

* `src/graph_manager.py`
* `src/shortest_path.py`
* `src/visualization.py`
* `src/converters.py`
* `src/transport_modes.py`
* `data/ciudades.csv`
* `data/conexiones.csv`
* `docs/modelamiento.md`

Tareas:

* Definir el grafo ponderado.
* Definir los conjuntos `V`, `E` y la función de peso `w`.
* Implementar la carga del grafo desde archivos CSV.
* Implementar el algoritmo de Dijkstra.
* Verificar que el grafo sea conexo.
* Implementar la visualización del grafo.
* Resaltar la ruta óptima calculada.
* Agregar conversiones y estimaciones complementarias.

---

### Bernardo Sandoval 

Responsable de interfaz gráfica, documentación, pruebas, fuentes y preparación de la entrega.

Archivos principales:

* `src/app.py`
* `src/config.py`
* `docs/fuentes.md`
* `docs/pruebas.md`
* `docs/informe.md`
* `docs/guia_commits.md`
* `README.md`
* `requirements.txt`

Tareas:

* Implementar o ajustar la interfaz gráfica con CustomTkinter.
* Permitir selección de ciudad de origen y ciudad de destino.
* Mostrar la ruta óptima obtenida.
* Mostrar el costo total del recorrido.
* Documentar las fuentes utilizadas para las distancias.
* Registrar pruebas de funcionamiento.
* Mantener instrucciones claras de instalación y ejecución.
* Apoyar la preparación del informe técnico y la presentación final.

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/PabloUrra2233/Trabajo_final_Matematicas.git
```

Entrar al directorio del proyecto:

```bash
cd Trabajo_final_Matematicas
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python src/app.py
```

---

## Flujo de trabajo en GitHub

Cada integrante debe trabajar en una rama propia y abrir un Pull Request hacia `main`.

Ramas sugeridas:

```text
feature/algoritmo-modelamiento
feature/interfaz-documentacion
feature/integracion-final
```

Reglas de trabajo:

* No trabajar directamente sobre `main` salvo para cambios menores acordados.
* Realizar commits descriptivos.
* Abrir Pull Requests para integrar cambios.
* Revisar que la aplicación ejecute antes de fusionar cambios.
* Mantener actualizado el README y la documentación.

---

## Estado del proyecto

* [x] Estructura base del repositorio
* [x] Carga de ciudades desde CSV
* [x] Carga de conexiones desde CSV
* [x] Implementación de Dijkstra
* [x] Interfaz gráfica
* [x] Visualización del grafo
* [x] Ruta óptima resaltada
* [x] Documentación de fuentes
* [x] Pruebas de funcionamiento
* [x] Informe técnico
* [ ] Presentación final

---

## Licencia

Proyecto académico desarrollado para la asignatura de Matemática Discreta.
