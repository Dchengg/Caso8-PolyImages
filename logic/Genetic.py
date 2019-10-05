import random

from logic.Polygon import Polygon


def create_polygon():
    polygon = Polygon()
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.set_color('#32A844')
    return polygon


def initial_population(size):
    population = []
    for i in range(0, size):
        population.append(create_polygon())
    return population
