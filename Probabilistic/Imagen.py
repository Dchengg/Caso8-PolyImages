from PIL import Image
import random
from Grid import Grid
import time


class Imagen:
    def __init__(self, filename):
        try:
            self.image = Image.open(filename)
            self.colors = []
            self.width, self.height = self.image.size
            self.grids = []
            self.percentage = 0
            self.iterate_image()

        except FileNotFoundError:
            print("Invalid value")

    def iterate_image(self):
        x_squares = self.width // 8
        y_squares = self.height // 8

        width_subsquare = self.width // 8
        height_subsquare = self.width // 8

        count_x = 1
        self.percentage = int(round(((width_subsquare * height_subsquare) / 100) * 40))

        for x_tiles in range(8):
            count_y = 1

            x2 = x_squares * count_x

            for y_tiles in range(8):
                x1 = x_tiles * width_subsquare
                y1 = y_tiles * height_subsquare

                y2 = y_squares * count_y
                box = (x1, y1, x2, y2)

                self.background(box)

                count_y += 1
            count_x += 1

        self.set_colors()

    def background(self, box):
        total_alpha = 0

        x1 = box[0]
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]

        red, green, blue, alpha = self.image.getpixel((x1, y1))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x2-1, y2-1))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x1, y2-1))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x2-1, y1))
        total_alpha += alpha

        red, green, blue, alpha = self.image.getpixel((x1, y1))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x2//2, y2//2))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x1, y2//2))
        total_alpha += alpha
        red, green, blue, alpha = self.image.getpixel((x2//2, y1))
        total_alpha += alpha

        avg_alpha = int(round(total_alpha / 8))

        if avg_alpha != 0:
            self.grids.append(box)

    def get_grids(self):
        return self.grids

    def set_colors(self):
        for i in self.grids:
            grid = Grid(i)
            x1 = i[0]
            y1 = i[1]
            x2 = i[2]
            y2 = i[3]

            # region = self.image.crop(i)
            # region.show()

            for number in range(self.percentage):
                pixel1 = random.randint(x1, x2 - 1)
                pixel2 = random.randint(y1, y2 - 1)
                red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))

                if red > 60 and green > 60 and blue > 60:
                    color = red, green, blue
                    grid.add_color(color)


start_time = time.time()
im = Imagen("cyndaquill.png")
print("--- %s seconds ---" % (time.time() - start_time))

"""
    def set_colors(self):
        for i in self.grids:
            print(i)
            total_r = 0
            total_g = 0
            total_b = 0

            x1 = i[0]
            y1 = i[1]
            x2 = i[2]
            y2 = i[3]

            for number in range(self.percentage):
                pixel1 = random.randint(x1, x2 - 1)
                pixel2 = random.randint(y1, y2 - 1)
                red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))

                if alpha != 0:
                    total_r += red
                    total_g += green
                    total_b += blue

            avg_red = int(round(total_r / self.percentage))
            avg_green = int(round(total_g / self.percentage))
            avg_blue = int(round(total_b / self.percentage))

            if avg_red != 0 and avg_green != 0 and avg_blue != 0:
                color = (avg_red, avg_green, avg_blue)
                grid = Grid(color, i)
                # self.grids.append(grid)
"""

"""
total_alpha = 0

        x1 = box[0]
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]

        for i in range(y1, y2 - 1):
            pixel1 = x1
            pixel2 = i
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
            # print(pixel1, pixel2)
            total_alpha += alpha

        for i in range(y1, y2 - 1):
            pixel1 = x2 - 1
            pixel2 = i
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
            # print(pixel1, pixel2)
            total_alpha += alpha

        for i in range(x1, x2 - 1):
            pixel1 = i
            pixel2 = y1
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
            # print(pixel1, pixel2)
            total_alpha += alpha

        for i in range(x1, x2 - 1):
            pixel1 = i
            pixel2 = y2 - 1
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
            # print(pixel1, pixel2)
            total_alpha += alpha

        avg_alpha = int(round(total_alpha / self.percentage))
        # print("Avg alpha:", avg_alpha)

        if avg_alpha != 0:
            self.grids.append(box)
"""