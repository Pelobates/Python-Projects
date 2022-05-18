#!/usr/bin/env python3

'''

@author:
'''

from Domain.MyVector import MyVector
from Domain.VectorRepository import VectorRepository
from Validation.Test import int_input


class Menu:
    '''
    the menu class consists of a static list that contains all the menu options
    '''
    menu_options = ["Exist", "Add a vector", "Get all vectors", "Get a vector at a given index",
                    "Update a vector at a given index", "Update a vector identified by name_id",
                    "Delete a vector by index", "Delete a vector by name_id",
                    "Plot all vectors in a chart based on the type and colour of each vector"]


def read_vector():
    '''
    reads a vector of type MyVector and returns it
    '''
    id = input("id = ")
    c = input("colour = ")
    type = int(input("type = "))

    values = []
    vector1 = int(input("First number of vector : "))
    values.append(vector1)
    vector2 = int(input("Second number of vector : "))
    values.append(vector2)
    vector3 = int(input("Third number of vector : "))
    values.append(vector3)

    return MyVector(id, c, type, values)


def print_vector(vectors):
    '''
    prints all the vectors of type MyVector in a given list
    '''
    if len(vectors) == 0:
        print("INFO: There are no vectors.")
    else:
        for e in vectors:
            print(str(e))


def display_menu():
    '''
    clears the console window and displays the user interface
    '''

    for i in range(len(Menu.menu_options)):
        print((" " if i < 10 else "") + str(i) + ". " + Menu.menu_options[i])
    print()


def handle_menu_option(option, repo):
    '''
    handles user input
    '''


    if option == 0:
        print("INFO: Quitting.")
    elif option == 1:
        repo.add_vector(read_vector())
        print("INFO: The vector was added to the repository.")
    elif option == 2:
        print_vector(repo.get_all_vectors())
    elif option == 3:
        print(str(repo.get_vector_at_given_index(int_input("index = "))))
    elif option == 4:
        index = int(input("index = "))
        vector = read_vector()

        print(str(repo.update_vector_at_given_index(index, vector)))

        print("INFO: The vector at the given index was updated.")

    elif option == 5:

        name_id = input("name_id = ")
        vector = read_vector()

        repo.update_vector_by_name_id(name_id, vector)


    elif option == 6:

        index = int(input("index = "))
        repo.delete_vector_index(index)



    elif option == 7:

        name_id = input("name_id = ")
        repo.delete_vector_by_name_id(name_id)


    elif option == 8:
        repo.plot()



def run():
    '''
    implement the user interface
    '''

    repo = VectorRepository()
    v1 = MyVector(1, "r", 2, [1, 2, 3])
    v2 = MyVector(2, "g", 17, [77, 4, 11])
    v3 = MyVector(3, "b", 44, [18, 20, 30])
    v4 = MyVector(4, "y", 8, [0, 10, 20])
    v5 = MyVector(5, "m", 14, [17, 27, 37])
    v6 = MyVector(6, "r", 79, [12, 13, 14])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    repo.add_vector(v4)
    repo.add_vector(v5)
    repo.add_vector(v6)
    option = -1

    while option != 0:
        display_menu()
        option = int_input("Option: ")
        handle_menu_option(option, repo)
