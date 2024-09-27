import random
from abc import ABC, abstractmethod

from Graph import Graph
from node import Node
from nodeXY import NodeXY


class XYCalculator(ABC):
    @abstractmethod
    def calculate_xy(self, node: Node) -> (float, float):
        raise NotImplementedError("Этот метод должен быть переопределен")


class RandomXYCalculator(XYCalculator):
    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def calculate_xy(self, node: Node) -> (float, float):
        x = random.randint(20, self.canvas_width - 20)
        y = random.randint(20, self.canvas_height - 20)
        return x, y


class SimpleXYCalculator(XYCalculator):
    def calculate_xy(self, node: Node) -> (float, float):
        if isinstance(node, NodeXY):
            return node.x, node.y
        else:
            raise RuntimeError("Неудалосб определить координаты")


class AutoScaleXYCalculator(XYCalculator):
    def __init__(self, canvas_width:float, canvas_height:float,graph:Graph):
        self.graph = graph
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.min_x = min(no.x for no in self.graph.get_all_nodes())
        self.max_x = max(no.x for no in self.graph.get_all_nodes())
        self.min_y = min(no.y for no in self.graph.get_all_nodes())
        self.max_y = max(no.y for no in self.graph.get_all_nodes())

        self.x_scale = (self.canvas_width - 40) / (self.max_x - self.min_x) if self.max_x - self.min_x > 0 else 1
        self.y_scale = (self.canvas_height - 40) / (self.max_y - self.min_y) if self.max_y - self.min_y > 0 else 1

        self.scale_x = self.x_scale
        self.scale_y = self.y_scale

        self.offset_x = (self.canvas_width - (self.max_x - self.min_x) * self.scale_x) / 2 - self.min_x * self.scale_x
        self.offset_y = (self.canvas_height - (self.max_y - self.min_y) * self.scale_y) / 2 - self.min_y * self.scale_y

    def calculate_xy(self, node: Node) -> (float, float):
        x = node.x * self.scale_x + self.offset_x
        y = node.y * self.scale_y + self.offset_y
        return x, y
