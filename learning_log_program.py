# This is my learning tracking program.
import datetime
import os
import time

lists = {}


def courses_in():  # updates the database with today's learnt items
    print("Type exit when done")
    x = ""
    while x != "exit":
        x = input("Add entries to the learning database > ").lower()
        if x == "exit":
            break
        lists[x] = time_func()
    return lists


def show_courses():
    if os.name == 'nt':
        os.system("cls")  # windows compatibility
    else:
        os.system("clear")  # linux compatibility

    print("List of items learnt today:")
    for x, y in lists.items():
        strings = "\t" + x + " @ " + str(y) + "\n"
        print(strings)
        file_create(strings)


def time_func():
    time_now = datetime.datetime.now()
    return time_now


def file_create(log):
    f = open("learningdb.log", "a")
    f.write(log)
    f.close()
    print("Insertion successful! :)")

    g = open("learningdb.log", "r")
    print(g.read())
    g.close()
    time.sleep(3)


courses_in()
show_courses()
