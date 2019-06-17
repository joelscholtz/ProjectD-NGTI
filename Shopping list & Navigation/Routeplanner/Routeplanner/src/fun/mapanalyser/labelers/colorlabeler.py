# Import packages
from scipy.spatial import distance
from collections import OrderedDict

import numpy
import cv2

class ColorLabeler:
    def __init__( self ):
        # Initialize the color dictionary
        colors = OrderedDict( {
            "Red": ( 255, 0, 0 ),
            "Green": ( 0, 255, 0 ),
            "Blue": ( 0, 0, 255 ),
            "Black": ( 0, 0, 0 ),
            "Purple": ( 100, 0, 100 ),
            "Yellow": ( 255, 255, 0 ),
            "Brown": ( 150, 100, 50 ),
            "Cyaan": ( 100, 255, 255 ),
            "Pink": ( 255, 50, 200 )
        })

        # Allocate space for the image and initialize the color names
        self.lab = numpy.zeros( ( len( colors ), 1, 3 ), dtype = "uint8" )
        self.colorNames = []

        # Loop over the colors in the dictionary
        for ( index, ( name, rgb ) ) in enumerate( colors.items() ):
            # Update the array and the color name list
            self.lab[ index ] = rgb
            self.colorNames.append( name )

        # Convert the color space to L*a*b
        self.lab = cv2.cvtColor( self.lab, cv2.COLOR_RGB2LAB )

    def labelContourColours( self, image, contour ):
        # construct a mask for the contour and calculate the average color
        mask = numpy.zeros( image.shape[ :2 ], dtype = "uint8" )
        cv2.drawContours( mask, [contour], -1, 255, -1 )
        mask = cv2.erode( mask, None, iterations = 2 )
        mean = cv2.mean( image, mask = mask )[:3]

        # Initialize the minimum distance
        minimumDistance = ( numpy.inf, None )

        # Loop over the known lab color values
        for ( index, row ) in enumerate( self.lab ):
            # Compute the difference with the current color
            difference = distance.euclidean( row[0], mean )

            # if the difference is smaller, then the current color is a better match
            if difference < minimumDistance[0]:
                minimumDistance = ( difference, index )

        # Return the name of the color with smallest distance
        return self.colorNames[ minimumDistance[1] ]