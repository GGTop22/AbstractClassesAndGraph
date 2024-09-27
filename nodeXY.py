from node import Node


class NodeXY(Node):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name)
        self.x = x
        self.y = y


    def __repr__(self):
        return f"NodeXY({self.name},{self.x},{self.y})"
