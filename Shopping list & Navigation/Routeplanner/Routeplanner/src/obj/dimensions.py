class Dimensions:
    # Constructor of the class
    def __init__( self, positionX, positionY, width, height ):
        self.positionX = positionX
        self.positionY = positionY
        self.width = width
        self.height = height

    # Override method for an equality check (==)
    def __eq__( self, other ):
        # Check whether anything in the x or y doesn't match
        if self.positionX != other.positionX or self.positionY != other.positionY:
            return False

        # Check if something in the width or height doesn't match
        if self.width != other.width or self.height != other.height:
            return False

        # Everything matches
        return True

    def isWithinHeight( self, positionY, height, correction = 0 ):
        # Check whether the given Y is below the Y of the object
        if self.positionY - correction > positionY:
            return False

        # Check whether the given height is above the height of the object
        if self.positionY + self.height + correction < positionY + height:
            return False

        # All tests succeeded, return true
        return True

    def isWithinWidth( self, positionX, width, correction = 0 ):
        # Check whether the given X is right of the X of the object
        if self.positionX - correction > positionX:
            return False

        # Check whether the given width is left of the width of the object
        if self.positionX + self.width + correction < positionX + width:
            return False

        # All tests succeeded, return true
        return True

    def isVBlocking( self, item1, item2 ):
        # Check whether we are blocking vertically 
        if self.isWithinHeight( item1.positionY, item1.width ):
            if self.isWithinHeight( item2.positionY, item2.width ):
                return True
        
        # Return false
        return False

    def isHBlocking( self, item1, item2 ):
        # Check whether we are blocking horizontally
        if self.isWithinWidth( item1.positionX, item1.width ):
            if self.isWithinWidth( item2.positionX, item2.width ):
                return True

        # Return false
        return False


    def getHeightDistance( self, positionY ):
        return positionY - self.positionY

    def getWidthDistance( self, positionX ):
        return positionX - self.positionX
