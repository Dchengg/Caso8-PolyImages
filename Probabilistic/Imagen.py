from PIL import Image
import random
from Grid import Grid


class Imagen:
    def __init__(self, filename):
        try:
            self.image = Image.open(filename)
            print(self.image.mode)
            # self.image = self.image.convert('RGB')
            self.width, self.height = self.image.size

            self.coordinates = []
            self.edges = []

            self.iterate_image()

        except FileNotFoundError:
            print("Invalid value")

    def iterate_image(self):
        x_squares = self.width // 8
        y_squares = self.height // 8

        width_subsquare = self.width // 8
        height_subsquare = self.width // 8

        count_x = 1
        percentage = int(round(((width_subsquare * height_subsquare) / 100) * 40))

        for x_tiles in range(8):
            count_y = 1

            x2 = x_squares * count_x

            for y_tiles in range(8):
                x1 = x_tiles * width_subsquare
                y1 = y_tiles * height_subsquare

                y2 = y_squares * count_y
                box = (x1, y1, x2, y2)

                self.is_background(percentage, box)

                count_y += 1
            count_x += 1

    def is_background(self, percentage, box):
        total_r = 0
        total_g = 0
        total_b = 0

        x1 = box[0]
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]

        for number in range(percentage):
            pixel1 = random.randint(x1, x2 - 1)
            pixel2 = random.randint(y1, y2 - 1)
            red, green, blue, alpha = self.image.getpixel((pixel1, pixel2))
            if alpha != 0:
                total_r += red
                total_g += green
                total_b += blue

        avg_red = int(round(total_r / percentage))
        avg_green = int(round(total_g / percentage))
        avg_blue = int(round(total_b / percentage))

        if avg_red != 0 and avg_green != 0 and avg_blue != 0:
            color = (avg_red, avg_green, avg_blue)
            grid = Grid(color, box)
            self.coordinates.append(grid)
            # region = self.image.crop(grid.get_coordinate())
            # region.show()

    def get_coordinates(self):
        return self.coordinates


im = Imagen("cyndaquill.png")

coordinates = im.get_coordinates()
for i in coordinates:
    print("Average of", i.get_coordinate(), "is", i.get_color())
    # region = im.crop(i.get_coordinate())
    # region.show()

