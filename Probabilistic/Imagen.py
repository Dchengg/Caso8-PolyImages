from PIL import Image
import random

import time

from Probabilistic.Grid import Grid


class Imagen:
    def __init__(self, filename):
        try:
            self.image = Image.open(filename)
            self.width, self.height = self.image.size
            self.grids = []
            self.image_colors = []
            self.percentage = 0
            self.percentage_color = 0
            self.iterate_image()

        except FileNotFoundError:
            print("Invalid value")

    def iterate_image(self):
        tiles = 32
        x_squares = self.width // tiles
        y_squares = self.height // tiles

        width_subsquare = self.width // tiles
        height_subsquare = self.width // tiles

        count_x = 1
        self.percentage = int(round(((width_subsquare * height_subsquare) / 100) * 5))
        self.percentage_color = int(round(((width_subsquare * height_subsquare) / 100) * 20))

        for x_tiles in range(tiles):
            count_y = 1
            x2 = x_squares * count_x
            for y_tiles in range(tiles):
                x1 = x_tiles * width_subsquare
                y1 = y_tiles * height_subsquare
                y2 = y_squares * count_y
                box = (x1, y1, x2, y2)
                grid = Grid(box)

                self.grids.append(grid)

                count_y += 1
            count_x += 1
        self.function()

    def function(self):
        for i in range(0, 20):
            for grid in self.grids:
                probability = random.randint(1, 100)
                if probability <= grid.get_probability():
                    if not self.analyze_grid(grid):
                        grid.reduce_probability()
        self.set_colors()

    def analyze_grid(self, Grid):
        grid = Grid.get_coordinate()

        x1 = grid[0]
        y1 = grid[1]
        x2 = grid[2]
        y2 = grid[3]

        total_red = 0
        total_green = 0
        total_blue = 0

        for number in range(self.percentage):
            pixel1 = random.randint(x1, x2 - 1)
            pixel2 = random.randint(y1, y2 - 1)
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))

            total_red += red
            total_green += green
            total_blue += blue

        if total_red != 0 and total_green != 0 and total_blue != 0:
            return True
        else:
            return False

    def get_grids(self):
        for i in self.grids:
            if i.get_total() > 20:
                self.image_colors.append(i)
        return self.image_colors

    def set_colors(self):
        for i in self.grids:
            if i.get_probability() > 0:
                grid = i.get_coordinate()

                x1 = grid[0]
                y1 = grid[1]
                x2 = grid[2]
                y2 = grid[3]

                for number in range(self.percentage_color):
                    pixel1 = random.randint(x1, x2 - 1)
                    pixel2 = random.randint(y1, y2 - 1)
                    red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
                    if (red > 60 and green > 60 and blue > 60) and (red < 240 and green < 240 and blue < 240):
                        color = red, green, blue
                        i.add_color(color)
