from Graph import Path, Graph
from PathFinder import Path_Finder
from collections import deque

from node import Node


class BFSPathFinder(Path_Finder):
    def getPath(self, graph: Graph, start_node: Node, end_node: Node) -> Path:
        visited = set()
        queue = deque([[start_node]])

        if start_node == end_node:
            p = Path()
            p.add_node(start_node)
            return p

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                neighbors = graph.get_reachable_nodes(node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == end_node:
                        p2 = Path()
                        p2.node_list = new_path
                        return p2
                visited.add(node)
        return None
