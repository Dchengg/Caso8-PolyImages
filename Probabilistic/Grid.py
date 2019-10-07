
import math
from colormath.color_objects import XYZColor, sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


class Grid:
    """
    def __init__(self, colors, coordinates):
        self.colors = colors
        self.average_colors = []
        self.coordinates = coordinates
    """
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.colors = []

    def convert_to_lab(self, colors):
        rgb = sRGBColor(rgb_r=colors[0], rgb_g=colors[1], rgb_b=colors[2], is_upscaled=True)
        xyz = convert_color(rgb, XYZColor)
        lab = convert_color(xyz, LabColor)
        return lab

    def add_color(self, new_color):
        not_similar = False
        if len(self.colors) == 0:
            self.colors.append(new_color)
        else:
            for i in self.colors:
                color1 = self.convert_to_lab(i)
                color2 = self.convert_to_lab(new_color)
                delta_e = delta_e_cie2000(color1, color2)
                if delta_e < 20:
                    not_similar = False
                    break
                else:
                    not_similar = True
            if not_similar:
                self.colors.append(new_color)

    def get_color(self):
        return self.colors
    
    def get_coordinate(self):
        return self.coordinates