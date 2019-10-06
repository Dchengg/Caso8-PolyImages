
class Grid:
    def __init__(self, color, coordinates):
        self.color = color
        self.average_colors = []
        self.coordinates = coordinates
        
    def get_color(self):
        return self.color
    
    def get_coordinate(self):
        return self.coordinates

    def add_color_list(self, color):
        self.average_colors.append(color)