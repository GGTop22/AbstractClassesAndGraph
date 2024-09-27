import unittest
import os

from Graph import Graph
from Loader import GraphFileLoader


class TestFileLoader(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл для тестирования
        self.file_path = 'test_file.txt'
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write('x y 12\nx z 5\nz y 6\n')

    def tearDown(self):
        # Удаляем временный файл после тестирования
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_successful_load(self):
        loader = GraphFileLoader(self.file_path)
        data = loader.getGraph()
        self.assertEqual("Graph({Node(x): {Node(y): 12.0, Node(z): 5.0}, Node(y): {}, Node(z): {Node(y): 6.0}})", str(data))

    def test_file_not_found(self):
        loader = GraphFileLoader('non_existent_file.txt')
        data = loader.getGraph()
        self.assertEqual(data,Graph())

        #loader = FileLoader(empty_file_path)
        #data = loader.load()
        #self.assertEqual(data, [])

        #os.remove(empty_file_path)

if __name__ == '__main__':
    unittest.main()
