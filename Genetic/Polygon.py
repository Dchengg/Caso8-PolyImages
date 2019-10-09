class Polygon:
    def __init__(self, adn):
        self.points = []
        self.color = (0, 0, 0)
        self.adn = adn
        self.fitness_score = 0

    def add_point(self, x, y):
        pair = (x, y)
        self.points.append(pair)

    def set_color(self, color):
        self.color = color
