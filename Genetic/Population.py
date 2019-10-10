import random

from Genetic.Individual import Individual
from Genetic.Polygon import Polygon


class Population:
    def __init__(self, grids):
        self.individuals = []
        for grid in grids:
            self.individuals.append(Individual(grid))
