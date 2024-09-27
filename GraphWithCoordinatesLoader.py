from Graph import Graph
from Loader import GraphLoader
from node import Node
from nodeXY import NodeXY


class GraphWithCoordinatesLoader(GraphLoader):
    def __init__(self, filename):
        self.filename = filename
        # self.graph = {}

    def getGraph(self) -> Graph:
        g = Graph()
        d = {}
        with open(self.filename, 'r', encoding='utf-8') as file:
            nodes_section = False  # Флаг, чтобы разделить узлы и ребра
            edge_section = False

            for line in file:
                line = line.strip()

                if line == "Nodes{":
                    nodes_section = True
                    continue

                if line == "}":
                    nodes_section = False
                    edge_section = False
                    continue

                if line == "Edges {":
                    edge_section = True
                    continue

                if nodes_section:
                    # Ожидается формат: узел x y
                    name, x, y = line.split()
                    x, y = int(x), int(y)
                    node = NodeXY(name, x, y)
                    d[name] = node
                    # self.graph[node] = [] здесь нужно доделать
                elif edge_section:
                    # Ожидается формат: узел1 узел2 вес (ребро)
                    from_node_name, to_node_name, weight = line.split()
                    from_node = d[from_node_name]
                    to_node = d[to_node_name]
                    weight = float(weight)

                    if from_node and to_node:
                        g.add_edge(from_node, to_node, weight)

        return g
