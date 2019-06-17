from obj import weightedgraphfactory, graph
import fun.mapanalyser as mapanalyser
import fun.router as routeplanner

# Get the store details
store = mapanalyser.analyseMap( "../res/img/map.png" )

# Prepare the graph for dijkstra
graphFactory = weightedgraphfactory.WeightedGraphFactory( store )
edges = graphFactory.generateWeightedGraphEdges()
weightedGraph = graph.Graph( edges )

# Create a list
targets = [ "Vlees", "Koffie en Thee", "Alcohol", "Chips", "Zuivel" ]

# Get the fastest route
route = routeplanner.router.bestRoute( targets, weightedGraph )
print( route )