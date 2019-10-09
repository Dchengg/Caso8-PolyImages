
import math
from colormath.color_objects import XYZColor, sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


class Grid:

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.colors = []
        self.map = dict()
        self.probs = 100
        self.count = 0

    def convert_to_lab(self, colors):
        rgb = sRGBColor(rgb_r=colors[0], rgb_g=colors[1], rgb_b=colors[2], is_upscaled=True)
        xyz = convert_color(rgb, XYZColor)
        lab = convert_color(xyz, LabColor)
        return lab

    def add_color(self, new_color):
        not_similar = False
        if len(self.map) == 0:
            self.count += 1
            self.map[new_color] = 1
        else:
            for k in self.map:
                color1 = self.convert_to_lab(k)
                color2 = self.convert_to_lab(new_color)
                delta_e = delta_e_cie2000(color1, color2)
                if delta_e < 20:
                    not_similar = False
                    self.count += 1
                    self.map[k] += 1
                    break
                else:
                    not_similar = True
            if not_similar:
                self.count += 1
                self.map[new_color] = 1

    def reduce_probability(self):
        self.probs -= 20

    def get_map(self):
        return self.map

    def get_color(self):
        print("Total:", self.count)
        for i in self.map:
            percentage = int(round((self.map[i] / self.count) * 100))
            print("Percentage of", i, ":", percentage)
        return self.map

    def get_total(self):
        return self.count

    def get_coordinate(self):
        return self.coordinates

    def get_probability(self):
        return self.probs
