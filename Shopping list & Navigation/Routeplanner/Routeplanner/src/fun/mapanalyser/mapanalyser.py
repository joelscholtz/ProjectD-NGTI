from obj import Store

import fun.mapanalyser.imagereader as imagereader
import fun.mapanalyser.contourprocessor as contourprocessor
import fun.mapanalyser.labelers as labelers
import imutils
import cv2

def analyseMap( mapPath ):
    # Create some analysable images and get the contours 
    ( labImage, threshold ) = imagereader.getLabAndThreshold( mapPath )
    contours = contourprocessor.grabCountersFromThreshold( threshold )

    # Create an instance of the colorlabeler and store
    colorLabeler = labelers.colorlabeler.ColorLabeler()
    store = Store()

    # Loop over the contours
    for contour in contours:
        # Check whether the contours are within the threshold
        if cv2.contourArea( contour ) > 0:
            # Get all data from the contour
            objectCenter = contourprocessor.getCenterCoordinatesFromContour( contour )
            ( shape, dimensions ) = labelers.shapelabeler.labelContourShapes( contour )
            color = colorLabeler.labelContourColours( labImage, contour )
        
            # Generate an item and add it to the store
            item = labelers.maplabeler.labelMapObject( shape, color, dimensions, objectCenter )
            store.addItem( item )

    # Return all the items
    return store
    