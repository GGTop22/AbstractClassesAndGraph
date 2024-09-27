import unittest

from node import Node


class NodeTest(unittest.TestCase):
    def test_lt(self):
        node1 = Node("x")
        node2 = Node("y")
        node3 = Node("x")
        self.assertTrue(node1 < node2)
        self.assertFalse(node2 < node1)
        self.assertFalse(node1 < node3)


if __name__ == '__main__':
    unittest.main()
