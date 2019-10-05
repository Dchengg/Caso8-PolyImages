
class Grid:
    def __init__(self, color, coordinates):
        self.color = color
        self.coordinates = coordinates

        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]
        
    def get_color(self):
        return self.color
    
    def get_coordinate(self):
        return self.coordinates

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

