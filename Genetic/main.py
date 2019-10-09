import time

from Genetic.Population import Population
from Probabilistic.Imagen import Imagen


def main():
    #start_time = time.time()
    im = Imagen("earth.png")
    population = Population(im.get_grids())
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
