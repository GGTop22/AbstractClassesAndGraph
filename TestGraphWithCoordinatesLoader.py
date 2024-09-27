import os
import unittest

from Graph import Graph
from GraphWithCoordinatesLoader import GraphWithCoordinatesLoader
from nodeXY import NodeXY


class TestGraphWithCoordinatesLoader(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл для тестирования
        self.file_path = 'test_file.txt'
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write("""Nodes{
город 10 10
деревня 12 4
}
Edges {
город деревня 60
}""")

   # def tearDown(self):
        # Удаляем временный файл после тестирования
       # if os.path.exists(self.file_path):
           # os.remove(self.file_path)

    def test_load_graph(self):
        loader = GraphWithCoordinatesLoader(self.file_path)
        graph = loader.getGraph()
        expected_graph = Graph()
        expected_graph.add_edge(NodeXY("город", 10, 10), NodeXY("деревня", 12, 4),60)
        self.assertEqual(expected_graph,graph)


    def test_load_graphXY(self):
        loader = GraphWithCoordinatesLoader("testXY")
        graph = loader.getGraph()
        expected_graph = Graph()
        node1=NodeXY("A", 100, 200)
        node2=NodeXY("B", 300, 200)
        node3=NodeXY("C", 200, 300)
        expected_graph.add_edge(node1,node2,20)
        expected_graph.add_edge(node3,node2,40)
        expected_graph.add_edge(node2,node3,35)
        self.assertEqual(expected_graph,graph)

if __name__ == '__main__':
    unittest.main()
