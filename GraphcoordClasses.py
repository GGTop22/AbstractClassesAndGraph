import random
from abc import ABC, abstractmethod


class CoordinateCalculator(ABC):
    @abstractmethod
    def calculate_coordinates(self, graph):
        raise NotImplementedError("Этот метод должен быть переопределен")

class RandomCoordinateCalculator(CoordinateCalculator):
    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def calculate_coordinates(self, graph):
        coordinates = {}
        for node in graph.keys():
            x = random.randint(20, self.canvas_width - 20)
            y = random.randint(20, self.canvas_height - 20)
            coordinates[node] = (x, y)
        return coordinates

class AutoScalingCoordinateCalculator(CoordinateCalculator):
    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def calculate_coordinates(self, graph):
        coordinates = {}
        min_x = min(node.x for node in graph.keys())
        max_x = max(node.x for node in graph.keys())
        min_y = min(node.y for node in graph.keys())
        max_y = max(node.y for node in graph.keys())

        # Рассчитываем коэффициенты масштабирования
        x_scale = (self.canvas_width - 40) / (max_x - min_x) if max_x - min_x > 0 else 1
        y_scale = (self.canvas_height - 40) / (max_y - min_y) if max_y - min_y > 0 else 1
        scale = min(x_scale, y_scale)

        offset_x = (self.canvas_width - (max_x - min_x) * scale) / 2 - min_x * scale
        offset_y = (self.canvas_height - (max_y - min_y) * scale) / 2 - min_y * scale

        # Рассчитываем координаты с масштабированием
        for node in graph.keys():
            x = node.x * scale + offset_x
            y = node.y * scale + offset_y
            coordinates[node] = (x, y)
        return coordinates
