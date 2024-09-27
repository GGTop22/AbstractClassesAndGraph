import pandas as pd
import unittest
from tempfile import NamedTemporaryFile
from node import Node
from ExcelGraphLoader import ExcelGraphLoader

# Тест для ExcelGraphLoader
class TestExcelGraphLoader(unittest.TestCase):
    def setUp(self):
        # Создание временного Excel файла с тестовыми данными
        self.test_data = pd.DataFrame({
            'from': ['A', 'B', 'C'],
            'to': ['B', 'C', 'A'],
            'weight': [1, 2, 3]
        })




    def test_load_graph(self):
        loader = ExcelGraphLoader(self.temp_file.name)
        graph = loader.getGraph()

        # Проверка узлов и рёбер
        self.assertTrue(graph.has_node(Node('A')))
        self.assertTrue(graph.has_node(Node('B')))
        self.assertTrue(graph.has_node(Node('C')))

        self.assertTrue(graph.has_edge(Node('A'), Node('B')))
        self.assertTrue(graph.has_edge(Node('B'), Node('C')))
        self.assertTrue(graph.has_edge(Node('C'), Node('A')))

        self.assertEqual(graph.get_edge_weight(Node('A'), Node('B')), 1)
        self.assertEqual(graph.get_edge_weight(Node('B'), Node('C')), 2)
        self.assertEqual(graph.get_edge_weight(Node('C'), Node('A')), 3)

if __name__ == '__main__':
    unittest.main()
