import random
class Polygon:
    def __init__(self):
        self.points = []
        self.color = (0, 0, 0)
        self.fitness_score = 0

    def add_point(self, x, y):
        pair = (x, y)
        self.points.append(pair)

    def set_color(self, color):
        self.color = color

    def fitness(self, target_r, target_g, target_b):
        #score = ((self.color[0] / target_r) * (self.color[1] / target_g) * (self.color[2] / target_b))
        delta_red = self.color[0] - target_r
        delta_green = self.color[1] - target_g
        delta_blue = self.color[2] - target_b
        self.fitness_score = 100 - ((abs(delta_red + delta_green + delta_blue))/3)
        print('red : ' + str(self.color[0]))
        print('green : ' + str(self.color[1]))
        print('blue : ' + str(self.color[2]))
        print('score : ' + str(self.fitness_score))
        return self.fitness_score

    def mutate(self, mutation_percentage):
        if random.uniform(0.0, 1.0) < mutation_percentage:
            red = self.color[0] + random.randint(1, 20)
            green = self.color[1] + random.randint(1, 20)
            blue = self.color[2] + random.randint(1, 20)
            self.color = (red, green, blue)