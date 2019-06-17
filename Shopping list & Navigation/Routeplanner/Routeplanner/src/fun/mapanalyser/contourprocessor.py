import cv2
import imutils

def grabCountersFromThreshold( threshold ):
    # find the contours
    contours = cv2.findContours( threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    contours = imutils.grab_contours( contours )

    # return the contours
    return contours

def getCenterCoordinatesFromContour( contour ):
    # Calculate the center coordinates
    moments = cv2.moments( contour )
    centerX = int( ( moments["m10"] / moments["m00"] ) )
    centerY = int( ( moments["m01"] / moments["m00"] ) )

    # Return the coordinates as tuple
    return ( centerX, centerY )