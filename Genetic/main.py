import time

from Genetic.Population import Population
from Probabilistic.Imagen import Imagen


def main():
    im = Imagen("cyndaquill.png")
    population = Population(im.get_grids())
    polygons = population.individuals[0].polygons
    for p in polygons:
        print("Poligono : ", p.color, "  ADN : ", p.adn, "  Fitness_score : ", p.fitness_score)

    ''' cont = 0
    for i in im.get_grids():
        print(i.get_coordinate())
        print("Probability:", i.probs)
        print(i.get_color())
        print("")
    print("--- %s seconds ---" % (time.time() - start_time))
    '''


if __name__ == "__main__":
    main()
