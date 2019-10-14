from PIL import Image
import random

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
            self.r, self.g, self.b, self.a = red, green, blue, alpha = self.image.getpixel((0, 0))
            print(red, green, blue, alpha)
            if alpha == 0:
                self.background = False
            else:
                self.background = True
            self.iterate_image()

        except FileNotFoundError:
            print("Invalid value")

    def iterate_image(self):
        # Tiles es la cantidad de cuadrantes por cada eje. La cantidad de cuadrantes en la imagen es este al cuadrado
        # Conforma más grande sea tiles, más pequeños van a ser los cuadrantes
        tiles = 64
        x_squares = self.width // tiles
        y_squares = self.height // tiles

        width_subsquare = self.width // tiles
        height_subsquare = self.width // tiles

        self.percentage = int(round(((width_subsquare * height_subsquare) / 100) * 5))          # Porcentaje que se usa para sacar probabilidad del fondo
        self.percentage_color = int(round(((width_subsquare * height_subsquare) / 100) * 10))   # Porcentaje que se usa para sacar probabilidad de colores

        count_x = 1         # Se inicia el contador en 1 porque sino el primer cuadrante no haría nada

        for x_tiles in range(tiles):                # Itera por cada cuadrante de tiles de alto
            count_y = 1     # Igual que count_x

            x2 = x_squares * count_x                # x de la esquina inferior izquierda
            for y_tiles in range(tiles):            # Itera por cada cuadrante de tiles de ancho
                x1 = x_tiles * width_subsquare      # x de la esquina superior derecha
                y1 = y_tiles * height_subsquare     # y de la esquina superior derecha
                y2 = y_squares * count_y            # y de la esquina inferior izquierda
                box = (x1, y1, x2, y2)              # Se hace una tupla de cuatro números para crear un cuadrante lógico
                grid = Grid(box)                    # Crea un nuevo objeto tipo Grid
                self.grids.append(grid)             # Agrega a una lista que tiene todos los cuadrantes lógicos
                count_y += 1                        # Le incrementa al contador de y para mover las esquinas del eje
            count_x += 1                            # Le incrementa el contador para mover esquinas del eje

        if not self.background:
            self.remove_transparent_background()                    # Método probabilísitco que se encarga de remover el fondo
        else:
            self.remove_white_background()

    def remove_transparent_background(self):
        for attempts in range(0, 20):                       # Se hace 20 veces para asegurar que remueva todos los cuadrantes que no tengan imagen
            for grid in self.grids:                         # Itera sobre cada cuadrante lógico de la imagen
                probability = random.randint(1, 100)        # Random que indica si se analiza el cuadrante
                if probability <= grid.get_probability():   # Si random es igual que probabilidad restante del cuadrante
                    if not self.analyze_transparent_grid(grid):         # Si lo que se analiza no tiene color, reduce la probabilidad del cuadrante
                        grid.reduce_probability()           # Llama método que reduce score del cuadrante
        self.set_colors()                                   # Guarda "top" de colores del cuadrante

    def remove_white_background(self):
        for attempts in range(0, 20):                       # Se hace 20 veces para asegurar que remueva todos los cuadrantes que no tengan imagen
            for grid in self.grids:                         # Itera sobre cada cuadrante lógico de la imagen
                probability = random.randint(1, 100)        # Random que indica si se analiza el cuadrante
                if probability <= grid.get_probability():   # Si random es igual que probabilidad restante del cuadrante
                    if not self.analyze_white_grid(grid):         # Si lo que se analiza no tiene color, reduce la probabilidad del cuadrante
                        grid.reduce_probability()           # Llama método que reduce score del cuadrante
        self.set_colors()

    def analyze_transparent_grid(self, Grid):
        grid = Grid.get_coordinate()

        # Agarra las posiciones respectivas de la tupla de coordenadas
        x1 = grid[0]
        y1 = grid[1]
        x2 = grid[2]
        y2 = grid[3]

        # For crea un pixel dentro del cuadrante lógico de forma aleatoria
        for number in range(self.percentage):
            pixelx = random.randint(x1, x2 - 1)
            pixely = random.randint(y1, y2 - 1)
            red, green, blue, alpha = self.image.getpixel((pixelx, pixely))

            if red != 0 or green != 0 or blue != 0:
                return True     # Retorna True si al menos un RGB da un color

        return False    # Retorna False si todos los RGB son negros o no tienen fondo

    def analyze_white_grid(self, Grid):
        grid = Grid.get_coordinate()

        # Agarra las posiciones respectivas de la tupla de coordenadas
        x1 = grid[0]
        y1 = grid[1]
        x2 = grid[2]
        y2 = grid[3]

        # For crea un pixel dentro del cuadrante lógico de forma aleatoria
        for number in range(self.percentage):
            pixelx = random.randint(x1, x2 - 1)
            pixely = random.randint(y1, y2 - 1)
            red, green, blue, alpha = self.image.getpixel((pixelx, pixely))

            if red != self.r or green != self.g or blue != self.b:
                return True  # Retorna True si al menos un RGB da un color diferente a blanco

        return False  # Retorna False si todos los RGB son blancos, osea, es fondo

    def set_colors(self):
        for i in self.grids:
            if i.get_probability() > 20:    # Si un cuadrante tiene 20% de probabilidad o menos de NO contener imagen, se ignora
                grid = i.get_coordinate()

                # Agarra las posiciones respectivas de la tupla de coordenadas
                x1 = grid[0]
                y1 = grid[1]
                x2 = grid[2]
                y2 = grid[3]

                for number in range(self.percentage_color):
                    pixelx = random.randint(x1, x2 - 1)
                    pixely = random.randint(y1, y2 - 1)
                    red, green, blue, alpha = self.image.getpixel((pixelx, pixely))

                    # If se asegura que no agarre pixeles que sean transparentes
                    if alpha != 0 or (red < 250 and green < 250 and blue < 250):
                        color = red, green, blue
                        i.add_color(color, pixelx, pixely)

    def get_grids(self):
        for grid in self.grids:                     # Itera sobre cada grid lógico de la imagen
            if grid.get_total() > 0:                # Agarra cuadrantes que tengan al menos un color
                self.image_colors.append(grid)         # Mete en una lista que tiene únicamente cuadrantes con color
        return self.image_colors                    # Retorna lista con cuadrantes que contienen colores
