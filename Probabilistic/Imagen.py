from PIL import Image
import random
from Grid import Grid


class Imagen:
    def __init__(self, filename):
        try:
            self.image = Image.open(filename)
            self.image = self.image.convert('RGB')
            self.width, self.height = self.image.size
            self.coordinates = []

            self.iterate_image()

        except FileNotFoundError:
            print("Invalid value")

    def is_background(self, percentage, x1, x2, y1, y2, box):

        total_r = 0
        total_g = 0
        total_b = 0

        for number in range(percentage):
            pixel1 = random.randint(x1, x2 - 1)
            pixel2 = random.randint(y1, y2 - 1)
            red, green, blue = self.image.getpixel((pixel1, pixel2))
            total_r += red
            total_g += green
            total_b += blue

        avg_red = int(round(total_r / percentage))
        avg_green = int(round(total_g / percentage))
        avg_blue = int(round(total_b / percentage))

        if avg_red != 0 and avg_green != 0 and avg_blue != 0:
            color = (avg_red, avg_green, avg_blue)
            cuadrante = Grid(color, box)
            self.coordinates.append(cuadrante)
            print("Average of", box, "=", avg_red, avg_green, avg_blue)


    def iterate_image(self):
        x_squares = self.width // 16
        y_squares = self.height // 16

        width_subsquare = self.width // 16
        height_subsquare = self.width // 16

        count_x = 1
        percentage = int(round(((width_subsquare * height_subsquare) / 100) * 40))

        for x_tiles in range(16):
            count_y = 1

            x2 = x_squares * count_x

            for y_tiles in range(16):
                x1 = x_tiles * width_subsquare
                y1 = y_tiles * height_subsquare

                y2 = y_squares * count_y
                box = (x1, y1, x2, y2)

                self.is_background(percentage, x1, x2, y1, y2, box)

                count_y += 1
            count_x += 1




im = Imagen("cyndaquill.png")
print("Meow")