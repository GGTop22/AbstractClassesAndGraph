import abc
from abc import ABC
from Graph import Graph
from node import Node


class GraphLoader(ABC):
    @abc.abstractmethod
    def getGraph(self) -> Graph:
        pass


class GraphFileLoader(GraphLoader):
    def __init__(self, file_path:str):
        self.file_path = file_path

    def getGraph(self) -> Graph:
        g = Graph()
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = file.readlines()
            for line in data:
                # Вытащить из строки Node откуда,Node куда и стоимость
                sFrom, sToo, sPrice = line.split()
                nFrom, nToo, fPrice = Node(sFrom), Node(sToo), float(sPrice)
                # Вызвать метод добовления edge для g

                g.add_edge(nFrom, nToo, fPrice)



        except FileNotFoundError:
            print(f"File at path {self.file_path} not found.")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
        return g
