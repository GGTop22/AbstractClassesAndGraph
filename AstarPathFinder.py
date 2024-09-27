from Graph import Path, Graph
from node import Node


class AstarPathFinder:
    def heuristic(self, node: Node, end_node: Node):
        # return abs(node.x - end_node.x) + abs(node.y - end_node.y)
        return 1

    def getPath(self, graph: Graph, start_node: Node, end_node: Node) -> Path:
        from queue import PriorityQueue

        frontier = PriorityQueue()
        frontier.put((0, start_node))
        came_from = {}
        cost_so_far = {}
        came_from[start_node] = None
        cost_so_far[start_node] = 0

        while not frontier.empty():
            _, current_node = frontier.get()

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                if neighbor == end_node:
                    p2 = Path()
                    p2.node_list = path
                    return p2

            for neighbor in graph.get_reachable_nodes(current_node):

                new_cost = cost_so_far[current_node] + graph.get_edge_weight(current_node, neighbor)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, end_node)
                    frontier.put((priority, neighbor))
                    came_from[neighbor] = current_node

        return None
