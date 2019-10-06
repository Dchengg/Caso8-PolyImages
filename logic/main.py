from logic.HtmlWriter import HtmlWriter
from logic.Population import Population


def main():
    HtmlWriter.reset_html('PolyImage.html')
    population = Population(0.1, 10, 100)
    population.initial_population()
    print(str(len(population.population)))
    population.view_population()
    #'''
    population.apply_fitness()
    population.natural_selection()
    population.mutation()
    HtmlWriter.reset_html('PolyImage.html')
    print(str(len(population.population)))
    population.view_population()
    #'''

if __name__ == "__main__":
    main()
