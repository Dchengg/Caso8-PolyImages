import random

from Genetic.HtmlWriter import HtmlWriter
from Genetic.Individual import Individual
from xml.sax import saxutils as su
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

    def tester(self):
        while not self.individuals[0].finished:
            if not self.individuals[0].finished:
                self.individuals[0].selection()
                print(self.individuals[0].finished)
                polygons = self.individuals[0].polygons
                for p in polygons:
                    print("Poligono : ", p.color, "  ADN : ", p.adn, "  Fitness_score : ", p.fitness_score)

    def view_population(self):
        HtmlWriter.reset_html('PolyImage.html')
        polygons = ''
        for individual in self.individuals:
            for polygon in individual.polygons:
                points = ''
                for point in polygon.points:
                    points = points + str(point.x) + ',' + str(point.y) + ','
                color = '#%02x%02x%02x' % (polygon.color[0], polygon.color[1], polygon.color[2])
                new_polygon = '\n' + '<polygon points= ' + '"' + points + '" ' + 'style=' + '"fill: ' + color + '"' + '>' + '\n' + '</polygon> '
                polygons = polygons + new_polygon
        print(polygons)
        # polygons = su.unescape(polygons)
        HtmlWriter.write_polygon('PolyImage.html', polygons)
        HtmlWriter.visualize('PolyImage.html')
