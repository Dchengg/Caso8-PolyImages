
from colormath.color_objects import XYZColor, sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

from Genetic.Point import Point


class Grid:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.colors = []
        self.map = dict()
        self.sample = dict()
        self.probs = 100
        self.total = 0

    # Utiliza varias fucniones matemáticas para determinar qué tan parecidos son dos RGBA
    def convert_to_lab(self, colors):
        rgb = sRGBColor(rgb_r=colors[0], rgb_g=colors[1], rgb_b=colors[2], is_upscaled=True)
        xyz = convert_color(rgb, XYZColor)
        lab = convert_color(xyz, LabColor)
        return lab

    # Verifica si el color que entra como parámetro es similar a alguno que ya se haya analizado en el cuadrante
    def add_color(self, new_color, x, y):
        not_similar = False             # Bool que se mantiene falso a ser que el pixel sea diferente de todos los demás
        if len(self.map) == 0:          # Primera iteración, para cuando la lista esté vacía
            self.total += 1             # Contador que sirve para llevar el totoal de pixel analizados
            self.map[new_color] = 1     # Información del pixel se guarda en un diccionario
            self.sample[new_color] = []
            self.sample[new_color].append(Point(x, y))
        else:
            for current_color in self.map:
                color1 = self.convert_to_lab(current_color)     # Pasa de RGBA a lab
                color2 = self.convert_to_lab(new_color)         # Para de RGBA a lab
                delta_e = delta_e_cie2000(color1, color2)       # Se usa para determinar la diferencia
                if delta_e < 30:                                # En caso que los colores sean vagamente parecidos
                    not_similar = False
                    self.total += 1
                    self.map[current_color] += 1
                    if len(self.sample[current_color]) <= 10:
                        self.sample[current_color].append(Point(x, y))
                    break
                else:
                    not_similar = True
            if not_similar:
                self.total += 1
                self.map[new_color] = 1
                self.sample[new_color] = []
                self.sample[new_color].append(Point(x, y))

    def reduce_probability(self):
        self.probs -= 20

    def get_map(self):
        return self.map

    def get_color(self):
        print("Total:", self.total)
        for i in self.map:
            percentage = int(round((self.map[i] / self.total) * 100))
            print("Percentage of", i, ":", percentage)
        return self.map

    def get_total(self):
        return self.total

    def get_coordinate(self):
        return self.coordinates

    def get_probability(self):
        return self.probs
