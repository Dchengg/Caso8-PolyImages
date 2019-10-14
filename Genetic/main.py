from Genetic.Population import Population
from Probabilistic.Imagen import Imagen
import time


def main():
    start_time = time.time()
    im2 = Imagen("cyndaquill2.png")
    print("--- %s seconds ---" % (time.time() - start_time))
    population2 = Population(im2.get_grids())
    population2.genetics()
    print("--- %s seconds ---" % (time.time() - start_time))
    population2.view_population()
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
