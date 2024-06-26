

class Mypoint:
    def __init__(self, x, y, colour = ""):
        self.coord_x = x
        self.coord_y = y
        self.colour = colour
    def getCoordX(self):
        return self.coord_x

    def getCoordY(self):
        return self.coord_y

    def getColour(self):
        return self.colour

    def setCoordX(self, x):
        self.coord_x = x

    def setCoordy(self, y):
        self.coord_y = y

    def setColour(self, colour = ""):
        self.colour = colour

    def __str__(self):
        print("Point", str(self.getCoordX())+"," +str(self.getCoordY()), "of colour", self.getColour())


