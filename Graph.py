from node import Node


class Graph:
    # должны описать то что граф представляет собой словарь,ключами в котором являются Ноды ,а значения - это словари ,в которых  ключами являются Ноды,а значения - стоимость пути/вес ребра
    graph: dict[Node, dict[Node, float]]

    def __init__(self):
        self.graph = {}

    def add_node(self, node: Node):
        if node not in self.graph:
            self.graph[node] = {}

    def __repr__(self):
        return f"Graph({self.graph})"

    def add_edge(self, from_node: Node, to_node: Node, weight: float):
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node][to_node] = weight

    def __eq__(self, other):
        return self.graph == other.graph

    # Здесь должен быть метод "получить список вершин в котороые можно попасть из вершины z"
    # Получить список достижимых вершин (z)
    # get list of reachable Nodes

    def get_reachable_nodes(self, z: Node) -> list[Node]:
        if z in self.graph:
            return list(self.graph[z].keys())
        else:
            return []

    def get_all_nodes(self) -> list[Node]:
        return list(self.graph.keys())

    def get_edge_weight(self, from_node: Node, to_node: Node) -> int:
        if from_node in self.graph and to_node in self.graph[from_node]:
            return self.graph[from_node][to_node]
        else:
            return None


class Path:
    node_list: list[Node]

    def __init__(self):
        self.node_list = []

    def add_node(self, node: Node):
        if node not in self.node_list:
            self.node_list.append(node)

    def __repr__(self):
        return f"Path({self.node_list})"

    def __eq__(self, other):
        return self.node_list == other.node_list

    def get_node_list(self):
        return self.node_list
