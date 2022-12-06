from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
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
    geom = f.geometry()
    print("Length:", geom.length())
    
for field in perfil.fields():
    print(field.name(), field.typeName())
    
