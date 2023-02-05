# programing assignment cs560 Spring 2019
# Prince Clumson-Eklu

import os  # to interatact with the command line
import random #For random number generating
import time
from itertools import repeat
#start = time.time()


# this helper function will check for integer value for 2.b
def checkInt():
    Nu = input ("Please enter the number of integer: ")

    try:
        N = int(Nu)
        print("you have entered :", N)
        for x in range (N):
            print(random.randint(0, 10000))
    except ValueError:
        print("your input is not an interger")
        checkInt()
start = time.time()
a = range(100000)
b = [i*2 for i in a]
checkInt()

# def generateRamdom():
#     checkInt()
#     for x in range (N):
#         print (random.randint(0, N))
#
# generateRamdom(N)

#"the code you want to test stays here"
end = time.time()
print(end - start)


    # import time
    # start = time.time()
    # a = range(100000)
    # b = [i*2 for i in a]
    # end = time.time()
    # print(end - start)
