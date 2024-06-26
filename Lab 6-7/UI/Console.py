from Domain.MyPoint import Mypoint
from Infrastructure.PointRepository import PointRepo


points = []





def readpoint():
    '''
    Reads a point ( coord_x, coord_y, colour)

    '''
    '''point Coord_X = int(input("X ="))
    point Coord_Y = int(input("Y ="))
    point colour = input("Colour = ")
    p = Mypoint(Coord_X, Coord_Y, colour)
    return p'''
def printpoints():
    '''
    Print all points

    '''
    global points
    for p in points:
        print(p)


def printMenu():
    '''
    Prints a menu with options

    '''
    print("Chose an option:")
    print("1.Add a point")
    print("2.Get all points")
    print("3.Get all points of a given colour")
    print("4.Get all points that are inside a give square")
    print("5.Get the minimum distance between the points")
    print("6.Update a point at given index")
    print("7.Delete a point by index")
    print("8.Delete all points that are inside a given square")
    print("9.Plot all pointsinachart ")

def run():
    '''
    Implements the user interface
    '''

    cont = True
    while cont:
        printMenu()
        opt = input("")
        if opt == "1":
            addPoint()
        if opt == "2":
            getAllPoints()
        if opt == "3":
            getAllPointsOfColour()
        if opt == "4":
            getAllPointsInsideSquare()
        if opt == "5":
            getMinDistance()
        if opt == "6":
            updatePoint()
        if opt == "7":
            deletePointByIndex()
        if opt == "8":
            deletePointsInsideSquare()
        if opt == "9":
            plotAllPoints()
        elif opt == "0":
            print("Good Bye")
            cont = False
        else:
            print("Please give a corect option")







