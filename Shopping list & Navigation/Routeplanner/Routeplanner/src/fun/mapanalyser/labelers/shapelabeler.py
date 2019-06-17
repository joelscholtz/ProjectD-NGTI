# Import the packages
import cv2

from obj import Dimensions

def labelContourShapes( contour ):
    # Initialize the shape name and approximate the contour
    perimeter = cv2.arcLength( contour, True )
    approximation = cv2.approxPolyDP( contour, 0.04 * perimeter, True )
    dimensions = Dimensions( *cv2.boundingRect( approximation ) )

    # If the shape is a triangle, it will have 3 vertices
    if len( approximation ) == 3:
        shapeName = "Triangle"

    # If the shape has 4, it's either a square or a rectangle
    elif len( approximation ) == 4:
        # Computer the aspect ratio
        aspectRatio = dimensions.width / float( dimensions.height )

        # A square has an aspect ratio of 1, a rectangle doesn't
        shapeName = "Square" if aspectRatio >= 0.95 and aspectRatio <= 1.05 else "Rectangle"

    # If the shape has 5, it's a pentagon
    elif len( approximation ) == 5:
        shapeName = "Pentagon"

    # Otherwise, we assume it's a circle
    else:
        shapeName = "Circle"

    # Return the name of the shape
    return ( shapeName, dimensions )