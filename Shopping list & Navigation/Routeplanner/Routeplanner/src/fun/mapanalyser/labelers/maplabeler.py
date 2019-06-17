from obj import WayPoint, Door, Shelf

def labelMapObject( shape, color, dimensions, center ):
    # Create a placeholder for the detected object
    detectedObject = None

    # Check the shape of the image
    if shape == "Rectangle" or shape == "square":
        # Get the product category from the color of the shape
        productCategory = getProductCategoryFromColor( color )
        if productCategory:
            detectedObject = Shelf( productCategory, dimensions, center )

    if shape == "Circle":
        # Get the right item for the right color
        if color == "Red":
            detectedObject = WayPoint( "Uitgang", dimensions, center )

        if color == "Green":
            detectedObject = WayPoint( "Ingang", dimensions, center )

    if shape == "Triangle":
        # Get the product category from the color of the shape
        productCategory = getProductCategoryFromColor( color )
        if productCategory:
            detectedObject = WayPoint( productCategory, dimensions, center )
        else:
            detectedObject = WayPoint( "WayPoint", dimensions, center )

    # Return the name of the map item
    return detectedObject

def getProductCategoryFromColor( color ):
    if color == "Blue":
        return "Zuivel"
    if color == "Purple":
        return "Koek"
    if color == "Yellow":
        return "Chips"
    if color == "Brown":
        return "Koffie en Thee"
    if color == "Red":
        return "Vlees"
    if color == "Cyaan":
        return "Drinken"
    if color == "Pink":
        return "Alcohol"
    if color == "Green":
        return "Groente en Fruit"
    return ""