import cv2

def getImage( imagePath ):
    # Return the image when received with cv2
    return cv2.imread( imagePath )

def getLabAndThreshold( imagePath ):
    # Get the image
    image = getImage( imagePath )

    # Manipulate the image in order to make them checkable
    blurredImage = cv2.GaussianBlur( image, ( 5, 5 ), 0 )
    grayImage = cv2.cvtColor( blurredImage, cv2.COLOR_BGR2GRAY )
    labImage = cv2.cvtColor( blurredImage, cv2.COLOR_BGR2LAB )
    threshold = cv2.threshold( grayImage, 240, 255, cv2.THRESH_BINARY_INV )[1]

    # Return the lab-colored image and the thresholded grayscale
    return ( labImage, threshold )