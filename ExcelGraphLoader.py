
import pandas as pd
from Graph import Graph
from Loader import GraphLoader
from node import Node

class ExcelGraphLoader(GraphLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def getGraph(self) -> Graph:
        df = pd.read_excel(self.file_path)
        graph = Graph()

        for i, row in df.iterrows():
            from_node = Node(row['from'])
            to_node = Node(row['to'])
            weight = row['weight']
            graph.add_edge(from_node, to_node, weight)

        return graph

