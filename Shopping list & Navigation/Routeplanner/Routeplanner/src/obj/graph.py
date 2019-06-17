from collections import deque, namedtuple

class Graph:
    # Constructor of the class
    def __init__( self, edges ):
        # Get all the wrong edges en setup the class
        wrongEdges = [index for index in edges if len( index ) not in [2, 3]]
        self.infinity = float( 'inf' )
        self.edgeTuple = namedtuple( 'Edge', 'start, end, cost' )

        # Show the wrong edges as problems in the console
        if wrongEdges:
            raise ValueError( 'Wrong edges data: {}'.format( wrongEdges ) )

        # Set the edges
        self.edges = list()
        for edge in edges:
            self.addEdge( *edge )

    @property
    def countEdges( self ):
        return len( self.edges )

    @property
    def vertices( self ):
        # Get all the vertices in a set
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def getNodePairs( self, n1, n2, bothEnds = True ):
        # Get all the node pairs
        if bothEnds:
            nodePairs = [[n1, n2], [n2, n1]]
        else:
            nodePairs = [[n1, n2]]
        return nodePairs

    def removeEdge( self, n1, n2, bothEnds = True ):
        # Get all pairs
        nodePairs = self.getNodePairs( n1, n2, bothEnds )
        edges = self.edges[:]

        for edge in edges:
            # Check whether the edge exists
            if [edge.start, edge.end] in nodePairs:
                self.edges.remove( edge )

    def addEdge( self, n1, n2, cost = 1, bothEnds = True ):
        # Make sure that the entrance is not directly linked to the exit
        if not ( ( n1 == "Ingang" and n2 == "Uitgang" ) or ( n1 == "Uitgang" and n2 == "Ingang" ) ):
            # Get all pairs
            nodePairs = self.getNodePairs( n1, n2, bothEnds )
            for edge in self.edges:
                # Prevent problems by checking whether the pair already exists
                if [edge.start, edge.end] in nodePairs:
                    return ValueError( 'Edge {} {} already exists'.format( n1, n2 ) )

            # Append the edge to the list
            self.edges.append( self.edgeTuple( start = n1, end = n2, cost = cost ) )
            if bothEnds:
                self.edges.append( self.edgeTuple( start = n2, end = n1, cost = cost ) )

    @property
    def neighbours( self ):
        # Check for neighbours
        neighbours = { vertex: set() for vertex in self.vertices }
        for edge in self.edges:
            neighbours[edge.start].add( ( edge.end, edge.cost ) )

        # Return the list of neighbours
        return neighbours

    def dijkstra( self, source, destination ):
        # Check for the source node, report if it doesn't exist
        assert source in self.vertices, source + " source node doesn't exist"
        
        # Settup values for the algorithm
        distances = { vertex: self.infinity for vertex in self.vertices }
        previousVertices = { vertex: None for vertex in self.vertices }
        distances[source] = 0
        vertices = self.vertices.copy()

        # Loop over all the vertices
        while vertices:
            # Pick a vertex from the list to work with and remove it
            currentVertex = min( vertices, key = lambda vertex: distances[vertex] )
            vertices.remove( currentVertex )

            # Make sure that there is a way
            if distances[currentVertex] == self.infinity:
                break

            # Loop over all the neighbours
            for neighbour, cost in self.neighbours[currentVertex]:
                # Get possible alternative routes
                alternativeRoute = distances[currentVertex] + cost
                if alternativeRoute < distances[neighbour]:
                    distances[neighbour] = alternativeRoute
                    previousVertices[neighbour] = currentVertex

        # get the path and the current vertex
        path, currentVertex = deque(), destination
        cost = 0

        # Get a list of all the vertices in order to construct the right path
        while previousVertices[currentVertex] is not None:
            path.appendleft( currentVertex )
            currentVertex = previousVertices[currentVertex]

        # Check if there is a path, and add the current point to it
        if path:
            path.appendleft( currentVertex )

        for location in path:
            cost = cost + distances[location]

        # return the path
        return ( path, distances[destination] )