![](img/Aspose.Words.07d8cf39-75e0-4b01-a6c3-d2db387911cc.003.png)
![](img/Aspose.Words.07d8cf39-75e0-4b01-a6c3-d2db387911cc.004.png)

![](https://upload.wikimedia.org/wikipedia/commons/7/7d/Logo_de_la_Universidad_de_Colima.svg)

# Proyección de un perfil y el cálculo de su longitud en PyQgis
*Projecting a profile and calculating its length in PyQgis*

**Daniela Nohemí González Preciado (1), Roberto Alejandro Navarro Obispo (2), Vanessa Belén Martínez Hernández (3)**

(1) Colima - Coquimatlán Kilómetro 9, Jardines del Llano, 28400 Coquimatlán, Col., 20186496, <dgonzalez17@ucol.mx>. (2) 20172919, <rnavarro0@ucol.mx>. (3) 20177585, <vmartinez6@ucol.mx> 
##
## **1.Introducción.** 
La nivelación de perfil tiene como objetivo determinar las cotas o elevaciones de puntos con distancias conocidas sobre un trazo para obtener el perfil del trazo.  

Cuando se requiere del estudio de una vía de comunicación terrestre ya sea de camino, introducción de agua potable, un sistema de alcantarillado, un canal, entre otros; se utiliza este procedimiento el cual se encarga de determinar las elevaciones, cotas y alturas o intervalos cortos sobre una línea fija generalmente sobre el centro de un eje de la vía que se presenta alojar.  

Por lo general esos intervalos son en forma longitudinal a cada 20m y cambio de pendientes importantes a estos intervalos se les llama estaciones complejas o estaciones cerradas a los oros puntos se les conoce como estaciones intermedias, en cada estación se clava una estaca a la cual tiene su respectivo kilometraje.  

Programar significa tener la habilidad de crear y codificar un algoritmo para que pueda ser ejecutado por una computadora. Es decir, se desarrollan un conjunto de instrucciones que le indican a la computadora cómo hacer ciertas tareas. En la actualidad, la programación es catalogada como un lenguaje tecnológico fundamental. ¿Por qué es tan importante aprender programación hoy en día? el constante progreso de la tecnología aplicado a cualquier ámbito profesional, el desarrollo de capacidades resolutivas, la amplia oferta de trabajo que ofrece la industria IT.

Un perfil topográfico es un corte o sección a lo largo de una línea dibujada en un mapa. En otras palabras, es como si se pudiera rebanar una porción de la Tierra y separarla del resto para poder verla de lado a lado; la superficie de esta rebanada sería el perfil topográfico. ¿Cuál es el uso de un perfil topográfico? Un perfil topográfico permite un mejor conocimiento de los Modelos Digitales de Elevaciones (MDE), ya que el análisis de elementos lineales es más sencillo que el análisis de superficies.

## **2.Desarrollo**

**Nivelación de perfil**

![](http://4.bp.blogspot.com/_oKSDCrhgRhk/TE9KOhus3NI/AAAAAAAAADY/kanzAg_9XkY/s1600/nivel_-_desnivel.jpg)

Figura #1. Gráfico de una nivelación de perfil. Fuente: Google

Es la operación, usualmente por nivelación directa, de determinar las elevaciones de puntos a cortos intervalos a lo largo de una línea localizada tal como el centro para una carretera o tubería. Es también usada para determinar elevaciones de cortes o secciones, contornos y gradientes.

Son colocadas estacas a intervalos regulares sobre esta línea, usualmente la línea central. El intervalo escogido es uno conveniente de acuerdo con la longitud del perfil, tal como 100, 50, 25 mts. Los puntos al intervalo escogido, tal como por ejemplo 100 m son llamados estación completa y todos los otros puntos, estaciones “más”, (+). Por ej. Una estaca colocada a 1600 m del punto de inicio es numerada “16+00” y una colocada a 1,625,” 16+25, cuando se usa intervalos de 100 m. En caso de usar intervalo de 1000 m la numeración sería	1+600 y 1+625, correspondientemente. Las elevaciones por medio de las cuales el perfil se construyen son levantadas tomando lectura de nivelación sobre las estacas o en puntos intermedios donde ocurren cambios de pendientes.

![](https://drive.google.com/uc?export=view&id=1WQJfl6Io_q4l9vtbIM_3lDi9A9UG7cr0)

Debe tenerse cuidado en la escogencia de los puntos de cambio ya que éstos son los puntos de enlace o de transferencia de cotas. Deben ser puntos firmes en el terreno, o sobre estacas de madera, vigas de puentes, etc.

Siendo los puntos de cambio puntos de transferencia de cotas, en ellos siempre será necesario tomar una lectura adelante desde una estación y una lectura atrás desde la estación siguiente.

Procedimiento:

- Se colocan desde el principio de la línea, una serie de puntos llamados estaciones completas, los cuales van a estar una de la otra a una distancia de 20m (por lo general, ya que puede ser otra 10m, 50m etc.), aunque esta distancia puede variar, además de las estaciones completas, también se ubican los puntos donde hay cambios de dirección, cambios de pendiente, etc. llamados subestaciones.

- Estación Completa: son los puntos situados cada 20 metros completos, ejemplo: 0+020, 0+100, 0+240, 0+980, 1+000, 1+120, etc.
- Subestación: son puntos situados en la línea central que no están a 20 metros completos, ejemplo: 0+95.40, 0+985.40, 1+125.30, 1+242.6, etc.



Las elevaciones con que se construyen los perfiles se obtienen de las lecturas del estadal tomadas en cada estación y subestación.

Ejemplo de registro:

![](https://drive.google.com/uc?export=view&id=1-JmtzWf3QFOnUFx-aOV5DmBl_cmcfU7v) 

Figura #2. Ejemplo de registro de una nivelación de perfil. Fuente: M.C. Rosendo Sánchez

## **2.1. Metodología** 
#
Comprobación ida y vuelta

Esta comprobación se realiza repitiendo la nivelación en sentido contrario, ya sea siguiendo la misma ruta u otra distinta. Este procedimiento tiene la ventaja de que, al repetir la nivelación en dirección contraria, se pueden eliminar ciertos errores de acumulación

Procedimiento:

Es igual a la simple con la única diferencia que el aparato se plantara más de una vez y por consiguiente la altura de instrumento será diferente cada vez que se cambie. Este tipo de nivelación se realiza cuando los terrenos son bastantes accidentados y exceden visuales de 200 m., en otras palabras, la nivelación compuesta es una serie de nivelaciones simples amarradas entre sí por puntos de cambio o de liga del aparato.  

|**P.V.**|**+**|**A.I.**|**-**|**COTA**|
| - | - | - | - | - |
|**BN1**|0.274|355.254| |354.98|
|**0+000**|0.595|353.88|1.969|353.285|
|**0+020**| | |2.683|351.197|
|**0+040**| | |3.88|350|
|**0+053**| | |4.415|349.465|
|**PL1**|1.015|351.187|3.708|350.172|
|**0+060**| | |1.588|349.599|
|**0+080**| | |1.105|350.082|
|**0+100**| | |0.648|350.539|
|**0+120**| | |0.161|351.026|
|**PL2**|2.888|353.986|0.089|351.098|
|**0+140**| | |2.425|351.561|
|**0+156**| | |1.945|352.041|
|**0+160**| | |1.514|352.472|
|**0+180**| | |1.023|352.963|
|**PL3**|3.816|357.64|0.162|353.824|
|**0+200**| | |3.214|354.426|
|**0+220**| | |0.625|357.015|
|**PL4**|3.772|360.787|0.625|357.015|
|**0+240**| | |3.003|357.784|
|**0+260**| | |2.257|358.53|
|**0+269**| | |1.914|358.873|
|**0+280**| | |1.687|359.1|
|**0+300**| | |1.347|359.44|
|**0+320**| | |1.038|359.749|
|**0+340**| | |0.709|360.078|
|**0+349**| | |0.602|360.185|
|**BN2**| | |0.383|360.404|
|**Comprobación de Vuelta**|
|**BN2**|0.349|360.753| |360.404|
|**PL4**|0.118|357.132|3.739|357.014|
|**PL3**|0.231|354.053|3.31|353.822|
|**PL2**|0.01|351.108|2.955|351.098|
|**PL1**|3.485|353.646|0.947|350.161|
|**PL0**|2.229|355.506|0.369|353.277|
|**BN1**| | |0.532|354.974|

Comprobación Ida y Vuelta: se efectúa la nivelación en un sentido (nivelación de ida), trabajando con el método del punto medio, concluida esta, se inicia la nivelación de regreso, pudiendo utilizar los mismos PL’s que se usaron en el primer recorrido.

![](https://drive.google.com/uc?export=view&id=14MH49QmR_xI0EOpw1nF_wTxpEqIQ4aNw)

EL trabajo de campo se realizó en el campus Coquimatlán de la Universidad de Colima, se necesitó de importantes instrumentos topográficos, así como la adecuada indumentaria para su realización. Se dio principio con el reconocimiento del terreno del cual se tenía que obtener el perfil, consecutivamente en la parte sur del campus en donde se encuentra un estacionamiento, se indicó un banco de nivel (BN) teniendo una cota arbitraria.


**Qgis**

QGIS es un Sistema de Información Geográfica (SIG) de Código Abierto licenciado bajo GNU - General Public License . QGIS es un proyecto oficial de Open Source Geospatial Foundation (OSGeo). Corre sobre Linux, Unix, Mac OSX, Windows y Android y soporta numerosos formatos y funcionalidades de datos vector, datos ráster y bases de datos.

QGIS funciona en diferentes sistemas operativos: Linux, Windows, Mac y Android. Además, se puede instalar en una llave USB, lo que permite transportar QGIS de un ordenador a otro sin tener que instalarlo.

Uno de sus puntos fuertes es la interoperabilidad y te permitirte trabajar con una multitud de datos vectoriales y raster. Por citar algunos:

- Formato Shapefile (.shp formato nativo de QGIS) desarrollado por ESRI ArcGIS.
- Formatos MapInfo (.tab, mif-mid).
- Formato KML de Google Earth.
- Formatos DAO (Autocad DXF).

![QGIS](https://geomatiqueagricole.ca/wp-content/uploads/2019/01/QGIS_logo_2017.svg_-1024x305.png)
Figura #4. Logo de Qgis.

**Python**

Python es un lenguaje de programación orientado a objetos de alto nivel y fácil de interpretar con sintaxis fácil de leer. Ideal para prototipos y tareas ad hoc, Python tiene un amplio uso en computación científica, desarrollo web y automatización. Como lenguaje de programación para principiantes y de uso general, Python es compatible con muchos de los principales científicos de computadoras y desarrolladores de aplicaciones en todo el mundo.


![Python Programación - 14102 - Otras clases o cursos - Ciudad Autónoma ...](https://download.logo.wine/logo/Python_(programming_language)/Python_(programming_language)-Logo.wine.png)
Figura #5. Logo de Python.

## **3.Manejo de datos**

Para este programa se realiza un análisis de las diferentes librerías de PyQgis, la cual es una consola de Python en el software de Qgis. Primeramente se analiza la capa del vector, la cual fue resultado de los datos de una práctica de campo llevada a cabo en la Facultad de Ingeniería Civil en el camino del estacionamiento. Una vez obtenido el shapefile del vector, se realiza un programa el cual permite abrir una capa de archivo “.shp” y de esta misma calcula la longitud que esta tiene.



![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.07d8cf39-75e0-4b01-a6c3-d2db387911cc.014.png)



![Interfaz de usuario gráfica, Texto, Aplicación, Chat o mensaje de texto

Descripción generada automáticamente](Aspose.Words.07d8cf39-75e0-4b01-a6c3-d2db387911cc.015.png)





## **4.Resultados**

from PyQt5.QtCore import \*

from PyQt5.QtGui import \*

from qgis.core import \*

from qgis.gui import \*

from osgeo import gdal, osr

from PyQt5.QtCore import QVariant

#Vector

perfil = 'C:\\PyQGIS\\Perfil.shp'

perfil = QgsVectorLayer(perfil,'perfil','ogr')

#Raster

colima ='C:\\PyQGIS\\B5.TIF'

fileInfo = QFileInfo(colima)

baseName = fileInfo.baseName()

raster = QgsRasterLayer(colima, baseName)

QgsProject.instance().addMapLayer(raster)

QgsProject.instance().addMapLayer(perfil)

layer = qgis.utils.iface.activeLayer()

features = layer.selectedFeatures()

for f in features:

`    `geom = f.geometry()

`    `print("Length:", geom.length())



for field in perfil.fields():

`    `print(field.name(), field.typeName())

## **5.Conclusion**

En relación a todo lo visto durante todo el semestre, se realizó un proyecto en el cual nos basamos en pyqgis, la cual es la librería de QGIS para ejecutar código Python. Se realizo un codigo con el lenguaje de programacion ya mencionado, en el cual a partir de un vector ya creado de un perfil se añade a una imagen raster de Colima. Conforme con esta libreria,observamos que tiene bastante relación dentro de nuestra carrera, pues la aplicación de los diferentes códigos vistos en clases, nos facilitan y agilizan la interacción con la plataforma Qgis, así bien consideramos que la aplicación de estos códigos y similares en la rama de geomatica y topografica es importante su conocimiento y aplicacion para futuros proyectos academicos como personales.

Concluimos que el uso de la tecnología para la realización de cálculos es importante, ya que estos se realizan de una manera rápida y eficaz, pudiendo así menorar el tiempo en la verificación de la nivelación. La nivelación es una operación fundamental para el ingeniero, tanto para poder confeccionar un proyecto, como para lograr replantear el mismo. Las aplicaciones más comunes de la nivelación son: En proyecto de carreteras y canales que deben tener pendientes determinadas. Situar obras de construcción de acuerdo con elevaciones planeadas. Calcular volúmenes de terracería. (Volúmenes de tierra). Investigar características de drenaje y escurrimiento de superficies. Establecer puntos de control mediante el corrimiento de una cota.

Recordemos que la nivelación geométrica o nivelación diferencial es el procedimiento topográfico que nos permite determinar el desnivel entre dos puntos mediante el uso del nivel y la mira vertical. La nivelación geométrica mide la diferencia de nivel entre dos puntos a partir de la visual horizontal lanzada desde el nivel hacia las miras colocadas en dichos puntos. Cuando los puntos a nivelar están dentro de los límites del campo topográfico altimétrico y el desnivel entre dichos puntos se puede estimar con una sola estación, la nivelación recibe el nombre de nivelación geométrica simple. Cuando los puntos están separados a una distancia mayor que el límite del campo topográfico, o que el alcance de la visual, es necesario la colocación de estaciones intermedias y se dice que es una nivelación compuesta.

## **6. Referencias**

• Gamez W. (2013). Texto Básico Auto informativo de topografía general. Universidad Nacional Agraria.

• García Márquez, Fernando. (1994). Curso Básico de Topografía. Árbol Editorial, S.A. de C.V. México, D.F

• Reales, H. (2019). Introducción a la altimetría. Facultad de Ingenierias de la Universidad Tecnológica de Chocó.

• Zamarripa, M. (2010). Apuntes de Topografía. Facultad de Estudios Superiores Acatlán

• breco. (31 de 10 de 2022). abreco.com.mx.Obtenido de abreco.com.mx: https://www.abreco.com.mx/glosario_topografia.htm#:~:text=TRANSITO%3A,con%20solo%20tres%20tornillos%20nivelantes.

• CAMPOS, A. O. (31 de 10 de 2022). prezi.com. Obtenido de prezi.com: https://prezi.com/jri9j2z0l1wi/mate-aplicada-atopografia/#:~:text=La%20topograf%C3%ADa%20se%20basa%2C%20en,x%2Cy%2Cz).

• Eduard., L. (31 de 10 de 2022). acolita.com. Obtenido de acolita.com: https://acolita.com/evolucion-de-lastecnicas-topograficas/

• Palacio, T. (31 de 10 de 2022). taringa.net. Obtenido de taringa.net: https://www.taringa.net/+ciencia_educacion/aplicaciones-de-la-trigonometria-en-latopografia_hnvbt
• qgis. (31 de 10 de 2022). qgis.org. Obtenido de qgis.org: https://www.qgis.org/es/site/about/index.html

• rmsgeoespacial. (31 de 10 de 2022). rmsgeoespacial.com. Obtenido de rmsgeoespacial.com:https://rmsgeoespacial.com/comoseutilizaungpstopografico/#:~:text=Un%20gps%20topogr%C3%A1fico%20nos%20ayuda,al%20sistema%20de%20posicionamiento%20satelital
