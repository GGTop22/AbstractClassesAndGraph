import unittest
from Graph import Graph
from node import Node


class MyTestCase(unittest.TestCase):

    def test_graph(self):
        g = Graph()

        g.add_edge(Node("А"), Node("B"), 56)

        g.add_edge(Node("А"), Node("C"), 32)

        self.assertEqual("Graph({Node(А): {Node(B): 56, Node(C): 32}, Node(B): {}, Node(C): {}})", str(g))

    def test_graph2(self):
        g = Graph()
        g.add_edge(Node("x"), Node("y"), 12)

        g.add_edge(Node("x"), Node("z"), 5)

        g.add_edge(Node("z"), Node("y"), 6)

        self.assertEqual("Graph({Node(x): {Node(y): 12, Node(z): 5}, Node(y): {}, Node(z): {Node(y): 6}})", str(g))

    def test_get_reachable_nodes(self):
        g = Graph()

        node1 = Node('A')
        node2 = Node('B')
        node3 = Node('C')

        g.add_edge(node1, node2, 1.0)
        g.add_edge(node1, node3, 2.0)

        self.assertEqual(g.get_reachable_nodes(node1), [node2, node3])
        self.assertEqual(g.get_reachable_nodes(node2), [])
        self.assertEqual(g.get_reachable_nodes(Node('D')), [])  # Нода D не существует

    def test_get_edge_weight(self):
        xNode = Node("x")
        yNode = Node("y")
        zNode = Node("z")
        g = Graph()
        g.add_edge(xNode, yNode, 12)

        g.add_edge(xNode, zNode, 5)

        g.add_edge(zNode, yNode, 6)

        self.assertEqual(12, g.get_edge_weight(xNode, yNode))
        self.assertEqual(5, g.get_edge_weight(xNode, zNode))
        self.assertEqual(6, g.get_edge_weight(zNode, yNode))
        self.assertEqual(None, g.get_edge_weight(yNode, xNode))
