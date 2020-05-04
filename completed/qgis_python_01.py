layer = "/Users/danielmsheehan/GitHub/pratt-savi/pratt-savi-810-2020-03/lessons/pratt-savi-810-2020-03-lesson_13/completed/data/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"

iface.addVectorLayer(layer, "countries", "ogr")

vlayer = iface.addVectorLayer(layer, "countries", "ogr")

iface.showAttributeTable(vlayer)

for field in vlayer.fields():
    print(field.name())
    

for feature in vlayer.getFeatures():
    print(feature["ADMIN"])
    
    
vlayer.setSubsetString("ADMIN LIKE 'A%'")

for feature in vlayer.getFeatures():
    print(feature["ADMIN"])
    

vlayer.renderer().symbol().setColor(QColor("blue"))
vlayer.triggerRepaint()


iface.layerTreeView().refreshLayerSymbology(vlayer.id())

point_layer = "/Users/danielmsheehan/GitHub/pratt-savi/pratt-savi-810-2020-03/lessons/pratt-savi-810-2020-03-lesson_13/completed/data/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg|layername=ne_110m_populated_places"


result = processing.run(
    "native:buffer",   # name of the geoprocessing operation 
    {
        'INPUT': point_layer,
        'DISTANCE':10,
        'SEGMENTS':5,
        'END_CAP_STYLE':0,
        'JOIN_STYLE':0,
        'MITER_LIMIT':2,
        'DISSOLVE':False,
        'OUTPUT':'memory:',
    }
)


QgsProject.instance().addMapLayer(result['OUTPUT'])