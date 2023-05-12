from qgis.core import *
from qgis.utils import iface
from qgis.gui import *

def generate_transects(polygon_layer_name, interval, direction):
    # Load the polygon layer defining the area
    polygon_layer = QgsProject.instance().mapLayersByName(polygon_layer_name)[0]

    # Create a memory layer for the transects
    vl = QgsVectorLayer("LineString", "Transects", "memory")
    pr = vl.dataProvider()

    # Add the fields for the transects
    pr.addAttributes([QgsField("id", QVariant.Int)])
    vl.updateFields()

    # Set the CRS of the transects layer
    vl.setCrs(QgsCoordinateReferenceSystem(27700, QgsCoordinateReferenceSystem.EpsgCrsId))

    # Get the bounds of the polygon layer
    bounds = polygon_layer.extent()
    xmin = bounds.xMinimum()
    xmax = bounds.xMaximum()
    ymin = bounds.yMinimum()
    ymax = bounds.yMaximum()

    # Generate the transects
    id = 1
    if direction == "N-S":
        for y in range(int(ymin), int(ymax), int(interval)):
            for x in range(int(xmin), int(xmax), int(interval)):
                line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x, y + interval)])
                for polygon_feature in polygon_layer.getFeatures():
                    polygon = polygon_feature.geometry()
                    if line.intersects(polygon):
                        intersected_line = line.intersection(polygon)
                        feat = QgsFeature()
                        feat.setGeometry(intersected_line)
                        feat.setAttributes([id])
                        pr.addFeatures([feat])
                        id += 1
    elif direction == "E-W":
        for x in range(int(xmin), int(xmax), int(interval)):
            for y in range(int(ymin), int(ymax), int(interval)):
                line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x - interval, y)])
                for polygon_feature in polygon_layer.getFeatures():
                    polygon = polygon_feature.geometry()
                    if line.intersects(polygon):
                        intersected_line = line.intersection(polygon)
                        feat = QgsFeature()
                        feat.setGeometry(intersected_line)
                        feat.setAttributes([id])
                        pr.addFeatures([feat])
                        id += 1
    elif direction == "SE-NW":
        for y in range(int(ymin), int(ymax), int(interval)):
            for x in range(int(xmin), int(xmax), int(interval)):
                line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x + interval, y + interval)])
                # Check if the line intersects with any polygon
                for polygon_feature in polygon_layer.getFeatures():
                    polygon = polygon_feature.geometry()
                    if line.intersects(polygon):
                        # Get the intersected line
                        intersected_line = line.intersection(polygon)
                        # Add the intersected line as a transect
                        feat = QgsFeature()
                        feat.setGeometry(intersected_line)
                        feat.setAttributes([id])
                        pr.addFeatures([feat])
                        id += 1
    elif direction == "SW-NE":
        for y in range(int(ymin), int(ymax), int(interval)):
            for x in range(int(xmin), int(xmax), int(interval)):
                line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x + interval, y + interval)])
                # Check if the line intersects with any polygon
                for polygon_feature in polygon_layer.getFeatures():
                    polygon = polygon_feature.geometry()
                    if line.intersects(polygon):
                        # Get the intersected line
                        intersected_line = line.intersection(polygon)
                        # Add the intersected line as a transect
                        feat = QgsFeature()
                        feat.setGeometry(intersected_line)
                        feat.setAttributes([id])
                        pr.addFeatures([feat])
                        id += 1
    elif direction == "NNW-SSE":
        for y in range(int(ymin + interval/2), int(ymax), int(interval)):
            for x in range(int(xmin), int(xmax), int(interval)):
                line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x + interval, y - interval/2)])
                # Check if the line intersects with any polygon
                for polygon_feature in polygon_layer.getFeatures():
                    polygon = polygon_feature.geometry()
                    if line.intersects(polygon):
                        # Get the intersected line
                        intersected_line = line.intersection(polygon)
                        # Add the intersected line as a transect
                        feat = QgsFeature()
                        feat.setGeometry(intersected_line)
                        feat.setAttributes([id])
                        pr.addFeatures([feat])
                        id += 1
    elif direction == "NNE-SSW":
            for x in range(int(xmin), int(xmax), int(interval)):
                for y in range(int(ymax), int(ymin), -int(interval)):
                    line = QgsGeometry.fromPolylineXY([QgsPointXY(x, y), QgsPointXY(x + interval, y - interval)])
                    for polygon_feature in polygon_layer.getFeatures():
                        polygon = polygon_feature.geometry()
                        if line.intersects(polygon):
                            intersected_line = line.intersection(polygon)
                            feat = QgsFeature()
                            feat.setGeometry(intersected_line)
                            feat.setAttributes([id])
                            pr.addFeatures([feat])
                            id += 1



    QgsProject.instance().addMapLayer(vl)

# add the 3 paramateres here: polygon name, transects distance and direction e.g ("10mt_transect", 10, "NNW-SSE")
generate_transects("", ,"" )
