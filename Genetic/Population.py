import random

from Genetic.Polygon import Polygon


class Population:
    def __init__(self, individuals):
        self.individuals = individuals

    def genetic_distribution(self, individual):
        distribution = individual.get_map()
        adn = random.randint(0, 65536)
        polygon = Polygon(bin(adn))

        accumulator = 0
        print(distribution)
        for color, number in distribution.items():
            percentage = int(round((number / individual.total) * 100))
            if adn < (65536 * (percentage / 100)) + accumulator:
                print(65536 *(percentage / 100) + accumulator)
                polygon.color = color
                break
            else:
                accumulator += 65536 * (percentage / 100)
        return polygon