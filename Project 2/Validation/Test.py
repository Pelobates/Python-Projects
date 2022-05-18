#!/usr/bin/env python3

'''

@author:
'''


def int_input(prompt, error_message="ERROR: Invalid input (not an integer)"):
    '''
    continuously reads input from the user until a valid integer is given
    '''
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)
            print()


import unittest
from Domain.MyVector import MyVector
from Domain.VectorRepository import VectorRepository
repo = VectorRepository


class MyVectorTest(unittest.TestCase):
    def test_create(self):
        n = MyVector(1, colour = "r", values = [1,2,3,4]),(1, 2 , "m", [1,2,3,4])

        self.assertEqual(n.get_id(), 1)
        self.assertEqual(n.get_type(), 2)
        self.assertEqual(n.get_colour(), "m")
        self.assertEqual(n.get_values(), [1,2,3,4])

        n.set_id(4)
        self.assertEqual(n.get_id(), 4)
        n.set_type(3)
        self.assertEqual(n.get_type(), 3)
        n.set_colour("y")
        self.assertEqual(n.get_colour(), "y")
        n.set_values([7, 10])
        self.assertEqual(n.get_values(), [7, 10])
        try:
            v = MyVector(1, 1, "p", [1, 2])
            self.assertTrue(False)
        except ValueError as e:
            print(e)
            self.assertTrue(False)

        try:
            n.set_Type(-1)
            self.assertTrue(False)
        except ValueError as e:
            print(e)
            self.assertTrue(False)

from Domain.VectorRepository import VectorRepository

class VectorTest(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.__data = []


    def test__addVector(self,):
        repo = VectorRepository()
        m = MyVector(1, 1, "r", [2, 4, 5])
        repo.add_vector(m)
        self.assertTrue(repo.size(), 1)

    def add_at_index(self, index, v, i):
        if 0 <= index < len(self.__data):
            self.__data[i].set_id(v.get_id)
            self.__data[i].set_type(v.get_type())
            self.__data[i].set_colour(v.get_colour())
            self.__data[i].set_values(v.get_values())
        else:
            raise ValueError("The element at the given index does not exists")

'''
    def test__update_at_index(self,):
        m = MyVector(1, 1, "r", [1, 2, 3])
        n = MyVector(3, 2, "m", [5, 6])
        repo.add_vector(m)
        repo.add_vector(n)
        p = MyVector(50, 6, "r", [4, 4, 3])
        var = repo.update_vector_at_given_index(self, 1, p) == self.assertEqual(repo.get_vector_at_given_index(1), p)
        get_id(), p.get_id
        self.assertEqual(repo.get_vector_at_given_index(1))
        get_type(), p.get_type()
        self.assertEqual(repo.get_vector_at_given_index(1))
        get_colour(), p.get_colour()
        self.assertEqual(repo.get_vector_at_given_index(1))
        get_values(), get_values()
        self.assertEqual(repo.get_vector_at_given_index(1))

'''