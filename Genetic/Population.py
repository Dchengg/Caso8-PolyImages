from FileHandler.HtmlWriter import HtmlWriter
from Genetic.Individual import Individual
import ctypes


class Population:
    def __init__(self, grids, num_population):
        self.individuals = []
        self.generation = 0
        self.num_population = num_population  # Which population is it (according to the image is processing)
        for grid in grids:
            self.individuals.append(Individual(grid))  # Inserts all the grids in the population

    def new_generation(self):  # Creates a new generation of polygons in each grid
        for individual in self.individuals:
            if not individual.finished:
                individual.selection()

    def genetics(self):  # Repeats the process of the genetic algorithm until is has met the goal
        flag = False
        while not flag:
            self.new_generation()
            flag = self.check_finished()
            self.generation += 1

    def check_finished(self):  # Checks if the goal has been met to stop genetics method
        for individual in self.individuals:
            if not individual.finished:
                return False
        return True

    def write_population(self):  # Writes the entire population in the HTML
        polygons = ''
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        for individual in self.individuals:
            for polygon in individual.polygons:
                points = ''
                for point in polygon.points:
                    points = points + str(((screensize[0] / 3) * self.num_population) + (
                                ((screensize[0] * point.x) / 1024) / 3)) + ',' + str(point.y) + ','
                points = points[:-1]
                color = '#%02x%02x%02x' % (polygon.color[0], polygon.color[1], polygon.color[2])
                new_polygon = '\n' + '<polygon points= ' + '"' + points + '" ' + 'style=' + '"fill: ' + color + '"' + '>' + '\n' + '</polygon> '
                polygons = polygons + new_polygon
        HtmlWriter.write_polygon('PolyImage.html', polygons)
