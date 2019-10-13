import random

from Genetic.Point import Point
from Genetic.Polygon import Polygon
from bitstring import BitArray


def Point_in_polygon(point, polygon):
    count = 0
    vertexes = polygon.points
    for i in range(len(vertexes) - 1):
        if ((vertexes[i].y <= point.y) and (vertexes[i + 1].y > point.y)) or (
                (vertexes[i].y > point.y) and (vertexes[i + 1].y <= point.y)):
            vt = (point.y - vertexes[i].y) / (vertexes[i + 1].y - vertexes[i].y)
            if point.x < vertexes[i].x + vt * (vertexes[i + 1].x - vertexes[i].x):
                count += 1
    return count % 2


def crossover(bin1, bin2):
    div = random.randint(0, 15)
    num1 = BitArray(bin1)
    num2 = BitArray(bin2)
    num1 = num1[:div]
    num2 = num2[div:]
    new_num = num1 + num2
    return new_num.bin


class Individual:
    def __init__(self, grid):
        self.grid = grid
        self.distribution = grid.get_map()
        self.sample = grid.sample
        self.polygons = []
        self.pop_size = 0
        self.generation = 0
        self.finished = False
        for number in range(4):
            self.genetic_distribution()
            self.pop_size += 1
        for polygon in self.polygons:
            self.fitness(polygon)

    def genetic_distribution(self):
        adn = random.randint(0, 65535)
        polygon = Polygon(bin(adn))
        self.classify(adn, polygon)
        self.generate_vertixes(polygon)
        self.polygons.append(polygon)

    def generate_vertixes(self, polygon):
        coordinates = self.grid.coordinates
        for i in range(3):
            x = random.randint(coordinates[0], coordinates[2])
            y = random.randint(coordinates[1], coordinates[3])
            polygon.add_point(x, y)

    def classify(self, adn, polygon):
        accumulator = 0
        for color, number in self.distribution.items():
            percentage = number / self.grid.total
            if adn < (65536 * percentage) + accumulator:
                polygon.color = color
                break
            else:
                accumulator += 65536 * percentage

    def get_color_polygons(self, color_target):
        count = 0
        for polygon in self.polygons:
            if polygon.color == color_target:
                count += 1
        return count / len(self.polygons)

    def test_points_on_polygon(self, polygon):
        counter = 0
        pixels = self.sample[polygon.color]
        for pixel in pixels:
            counter += Point_in_polygon(pixel, polygon)
        return counter

    def selection(self):
        mating_pool = []
        self.polygons.sort(key=lambda x: x.fitness_score, reverse=True)
        # int(round(len(self.polygons) * 0.40)
        start = int(round(len(self.polygons) * 0.40))
        for number in range(start):
            mating_pool.append(self.polygons[number])
        del self.polygons[start:len(self.polygons)]
        self.pop_size += 2
        for i in range(self.pop_size - len(self.polygons)):
            r = random.randint(0, len(mating_pool) - 1)
            father = mating_pool[r]
            r = random.randint(0, len(mating_pool) - 1)
            mother = mating_pool[r]
            print("------------------")
            print(father.adn)
            print(mother.adn)
            baby = Polygon(crossover(father.adn, mother.adn))
            self.classify(int(baby.adn, 2), baby)
            self.generate_vertixes(baby)
            self.fitness(baby)
            self.polygons.append(baby)

        self.generation += 1
        self.finished = self.check_if_finished()

    def check_if_finished(self):
        for polygon in self.polygons:
            if polygon.fitness_score < 1:
                return False
        return True

    def fitness(self, polygon):
        inside = self.test_points_on_polygon(polygon)
        color_percentage = self.get_color_polygons(polygon.color)
        score = abs((1 * inside) - (color_percentage / self.distribution[polygon.color]))
        polygon.fitness_score = score


''' polygon = Polygon(101001011) tester de point_in_polygon
polygon.add_point(5, 5)
polygon.add_point(50, 50)
polygon.add_point(100, 30)
point = Point(10, 4)
times = Point_in_polygon(point,polygon)
print(times)'''
