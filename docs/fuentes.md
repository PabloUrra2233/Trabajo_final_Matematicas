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

| Origen    | Destino   | Distancia km | Fuente                                                                                       |
| --------- | --------- | -----------: | -------------------------------------------------------------------------------------------- |
| Paris     | Londres   |          459 | [Google Maps](https://www.google.com/maps/dir/Paris,+France/London,+United+Kingdom)          |
| Paris     | Bruselas  |          312 | [Google Maps](https://www.google.com/maps/dir/Paris,+France/Brussels,+Belgium)               |
| Paris     | Frankfurt |          572 | [Google Maps](https://www.google.com/maps/dir/Paris,+France/Frankfurt,+Germany)              |
| Paris     | Zurich    |          584 | [Google Maps](https://www.google.com/maps/dir/Paris,+France/Zurich,+Switzerland)             |
| Londres   | Bruselas  |          380 | [Google Maps](https://www.google.com/maps/dir/London,+United+Kingdom/Brussels,+Belgium)      |
| Londres   | Amsterdam |          555 | [Google Maps](https://www.google.com/maps/dir/London,+United+Kingdom/Amsterdam,+Netherlands) |
| Bruselas  | Amsterdam |          231 | [Google Maps](https://www.google.com/maps/dir/Brussels,+Belgium/Amsterdam,+Netherlands)      |
| Bruselas  | Frankfurt |          398 | [Google Maps](https://www.google.com/maps/dir/Brussels,+Belgium/Frankfurt,+Germany)          |
| Amsterdam | Berlin    |          656 | [Google Maps](https://www.google.com/maps/dir/Amsterdam,+Netherlands/Berlin,+Germany)        |
| Amsterdam | Frankfurt |          444 | [Google Maps](https://www.google.com/maps/dir/Amsterdam,+Netherlands/Frankfurt,+Germany)     |
| Frankfurt | Berlin    |          551 | [Google Maps](https://www.google.com/maps/dir/Frankfurt,+Germany/Berlin,+Germany)            |
| Frankfurt | Munich    |          393 | [Google Maps](https://www.google.com/maps/dir/Frankfurt,+Germany/Munich,+Germany)            |
| Frankfurt | Zurich    |          410 | [Google Maps](https://www.google.com/maps/dir/Frankfurt,+Germany/Zurich,+Switzerland)        |
| Berlin    | Praga     |          347 | [Google Maps](https://www.google.com/maps/dir/Berlin,+Germany/Prague,+Czechia)               |
| Praga     | Munich    |          383 | [Google Maps](https://www.google.com/maps/dir/Prague,+Czechia/Munich,+Germany)               |
| Praga     | Viena     |          335 | [Google Maps](https://www.google.com/maps/dir/Prague,+Czechia/Vienna,+Austria)               |
| Munich    | Zurich    |          316 | [Google Maps](https://www.google.com/maps/dir/Munich,+Germany/Zurich,+Switzerland)           |
| Munich    | Viena     |          402 | [Google Maps](https://www.google.com/maps/dir/Munich,+Germany/Vienna,+Austria)               |
| Zurich    | Milan     |          279 | [Google Maps](https://www.google.com/maps/dir/Zurich,+Switzerland/Milan,+Italy)              |
| Milan     | Venecia   |          270 | [Google Maps](https://www.google.com/maps/dir/Milan,+Italy/Venice,+Italy)                    |
| Budapest  | Viena     |          244 | [Google Maps](https://www.google.com/maps/dir/Budapest,+Hungary/Vienna,+Austria)             |
| Venecia   | Ljubljana |          243 | [Google Maps](https://www.google.com/maps/dir/Venice,+Italy/Ljubljana,+Slovenia)             |
| Ljubljana | Zagreb    |          147 | [Google Maps](https://www.google.com/maps/dir/Ljubljana,+Slovenia/Zagreb,+Croatia)           |
| Zagreb    | Budapest  |          345 | [Google Maps](https://www.google.com/maps/dir/Zagreb,+Croatia/Budapest,+Hungary)             |

## Nota

Las distancias pueden variar levemente según la ruta seleccionada, el punto exacto de inicio y destino dentro de cada ciudad y las condiciones de navegación. Para el proyecto se consideran valores aproximados y consistentes para construir el grafo ponderado.
