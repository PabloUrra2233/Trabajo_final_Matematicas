# Fuentes de datos

Las distancias utilizadas en este proyecto corresponden a distancias terrestres aproximadas entre ciudades europeas. Estas distancias se usan como pesos del grafo ponderado, manteniendo un criterio único: kilómetros por ruta en vehículo.

## Criterio utilizado

- Unidad de medida: kilómetros.
- Tipo de peso: distancia terrestre aproximada.
- Tipo de ruta: ruta en vehículo entre ciudades.
- Fuente principal: Google Maps.
- Fecha de consulta: 22 de junio de 2026.

## Justificación del criterio

Se decidió utilizar distancia terrestre aproximada en kilómetros porque permite representar el problema como un grafo ponderado con pesos positivos. Esto es adecuado para aplicar el algoritmo de Dijkstra, ya que todos los pesos del grafo son mayores que cero.

No se mezclaron criterios como distancia aérea, precio de pasajes, tiempo de viaje o costo de combustible. Todas las conexiones utilizan el mismo tipo de peso para mantener la consistencia del modelo matemático.

## Conexiones verificadas

| Origen | Destino | Distancia km | Fuente |
|---|---|---:|---|
| Paris | Londres | 459 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Paris | Bruselas | 312 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Paris | Frankfurt | 572 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Paris | Zurich | 584 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Londres | Bruselas | 380 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Londres | Amsterdam | 555 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Bruselas | Amsterdam | 231 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Bruselas | Frankfurt | 398 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Amsterdam | Berlin | 656 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Amsterdam | Frankfurt | 444 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Frankfurt | Berlin | 551 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Frankfurt | Munich | 393 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Frankfurt | Zurich | 410 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Berlin | Praga | 347 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Praga | Munich | 383 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Praga | Viena | 335 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Munich | Zurich | 316 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Munich | Viena | 402 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Zurich | Milan | 279 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Milan | Venecia | 270 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Budapest | Viena | 244 | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Venecia | Ljubljana | ___ | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Ljubljana | Zagreb | ___ | Google Maps, ruta en vehículo, consultado el 22-06-2026 |
| Zagreb | Budapest | ___ | Google Maps, ruta en vehículo, consultado el 22-06-2026 |

## Nota

Las distancias pueden variar levemente según la ruta seleccionada, el punto exacto de inicio y destino dentro de cada ciudad y las condiciones de navegación. Para el proyecto se consideran valores aproximados y consistentes para construir el grafo ponderado.
