class WayPoint:
    # Constructor of the class
    def __init__( self, category, dimensions, center ):
        self.dimensions = dimensions
        self.category = category
        self.center = center

    # Override method for an equality check (==)
    def __eq__(self, other):
        # Check something doesn't match
        if self.category != other.category or self.dimensions != other.dimensions:
            return False

        # Everything matches
        return True

    # Function that checks whether a waypoint is vertically or horizontally alined with the current one
    def isNeighbour( self, target, correction = 0 ):
        # Check whether the other waypoint is within the height of this one
        if self.dimensions.isWithinHeight( target.dimensions.positionY, target.dimensions.height, correction ):
            # Get the difference in width
            widthDifference = self.dimensions.getWidthDistance(target.dimensions.positionX)

            # Return the distance
            return ( "Horizontally", widthDifference )

        # Check whether the other waypoint is within the width of this one
        if self.dimensions.isWithinWidth( target.dimensions.positionX, target.dimensions.width, correction ):
            # Get the difference in height
            heightDifference = self.dimensions.getHeightDistance(target.dimensions.positionY)

            # Return the distance
            return ( "Vertically", heightDifference )

        # All tests failed, return true
        return False

    

