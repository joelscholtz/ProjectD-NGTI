def bestRoute( targets, weightedGraph ):
    # Prepare the creation of a route
    route = list()
    targets = ["Ingang"] + targets
    previousLocation = None
    currentLocation = targets[0]

    # Loop over all the locations that the user wants to visit
    while( targets ):
        # Prepare data storage to keep track of iterations
        currentDistance = float( 'inf' )
        currentPath = None
        currentTarget = None

        # Loop over all the targets, again
        for target in targets:
            # Make sure that the current location is not the same as the target
            if currentLocation != target and not( target == "Uitgang" and currentLocation == "Ingang" ):
                # Get the route and distance to the current location
                ( currentRoute, distance ) = weightedGraph.dijkstra( currentLocation, target )

                # If the route is shorter then previous mentions, save it
                if distance < currentDistance:
                    currentTarget = target
                    currentDistance = distance
                    currentPath = currentRoute

        # Make sure that the currentPath is not null before adding it to the routes
        if currentPath != None:
            route.append( currentPath )
            targets.remove( currentLocation )
            previousLocation = currentLocation
            currentLocation = currentTarget
        else:
            break

    # Get the route to the exit
    ( route_to_exit, currentDistance ) = weightedGraph.dijkstra( currentLocation, "Uitgang" )
    route.append( route_to_exit )

    # Return the final route
    return route
