 ESTIMACION DE LA INTENSIDAD DE LLUVIA
 POR : _SANTIAGO CHAUSTRE , NICOLAS MENDEZ,
       CARLOS BARON Y ANDRES COCUNUBO_
======================

Este proyecto consiste en la estimacion de la intensidad
de la lluvia basados en la reflectividad y la relacion Marshall-Palmer
graficando tambien los resultados obtenidos en imagenes con
clasificacion de color.

## CONSIDERACIONES ##

- Este es el primer paso para realizar un proyecto aun mas grande, ya que
   debido a la complejidad y el tiempo este proyecto es algo que se ira
   construyendo paso a paso por cada uno de los implicados
- El objetivo final de este proyecto, es presentar un articulo completo
   con la finalidad de ser presentado en alguna revista cientifica en el
   momento que cumpla con todos los objetivos propuestos
- Las interpolaciones se hicieron borrando datos aleatoriamente generando
  numeros en un rango de 0 a 25 en los cuales si generaba un 0, se borraba
  el dato
  
## ARCHIVOS ##

- La estructura basica de este repositorio esta clasificada en dos carpetas
  y tres archivos en el primer directorio, eston son :

    1. **ANEXOS -** _(Carpeta)_
    2. **CODIGOS -** _(Carpeta)_
    3. **Articulo-EstimacionLluvia.pdf -** _Representa  el articulo sobre el trabajo_
    4. **LICENSE -** _Tiene los parametros basicos de licencia en el proyecto_
    5. **README.md -** _Archivo con la informacion a tener en cuenta_

- El contenido de cada directorio sera explicado a continuacion.

**ANEXOS**

Se describira el contenido de los anexos del proyecto, en esta carpeta se
encontraran los siguientes archivos :

- ANEXO_1.png : Esta imagen representa la reflectividad inicial leida del
  archivo netcdf
- ANEXO_2.png : Esta imagen representa los datos de la reflectividad usando
  interpolacion de vecinos cercanos
- ANEXO_3.png : Esta imagen representa la intensidad de lluvia graficafada sobre
  el mapa con el tamaño del radio que abarca el radar.
- ANEXO_4.png : Esta imagen es un intento de interpolacion gausseana de la reflectividad

**CODIGOS**

En la carpeta de codigos, se encontraran los siguientes archivos :

- Interpolacion.py : En este documento de codigo python se interpola
  la reflectividad usando vecinos cercanos y gaussiano
- mapa.jpg : Esta es una imagen que delimita en un mapa el radio que
  abarca la cobertura del radar del cual se tomaron los datos
- Precipitacion.py : En este archivo fuente de python se encuentran los
  calculos de la intensidad de la lluvia mediante el metodo Marshall-Palmer
- Reflectividad.py : En este archivo de codigo fuente de python se encuentra
  el codigo para leer el archivo netcdf con los datos a procesar
- TAB130416002504_RAW4EU9.nc : Es el archivo en el cual se encuentran los
  datos obtenidos por el radar en un archivo netcdf

## AGRADECIMIENTOS ##

Se agradece a cualquier pesona que se interese en este trabajo, ya que ha venido
siendo realizado con mucho esfuerzo y paciencia por cada uno de los miembros implicados
y es el reflejo de las diferentes etapas en un trabajo investigativo, desde la recoleccion
de datos hasta su procesamiento y sobre todo su entendimiento, ya que es esta interpretacion
la que le da verdadero valor a este tipo de trabajos.

Con nuestro esfuerzo, estamos seguros que a base de pequeñas contribuciones de cada uno,
podremos ir complementando el trabajo  hasta obtener el resultado esperado el cual nos
permita presentarlo en alguna revista o congreso con relacion al tema principal.


Esperamos que el trabajo sera del agrado de todos, un abrazo.
