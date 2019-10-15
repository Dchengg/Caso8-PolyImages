import random
from Genetic.Polygon import Polygon


def Point_in_polygon(point,
                     polygon):  # Checks if the point is inside a polygon, returns 1 if is inside or 0 if is outside
    count = 0
    vertexes = polygon.points
    for i in range(len(vertexes) - 1):
        if ((vertexes[i].y <= point.y) and (vertexes[i + 1].y > point.y)) or (
                (vertexes[i].y > point.y) and (vertexes[i + 1].y <= point.y)):
            vt = (point.y - vertexes[i].y) / (vertexes[i + 1].y - vertexes[i].y)
            if point.x < vertexes[i].x + vt * (vertexes[i + 1].x - vertexes[i].x):
                count += 1
    return count % 2


def crossover(bin1, bin2):  # Crossover between bits (the color)
    div = random.randint(0, 15)
    num1 = bin1[:div]
    num2 = bin2[div:]
    new_num = num1 + num2
    return new_num





class Individual:
    def __init__(self, grid):
        self.grid = grid
        self.distribution = grid.get_map()  # distribution of colors
        self.sample = grid.sample  # Sample of points to be tested
        self.polygons = []
        self.pop_size = 0
        self.pop_max = 20
        self.finished = False  # Boolean to check if the algorithm has finished
        for number in range(6):  # Creates the generation 0
            self.genetic_distribution()
            self.pop_size += 1
        for polygon in self.polygons:  # Sets the fitness for the gen 0
            self.fitness(polygon)

    def genetic_distribution(
            self):  # Uses the distribution of colors in the grid to set the genetic distribution of the gen 0
        adn = random.randint(0, 65535)
        polygon = Polygon(bin(adn))
        self.classify(adn, polygon)
        self.generate_vertexes(polygon)
        self.polygons.append(polygon)

    def generate_vertexes(self, polygon):  # Generates the vertexes of a polygon within the grid
        coordinates = self.grid.coordinates
        for i in range(3):
            x = random.randint(coordinates[0], coordinates[2])
            y = random.randint(coordinates[1], coordinates[3])
            polygon.add_point(x, y)

    def classify(self, adn, polygon):  # Classifies the color of a polygon usign the genetic distribution method
        accumulator = 0
        for color, number in self.distribution.items():
            percentage = number / self.grid.total
            if adn < (65535 * percentage) + accumulator:
                polygon.color = color
                break
            else:
                accumulator += 65536 * percentage
        polygon.color = color

    def mutation(self, polygon):  # Mutation
        binary = polygon.adn
        prob = random.randint(0, 1000)
        if prob >= 10:
            gen_pos = random.randint(2, len(binary) - 1)
            gen = binary[gen_pos]
            if gen == '1':
                binary = binary[:gen_pos - 1] + '0' + binary[gen_pos:]
            else:
                binary = binary[:gen_pos - 1] + '1' + binary[gen_pos:]
            polygon.adn = binary
            self.classify(int(polygon.adn, 2), polygon)

    def get_color_polygons(self,
                           color_target):  # Gets the the percentage of polygons of a certain color in the population
        count = 0
        for polygon in self.polygons:
            if polygon.color == color_target:
                count += 1
        return count / len(self.polygons)

    def test_points_on_polygon(self, polygon):  # test all the pixels of the same color of the polygon to see if it's inside them
        counter = 0
        pixels = self.sample[polygon.color]
        for pixel in pixels:
            counter += Point_in_polygon(pixel, polygon)
        return counter

    def selection(self):  # Selection of the genetic algorithm
        mating_pool = []
        self.polygons.sort(key=lambda x: x.fitness_score, reverse=True)
        start = int(round(len(self.polygons) * 0.70))
        for number in range(start):
            mating_pool.append(self.polygons[number])
        del self.polygons[start:len(self.polygons)]
        self.finished = self.check_if_finished()
        if self.finished:
            return
        if self.pop_size < self.pop_max:
            self.pop_size += 2
        for i in range(self.pop_size - len(self.polygons)):
            r = random.randint(0, len(mating_pool) - 1)
            father = mating_pool[r]
            r = random.randint(0, len(mating_pool) - 1)
            mother = mating_pool[r]
            baby = Polygon(crossover(father.adn, mother.adn))
            self.classify(int(baby.adn, 2), baby)
            self.generate_vertexes(baby)
            self.fitness(baby)
            self.polygons.append(baby)
        for polygon in self.polygons:
            self.mutation(polygon)

    def check_if_finished(self):  # Checks if the goal has been meet to stop the algorithm
        for polygon in self.polygons:
            if polygon.fitness_score < 1:
                return False
        return True

    def fitness(self, polygon):  # Calculate the fitness of the polygon and assigns it to it
        inside = self.test_points_on_polygon(polygon)
        color_percentage = self.get_color_polygons(polygon.color)
        score = abs((1 * inside) - (color_percentage / self.distribution[polygon.color]))
        polygon.fitness_score = score
