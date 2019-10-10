import random

from Genetic.Polygon import Polygon


class Individual:
    def __init__(self, grid):
        self.grid = grid
        self.distribution = grid.get_map()
        self.polygons = []
        for number in range(3):
            self.genetic_distribution()
        for polygon in self.polygons:
            self.fitness(polygon)

    def genetic_distribution(self):
        adn = random.randint(0, 65536)
        polygon = Polygon(bin(adn))
        accumulator = 0
        for color, number in self.distribution.items():
            percentage = int(round((number / self.grid.total) * 100))
            if adn < (65536 * (percentage / 100)) + accumulator:
                polygon.color = color
                break
            else:
                accumulator += 65536 * (percentage / 100)
        self.polygons.append(polygon)


    def get_color_polygons(self, color_target):
        count = 0
        for polygon in self.polygons:
            if polygon.color == color_target:
                count += 1
        return count / len(self.polygons)

    def fitness(self, polygon):
        color_percentage = self.get_color_polygons(polygon.color)
        score = abs(1 - (color_percentage / self.distribution[polygon.color]))
        polygon.fitness_score = score
