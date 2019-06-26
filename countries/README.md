# Gráfico: Móviles por países

### Descripción

Este gráfico trata de representar la cantidad de dispositivos móviles diferentes que se han detectado de cada país.

En el gráfico se muestra un mapa del mundo. Si se detectan dispositivos móviles de un país se añade una burbuja encima de dicho país, cuyo tamaño es proporcional a la cantidad de dispositivos móviles encontrados. En caso de no haber detectado ningún dispositivo móvil de un país, no se mostrará la burbuja.

Al clicar sobre una de las burbujas, aparecerá información con el nombre del país y la cantidad de dispositivos encontrados. Esta información viene dada en porcentajes.

En la parte superior del mapa se muestran la fecha y la hora del último dispositivo detectado por el sensor, además de un contador indicando el total de dispositivos detectados, es decir, el equivalente al 100% de dispositivos representados en el gráfico.

### Ejecución

    python lth_upna_map.py [-u] [-p]

        -u    Database username
        -p    Database password

_Se generará un fichero por cada sensor y uno adicional recogiendo los datos de todos los sensores_