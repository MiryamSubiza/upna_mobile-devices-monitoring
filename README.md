# UPNA | Monitorización de dispositivos móviles

    Autora: Miryam Subiza Erro
    Proyecto: Desarrollo de sensores pasivos de bajo costo para localización de teléfonos móviles
    Módulo: Análisis de datos

## Descripción:

Se propone analizar el contenido de los paquetes 3G intercambiados entre dispositivos móviles y antenas de las operadoras.
Se observa que, en cada paquete, se envía un código de identificación único para cada dispositivo de telefonía móvil, integrado en la tarjeta SIM y denominado IMSI.
El código IMSI está formado por:
- **MCC:** Código del país.
- **MNC:** Código de la red móvil.
- **MSIN:** Identificación de la estación móvil

Estos datos se envían a una plataforma en la nube y se almacenan en una base datos para poder tratarlos posteriormente.
Con esta información, se propone realizar gráficos mostrando la cantidad de dispositivos capturados por cada sensor, agrupando los datos por países, horas y recorridos.