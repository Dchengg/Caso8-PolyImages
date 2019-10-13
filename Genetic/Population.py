import random

from Genetic.Individual import Individual
from Genetic.Polygon import Polygon


class Population:
    def __init__(self, grids):
        self.individuals = []
        for grid in grids:
            self.individuals.append(Individual(grid))

    def new_generation(self):
        for individual in self.individuals:
            if not individual.finished:
                individual.selection()

    def genetics(self):
        flag = False
        while not flag:
            self.new_generation()
            flag = self.check_finished()

    def check_finished(self):
        for individual in self.individuals:
            if not individual.finished:
                return False
        return True
