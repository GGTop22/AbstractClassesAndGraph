import unittest

from AstarPathFinder import AstarPathFinder
from Graph import Graph, Path
from node import Node


class TestAStarPathFinder(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.nodeA = Node('A')
        self.nodeB = Node('B')
        self.nodeC = Node('C')
        self.nodeD = Node('D')

        self.graph.add_edge(self.nodeA, self.nodeB, 1)
        self.graph.add_edge(self.nodeB, self.nodeC, 2)
        self.graph.add_edge(self.nodeA, self.nodeC, 4)
        self.graph.add_edge(self.nodeC, self.nodeD, 1)
        self.graph.add_edge(self.nodeB, self.nodeD, 5)

        self.path_finder = AstarPathFinder()

    def test_path_finding(self):
        path = self.path_finder.getPath(self.graph, self.nodeA, self.nodeD)
        expected_path = Path()
        expected_path.add_node(self.nodeA)
        expected_path.add_node(self.nodeB)
        expected_path.add_node(self.nodeC)
        expected_path.add_node(self.nodeD)

        self.assertEqual(path.get_node_list(), expected_path.get_node_list())

if __name__ == '__main__':
    unittest.main()
