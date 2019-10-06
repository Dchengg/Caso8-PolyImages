from logic.HtmlWriter import HtmlWriter
from logic.Population import Population


def main():
    HtmlWriter.reset_html('PolyImage.html')
    population = Population(0.2, 20, 100)
    population.initial_population()

    while not population.finished:

        print(str(len(population.population)))
        population.apply_fitness()
        population.natural_selection()
        population.mutation()


    population.view_population()

if __name__ == "__main__":
    main()
