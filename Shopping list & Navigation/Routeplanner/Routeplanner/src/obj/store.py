import obj as Objects

class Store:
    # The constructor of the class
    def __init__( self ):
        self.waypoints = list()
        self.waypointName = 1
        self.doors = list()
        self.shelves = list()

    # Print a string listing store details
    def __str__(self):
        return "Store details:\nWaypoints: {0}\nShelves: {1}\nDoors: {2}".format( 
            str( len( self.waypoints ) ),
            str( len( self.shelves ) ),
            str( len( self.doors ) ),
        )

    def addItem( self, item ):
        # Check where the item should be added
        if isinstance( item, Objects.WayPoint ):
            # Check the name of the waypoint
            if item.category == "WayPoint":
                item.category = str( self.waypointName )
                self.waypointName = self.waypointName + 1

            self.waypoints.append( item )
        elif isinstance( item, Objects.Shelf ):
            self.shelves.append( item )
        elif isinstance( item, Objects.Door ):
            self.doors.append( item )