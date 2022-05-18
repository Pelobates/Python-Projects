#!/usr/bin/env python3

'''

@author:
'''

import matplotlib as plt
from Domain.MyVector import MyVector


class VectorRepository:
    def __init__(self):
        self.__data = []


    def add_vector(self, v):
        '''
        Adds a vector to the Repository
        '''
        self.__data.append(v)


    def get_all_vectors(self):
        '''
        Gets all vectors from the Repository
        '''
        return self.__data

    def get_vector_at_given_index(self, index):
        '''
        Gets all vectors at a given index
        '''
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("There is no vector corresponding to the given index.")

        return self.__data[index]

    def update_vector_at_given_index(self, index, vector):
        '''
        Updates all vectors at a given index
        '''
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("There is no vector corresponding to the given index.")

        self.__data[index] = vector

    def delete_vector_index(self, index):
        '''
        Delets all vectors at a given index
        '''
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("There is no vector corresponding to the given index.")

        del self.__data[index]

    def delete_vector_by_name_id(self, name_id):
        '''
         Delets a vector by a given name_id
        '''

        aux = 0

        for elem in self.__data:
            if elem.get_id() == name_id:
                del self.__data[aux]

            aux = aux + 1

    def update_vector_by_name_id(self, name_id, vector):
        '''
         Delets a vector by a given name_id
        '''

        aux = 0

        for elem in self.__data:
            if elem.get_id() == name_id:
                self.__data[aux] = vector

            aux = aux + 1

    def size(self):
        '''
        Gets the size
        '''
        return self.__data





    def plot(self):
        '''
        Plots all points in a chart
        '''

        t = []
        u = []
        v = []
        m = []
        j1 = j2 = j3 = j4 = 1
        for i in range(len(self.__data)):
            if self.__data[i].get_type() == 1:
                t.append(1)
                m.append("o")
            if self.__data[i].get_type() == 2:
                t.append(2)
                m.append("s")
            if self.__data[i].get_type() == 3:
                t.append(3)
                m.append("^")
            if self.__data[i].get_type() >= 4:
                t.append(4)
                m.append("D")
        for i in range(len(self.__data)):
            if t[i] == 1:
                u.append(j1)
                j1 = j1 + 1
            if t[i] == 2:
                u.append(j2)
                j2 = j2 + 1
            if t[i] == 3:
                u.append(j3)
                j3 = j3 + 1
            if t[i] == 4:
                u.append(j4)
                j4 = j4 + 1
            v.append(self.__data[i].get_colour())
        for i in range(len(self.__data)):
            plt.scatter(t[i], u[i], c=v[i], marker=m[i])
        plt.show()

