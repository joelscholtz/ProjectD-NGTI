class WeightedGraphFactory:
    # The constructor of the class
    def __init__( self, store ):
        self.store = store

    def generateWeightedGraphEdges( self ):
        # Create an empty list that will store all the neighbouring waypoints
        neighbours = []

        # Create a loop that goes over all the waypoints
        for waypoint in range( len( self.store.waypoints ) ):
            # Create a variable that is one past the index of waypoint
            # We don't need to check a waypoint against itself
            secondWaypoint = waypoint + 1

            # Have a while loop increase secondWaypoint in order to go over all the waypoints
            while secondWaypoint < len( self.store.waypoints ) :
                # Just be sure that the two waypoints are not the same
                if waypoint == secondWaypoint:
                    continue

                # Get the waypoints, check whether they are neighbors and increase secondWaypoint
                # isNeighbour contains the direction and the distance between two items if they are neighbours
                source = self.store.waypoints[waypoint]
                target = self.store.waypoints[secondWaypoint]
                isNeighbour = source.isNeighbour( target, 10 )
                secondWaypoint = secondWaypoint + 1

                # Check whether the item are actually neighbours
                if isNeighbour:
                    # Split the neightbour
                    ( direction, distance ) = isNeighbour
                    add = True

                    # Loop over all the shelves
                    for shelf in self.store.shelves:
                        # Check whether the points are not being blocked by shit
                        if direction == "Vertically" and shelf.dimensions.isVBlocking( source.dimensions, target.dimensions ):
                            add = False
                        elif direction == "Horizontally" and shelf.dimensions.isHBlocking( source.dimensions, target.dimensions ):
                            add = False
                    
                    if add:
                        # Register the two waypoints as neighbours
                        sourceName = source.category 
                        targetName = target.category
                        neighbours.append( ( sourceName, targetName, abs( distance ) ) )

        # Return the neighbours (the graph)
        return neighbours
