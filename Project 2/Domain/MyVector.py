#!/usr/bin/env python3

'''

@author:
'''

import numpy as np


class MyVector():

    def __init__(self, name_id, colour, type = 1, values = []):
        '''
               Creates a new instance of MyVector
        '''
        self.__name_id = name_id
        self.__type = 1
        if type < 1:
            raise ValueError("Add a higher number")
        else:
            self.type = type

        colours = ["r", "g", "b", "y", "m"]

        if colour in colours:
            self.__colour = colour

        else:
            raise ValueError("Add a colour only from this list : r, g, b, y, m")

        self.values = values

    def get_id(self):
        '''
        getter method
        return the id of a vector
        '''
        return self.get_id

    def get_colour(self):
        '''
        getter method
        return the colour of a vector
        '''
        return self.__colour

    def get_type(self):
        '''
        getter method
        return the type of a vector
         '''
        return self.__type

    def get_values(self):
        '''
        getter method
        return the values of a vector
         '''
        return self.values

    def set_id(self, id):
        '''
         setter method
         set the id of a vector
         '''
        if id < 0:
            raise ValueError("Add an positive number")
        else:
            self.__id = id

    def set_colour(self, c):
        '''
        setter method
        set the colour of a vector
        '''
        if not c in ("r", "g", "b", "y", "m"):
            raise ValueError("The provided colour is not valid.")
        else:
            self.colour = c

    def set_type(self, t):
        '''
        setter method
        set the type of a vector
        '''
        if t < 1:
            raise ValueError("Introduce a correct type")
        else:
            self.type = t

    def set_values(self, val):
        '''
        setter method
        set the values of a vector
        '''
        if val not in len(val):
            raise ValueError("The value is not in the list")
        else:
            self.val = val

    def __str__(self):
        '''
        provides a string representation of a vector
        returns a string
        '''

        return "The Vector with Name / ID " + str(self.__name_id) + " has the colour " + self.__colour + " , Type " + str(self.__type) + " and values " + str(self.values) + " ."

    def sum_vector(self, vector):
        '''
        returns the sum of vectors
        '''

        return np.sum(vector)


    def prod_vector(self,vector):
        '''
        returns the product of  vectors
        '''

        return np.prod(vector)


    def avarege_vetor(self,vector):
        '''
         returns the averege of  vectors
        '''

        return np.averege(vector)


    def min_vector(self, vector):
        '''
        returns the min of vectors
        '''

        return np.min(vector)

    def max_vector(self, vector):
        '''
        returns the max of vectors
        '''

        return np.max(vector)


'''
vector = [1, 2, 3]

print(np.sum(vector))
print(np.prod(vector))
print(np.average(vector))
'''