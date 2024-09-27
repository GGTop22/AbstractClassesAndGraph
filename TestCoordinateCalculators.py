import unittest

from GraphcoordClasses import RandomCoordinateCalculator, AutoScalingCoordinateCalculator
from node import Node


class TestCoordinateCalculators(unittest.TestCase):

    def test_random_coordinate_calculator(self):
        graph = {Node("A"): [], Node("B"): []}
        calculator = RandomCoordinateCalculator(600, 400)
        coordinates = calculator.calculate_coordinates(graph)

        self.assertEqual(len(coordinates), 2)
        for node, (x, y) in coordinates.items():
            self.assertTrue(20 <= x <= 580)
            self.assertTrue(20 <= y <= 380)


if __name__ == '__main__':
    unittest.main()
