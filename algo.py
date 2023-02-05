# programing assignment cs560 Spring 2019
# Prince Clumson-Eklu

import os  # to interatact with the command line
import sys
import random #For random number generating
from random import randint
from itertools import repeat
import time


# start = time.time()
# a = range(100000)
# b = [i*2 for i in a]
start = time.time()

def inPlaceQuickSort(A,start,end):
    if start<end:
        pivot=randint(start,end)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp

        p=inPlacePartition(A,start,end)
        inPlaceQuickSort(A,start,p-1)
        inPlaceQuickSort(A,p+1,end)

def inPlacePartition(A,start,end):
    pivot=randint(start,end)
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in range(start,end):
        if A[index]<A[end]:#check if current val is less than pivot value
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1


def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res

# Driver Code
Nu = input ("Please enter a number of integer: ")
num = int(Nu)
start = 0
end = 10000
A = []

A = (Rand(start, end, num))
print(A)


start = 0
end = (len(A) - 1)
n = len(A)
# inPlaceQuickSort(A,0,len(A)-1)

# print ("Sorted array is:")
# for i in range(n):
#     print ("%d" %A[i])

with open("output.txt", "a") as f:
        print(A, file=f)
        inPlaceQuickSort(A,0,len(A)-1)
        print ("Sorted array is:", file=f)
        for i in range(n):
            print("%d" %A[i], file=f)


end = time.time()
print(end - start)
# end = time.time()
# print(end - start)
