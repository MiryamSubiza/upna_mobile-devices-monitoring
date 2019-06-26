# Gráfico: Flujos de desplazamiento

### Descripción

Este tipo de gráfico muestra el recorrido de los dispositivos móviles que han sido detectados por más de un sensor.

Se generan dos gráficos:
- **Un salto:** Muestra los flujos de dispositivos detectados por dos sensores. Dados un sensor de partida y un rango de fechas introducidos como parámetros, se genera un gráfico que muestra la cantidad de dispositivos hallados en el sensor de inicio y, en un momento posterior, en un sensor diferente al de inicio.
- **Dos saltos:** Muestra los flujos de dispositivos detectados por hasta tres sensores. Dados un sensor de inicio y un rango de fechas introducidos como parámetros, se genera un gráfico indicando la cantidad de dispositivos móviles hallados en el sensor de inicio y, en momentos posteriores, en otros sensores diferentes. Se muestra un máximo de tres sensores por recorrido.

Cada flujo entre dos sensores (de izquierda a derecha) indica el número de dispositivos que se han detectado en un sensor determinado y, en un momento posterior, en otro sensor diferente. La anchura del flujo es proporcional al número de dispositivos que han realizado este recorrido. Al pasar por encima de un flujo se muestra la cantidad de dispositivos detectados.

Para generar estos gráficos se accede a la base de datos y se consultan los datos recogidos entre las fechas indicadas por parámetro. Se descartan los dispositivos móviles detectados por un único sensor y aquellos cuya primera aparición no sea en el sensor de inicio indicado como parámetro. Con los datos obtenidos se representa, a través del gráfico, el recorrido que han realizado dichos dispositivos.

### Ejecución

Se deben generar los gráficos a través del entorno <a href="https://jupyter.org/" target="_blank">Jupyter Notebook</a>.

Se solicitarán los siguientes parámetros de entrada:
- Fecha de inicio con formato AAAAMMDD.
- Fecha de fin con formato AAAAMMDD.
- Sensor de inicio.
- Credenciales de acceso a la base de datos.