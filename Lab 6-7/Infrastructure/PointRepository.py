
'''class PointRepository:
    def __init__(self):
        self.data = []

    def getPointRepo(self):
        return self.data

    def addPoint(self, Mypoint):
        self.data.append(Mypoint)

    def DeletePoint(self,p, poz):
        p.pop(poz)
        return p'''



import math

import matplotlib.pyplot as plt


class PointRepo:
    # my_list = []

    def _str_(self):
        """
        A function that prints a string with the details about my point
        Output : The string
        """
        res = ""
        for elem in self.my_list:
            res += "Point (" + str(elem.coord_x) + ", " + str(elem.coord_y) + ") of colour " + elem.colour + ".\n"
        return res

    def _init_(self, my_list):
        self.my_list = my_list

    def addPoint(self, point):
        '''
        Add a new point in the list
        '''
        self.my_list.append(point)

    def getAllPoints(self):
        '''
        Get all points from the repository
        '''
        return self.my_list

    def pointAtIndex(self, i):
        '''
        Get a point at a given index
        '''
        return self.my_list[i]

    def getAllPointsOfColour(self, colour):
        '''
        Get all points of a given colour
        '''
        l = []
        for elem in self.my_list:
            if elem.getcolour() == colour:
                l.append(elem)
        return l

    def getAllPointsInsideSquare(self, corner, length):
        '''
        Get all points that are inside a given square
        '''
        l = []
        for elem in self.my_list:
            if corner.get_x() <= elem.get_x() <= corner.get_x() + length and corner.get_y() - length <= elem.get_y() <= corner.get_y():
                l.append(elem)
        return l

    def getMinDistance(self, p1, p2):
        '''
        Get the minimum distance between two points
        '''
        return math.sqrt((p2.get_x() - p1.get_x())**2 + (p2.get_y() - p1.get_y())**2)

    def updatePoint(self, a, b, colour, i):
        '''
        Update a points at a given index
        '''
        self.my_list[i].set_x(a)
        self.my_list[i].set_y(b)
        self.my_list[i].set_colour(colour)

    def deletePointByIndex(self, i):
        '''
        Delete a point by index
        '''
        del (self.my_list[i])

    def deletePointsInsideSquare(self, corner, length):
        '''
        Delete all points that are inside a given square
        '''
        for elem in self.my_list():
            if corner.get_x() <= elem.get_x() <= corner.get_x() + length and corner.get_y() - length <= elem.get_y() <= corner.get_y():
                self.my_list.remove(elem)

    def plotAllPoints(self):
        '''
        Plot all points in a chart ( using library matplotlib )
        '''
        x_list = []
        y_list = []
        colour_list = []
        for elem in self.my_list:
            x_list.append(elem.get_x())
            y_list.append(elem.get_y())
            colour_list.append(elem.get_colour())


x = [1, 2, 3]
y = [1, 2, 3]
col = ["red", "green", "blue"]
plt.scatter(x, y, c=col)
plt.show()



