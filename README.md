 ESTIMACION DE LA INTENSIDAD DE LLUVIA
 POR : _SANTIAGO CHAUSTRE , NICOLAS MENDEZ,
       CARLOS BARON Y ANDRES COCUNUBO_
======================
Este proyecto consiste en la estimacion de la intensidad
de la lluvia basados en la reflectividad y la relacion Marshall-Palmer

## CONSIDERACIONES ##

- Este es el primer paso para realizar un proyecto aun mas grande, ya que
   debido a la complejidad y el tiempo este proyecto es algo que se ira
   construyendo paso a paso por cada uno de los implicados
- El objetivo final de este proyecto, es presentar un articulo completo
   con la finalidad de ser presentado en alguna revista cientifica en el
   momento que cumpla con todos los objetivos propuestos

** ANEXOS **

Se describira el contenido de los anexos del proyecto, en esta carpeta se
encontraran los siguientes archivos :

- ANEXO_1.png : Esta imagen representa la reflectividad inicial leida del
  archivo netcdf
- ANEXO_2.png : Esta imagen representa los datos de la reflectividad usando
  interpolacion de vecinos cercanos
- ANEXO_3.png : Esta imagen representa la intensidad de lluvia graficafada sobre
  el mapa con el tamaño del radio que abarca el radar.
- ANEXO_4.png : Esta imagen es un intento de interpolacion gausseana de la reflectividad

** CODIGOS **

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
