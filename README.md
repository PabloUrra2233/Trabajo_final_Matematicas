# Proyecto Final Matemática Discreta

## Ruta Óptima entre Ciudades mediante Grafos Ponderados

Este repositorio contiene una aplicación en Python que modela una red de ciudades como un grafo ponderado y calcula la ruta óptima entre una ciudad de origen y una ciudad de destino.

> Esta versión es una maqueta funcional de referencia. Para la entrega final, el grupo debe verificar distancias, documentar fuentes y adaptar el contenido.

---

## Tecnologías utilizadas

- Python
- NetworkX
- Matplotlib
- CustomTkinter

---

## Idea principal

El grafo utiliza **kilómetros** como unidad base para todas las aristas.

Después de calcular la ruta óptima, la aplicación permite mostrar estimaciones derivadas:

- Distancia total en kilómetros.
- Distancia total en metros.
- Distancia total en millas.
- Costo estimado en pesos chilenos según vehículo y octanaje.
- Tiempo y calorías estimadas si el recorrido se hiciera caminando.

El algoritmo de camino mínimo no cambia según estas conversiones. La ruta óptima se calcula usando siempre distancia en kilómetros.

---

## Estructura

```text
Proyecto-Mate/
│
├── data/
│   └── conexiones.csv
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
├── docs/
│   ├── fuentes.md
│   ├── modelamiento.md
│   ├── pruebas.md
│   └── guia_commits.md
│
├── requirements.txt
└── README.md
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/PabloUrra2233/Proyecto-Mate.git
cd Proyecto-Mate
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

## Distribución sugerida del trabajo

### Pablo Urra
Arquitectura, modelamiento matemático, algoritmo de Dijkstra e integración general.

### Compañero 2
Construcción y validación del dataset de ciudades, conexiones y fuentes.

### Compañero 3
Interfaz gráfica con CustomTkinter.

### Compañero 4
Visualización del grafo, documentación, informe y presentación.

---

## Flujo de trabajo sugerido

Cada integrante debe trabajar en una rama propia y abrir Pull Requests hacia `main`.

Ejemplos de ramas:

```text
feature/algoritmo
feature/datos
feature/interfaz
feature/visualizacion
feature/documentacion
```

Los commits deben ser pequeños, descriptivos y asociados a cambios concretos.

---

## Estado

- [x] Estructura modular
- [x] Carga de grafo desde CSV
- [x] Implementación manual de Dijkstra
- [x] Interfaz con CustomTkinter
- [x] Visualización con Matplotlib y NetworkX
- [x] Conversión a costo de combustible
- [x] Modo caminata con tiempo y calorías
- [ ] Verificación final de fuentes reales
- [ ] Informe técnico definitivo
- [ ] Presentación final
