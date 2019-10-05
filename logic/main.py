from logic.HtmlWriter import HtmlWriter
import logic.Genetic as genetic


def main():
    population = genetic.initial_population(3)
    for i in range(0, 3):
        HtmlWriter.write_polygon("PolyImage.html", population[i])
    HtmlWriter.visualize("PolyImage.html")


if __name__ == "__main__":
    main()
