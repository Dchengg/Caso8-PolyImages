import random

from logic.HtmlWriter import HtmlWriter
from logic.Polygon import Polygon


def create_polygon():
    polygon = Polygon()
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.add_point(random.randint(0, 800), random.randint(0, 800))
    polygon.set_color((random.randint(0,256),random.randint(0,256),random.randint(0,256)))
    return polygon


class Population:
    def __init__(self, mutation_rate, pop_zero, pop_max):
        self.mutation_rate = mutation_rate
        self.pop_zero = pop_zero
        self.pop_max = pop_max
        self.population = []

    def initial_population(self):
        for i in range(0, self.pop_zero):
            self.population.append(create_polygon())

    def view_population(self):
        for individual in self.population:
            HtmlWriter.write_polygon('PolyImage.html', individual)
        HtmlWriter.visualize('PolyImage.html')


    def apply_fitness(self):
        for individual in self.population:
            individual.fitness(237,135,45)

    def natural_selection(self):
        mating_pool = []
        self.population = sorted(self.population, key=lambda x: x.fitness_score, reverse=True)
        for i in range (0,5):
            mating_pool.append(self.population[i])
        del self.population[6 : len(self.population)]
        for i in range(0,10):
            r = random.randint(0,len(mating_pool)-1)
            father = mating_pool[r]
            mother = mating_pool[r]
            baby = Polygon()
            baby.add_point(father.points[0][0], father.points[0][1])
            baby.add_point(mother.points[1][0], mother.points[1][1])
            baby.add_point(mother.points[2][0], mother.points[2][1])
            red = father.color[0]
            green = mother.color[1]
            blue = mother.color[2]
            baby.set_color((red, green, blue))
            self.population.append(baby)

    def mutation(self):
        for individual in self.population:
            individual.mutate(self.mutation_rate)

