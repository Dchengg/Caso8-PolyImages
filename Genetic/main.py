from Genetic.Population import Population
from Probabilistic.Imagen import Imagen
from FileHandler.HtmlWriter import HtmlWriter
import time


def main():
    HtmlWriter.reset_html('PolyImage.html')  # Resets html for the new images
    start_time = time.time()
    im = Imagen("cyndaquill.png")  # Sets the first image and gets data with probabilistic algorithm
    population = Population(im.get_grids(), 0)  # Sets the population of grids for the image
    population.genetics()  # starts the genetic algorithm for the image
    print("Total de generaciones de la primera imagen : ", population.generation)
    population.write_population()  # Writes in the HTML the polygons of each grid
    im2 = Imagen("earth.png")  # Repeats the process with the second image
    population2 = Population(im2.get_grids(), 1)
    population2.genetics()
    print("Total de generaciones de la segunda imagen : ", population2.generation)
    population2.write_population()
    im3 = Imagen("mudkip.png")  # Repeats the process with the second image
    population3 = Population(im3.get_grids(), 2)
    population3.genetics()
    print("Total de generaciones de la tercera imagen : ", population3.generation)
    population3.write_population()
    HtmlWriter.visualize('PolyImage.html')  # Sends the HTML to the browser to be view
    print("Tiempo de ejecución del programa : ", "%s seconds" % (time.time() - start_time)) # Returns the execution time of the program


main()
