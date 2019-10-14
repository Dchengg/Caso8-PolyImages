from FileHandler.HtmlWriter import HtmlWriter
from Genetic.Individual import Individual
import ctypes



class Population:
    def __init__(self, grids, num_population):
        self.individuals = []
        self.generation = 0
        self.num_population = num_population
        self.htmlString = ''
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
            self.generation += 1
            #self.update_gen(self.generation)

    def update_gen(self, gen_number):
        self.htmlString = self.htmlString + '\n' + "<gen" + str(gen_number)+">"
        for individual in self.individuals:
            for polygon in individual.polygons:
                points = ''
                for point in polygon.points:
                    points = points + str(point.x) + ',' + str(point.y) + ','
                color = '#%02x%02x%02x' % (polygon.color[0], polygon.color[1], polygon.color[2])
                new_polygon = '\n' + '<polygon points= ' + '"' + points + '" ' + 'style=' + '"fill: ' + color + '"' + '>' + '\n' + '</polygon> '
                self.htmlString = self.htmlString + new_polygon
        self.htmlString = self.htmlString + '\n' + "</gen" + str(gen_number) + ">"


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
        polygons = ''
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(screensize)
        for individual in self.individuals:
            for polygon in individual.polygons:
                points = ''
                for point in polygon.points:
                    points = points + str( ((screensize[0]/3)*self.num_population ) + (((screensize[0]*point.x)/1024)/3)) + ',' + str(point.y) + ','
                color = '#%02x%02x%02x' % (polygon.color[0], polygon.color[1], polygon.color[2])
                new_polygon = '\n' + '<polygon points= ' + '"' + points + '" ' + 'style=' + '"fill: ' + color + '"' + '>' + '\n' + '</polygon> '
                polygons = polygons + new_polygon
        HtmlWriter.write_polygon('PolyImage.html', polygons)
        #HtmlWriter.write_polygon('PolyImageAnimated.html', self.htmlString)

