from BFSPathFinder import BFSPathFinder
from Graph import Graph
from nodeXY import NodeXY

nodeA = NodeXY("город", 10, 10)
nodeB = NodeXY("деревня", 12, 4)

print(nodeA, nodeB)

g = Graph()
g.add_edge(nodeA, nodeB, 6)
print(g)

pathFinder = BFSPathFinder()
path = pathFinder.getPath(g,nodeA, nodeB)
print(path)


path = pathFinder.getPath(g,nodeB, nodeA)
print(path)

