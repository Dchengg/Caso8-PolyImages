import time

from Genetic.Population import Population
from Probabilistic.Imagen import Imagen


def main():
    im = Imagen("cyndaquill.png")
    population = Population(im.get_grids())
    first_grid = population.individuals[0]
    print(first_grid.get_color())
    for i in range(30):
        polygon = population.genetic_distribution(first_grid)
        print("Poligono : ", polygon.color, "  ADN : " , polygon.adn)
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
