class Population:
    def __init__(self, individuals):
        self.individuals = individuals

    def genetic_distribution(self):
        for individual in self.individuals:
            distribution = individual.get_map()
            