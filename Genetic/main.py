from Genetic.Population import Population
from Probabilistic.Imagen import Imagen
from FileHandler.HtmlWriter import HtmlWriter
import time


def main():
    HtmlWriter.reset_html('PolyImage.html')
    start_time = time.time()
    im = Imagen("cyndaquill2.png")
    print("--- %s seconds ---" % (time.time() - start_time))
    population = Population(im.get_grids(), 0)
    population.genetics()
    print(population.generation)
    population.view_population()
    print("--- %s seconds ---" % (time.time() - start_time))
    im2 = Imagen("bicho.png")
    print("--- %s seconds ---" % (time.time() - start_time))
    population2 = Population(im2.get_grids(), 1)
    population2.genetics()
    print(population2.generation)
    print("--- %s seconds ---" % (time.time() - start_time))
    population2.view_population()
    print("--- %s seconds ---" % (time.time() - start_time))
    im3 = Imagen("earth2.png")
    print("--- %s seconds ---" % (time.time() - start_time))
    population3 = Population(im3.get_grids(), 2)
    population3.genetics()
    print(population3.generation)
    population3.view_population()
    HtmlWriter.visualize('PolyImage.html')
    print("--- %s seconds ---" % (time.time() - start_time))

    '''population.tester()
    polygons = population.individuals[0].polygons
    for p in polygons:
        print("Poligono : ", p.color, "  ADN : ", p.adn, "  Fitness_score : ", p.fitness_score)'''

    ''' cont = 0
    for i in im.get_grids():
        print(i.get_coordinate())
        print("Probability:", i.probs)
        print(i.get_color())
        print("")
    print("--- %s seconds ---" % (time.time() - start_time))
    '''


main()
