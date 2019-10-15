from Genetic.Point import Point


class Polygon:
    def __init__(self, adn):
        self.points = []
        self.color = (0, 0, 0)
        self.adn = adn  # The adn or binary genotype of the polygon
        self.fitness_score = 0

    def add_point(self, x, y):  # adds a vertex to the polygon
        point = Point(x, y)
        self.points.append(point)

    def set_color(self, color):
        self.color = color
