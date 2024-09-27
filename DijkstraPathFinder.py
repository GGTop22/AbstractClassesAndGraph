import heapq

from Graph import Graph, Path
from PathFinder import Path_Finder
from node import Node


class DijkstrapathFinder(Path_Finder):
    def getPath(self, graph: Graph, start: Node, end: Node) -> Path:
        path = Path()
        distances = {node: float('inf') for node in graph.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_nodes = {node: None for node in graph.graph}
        current_node = start
        current_distance = 0
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == end:
                break

            for neighbor, weight in graph.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

            if current_distance > distances[current_node]:
                continue
        if current_node != end:
            return None
        # Reconstruct the path
        #current_node = end
        #while current_node is not None:
            #path.add_node(current_node)
            #current_node = previous_nodes[current_node]
        # ТАК ДЕЛАТЬ НЕЛЬЗЯ!
        #path.path.reverse()


        # Восстанавливаем путь с использованием стека
        stack = []
        current_node = end
        while current_node is not None:
            stack.append(current_node)
            current_node = previous_nodes[current_node]

        # Добавляем узлы в путь в правильном порядке
        stack.reverse()
        for x in stack:
            path.add_node(x)

        return path

