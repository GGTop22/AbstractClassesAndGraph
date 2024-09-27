import unittest

from BFSPathFinder import BFSPathFinder
from Graph import Graph, Path
from node import Node


class TestBFSPathFinder(unittest.TestCase):
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

        self.path_finder = BFSPathFinder()

    def test_path_finding(self):
        path = self.path_finder.getPath(self.graph, self.nodeA, self.nodeD)

        self.assertIsNotNone(path)

    def test_path_finding2(self):
        path = self.path_finder.getPath(self.graph, self.nodeD, self.nodeA)
        self.assertIsNone(path)

    def test_path_finding3(self):
        graph2 = Graph()
        graph2.add_edge(self.nodeA, self.nodeB, 1)
        graph2.add_edge(self.nodeB, self.nodeC, 1)
        graph2.add_edge(self.nodeA, self.nodeC, 1)
        graph2.add_edge(self.nodeC, self.nodeD, 1)
        graph2.add_edge(self.nodeB, self.nodeD, 1)
        path = self.path_finder.getPath(graph2, self.nodeA, self.nodeD)

        expected_path1 = Path()
        expected_path1.add_node(self.nodeA)
        expected_path1.add_node(self.nodeC)
        expected_path1.add_node(self.nodeD)

        expected_path2 = Path()
        expected_path2.add_node(self.nodeA)
        expected_path2.add_node(self.nodeB)
        expected_path2.add_node(self.nodeD)



        self.assertIn(path,[expected_path2,expected_path1])


if __name__ == '__main__':
    unittest.main()
