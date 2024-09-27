import abc
from abc import ABC
from Graph import Graph, Path, Node


class Path_Finder(ABC):
    @abc.abstractmethod
    def getPath(self, graph: Graph, start: Node, end: Node) -> Path:
        pass
