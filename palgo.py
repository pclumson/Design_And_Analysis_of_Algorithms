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

# orig = sys.stdout
# with open("output.txt", "wb") as f:
#     sys.stdout = f
#     try:
#         execfile("palgo.py", {})
#     finally:
#         sys.stdout = orig

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
#print(Rand(start, end, num))
A = (Rand(start, end, num))
print(A)


# A = [4,5,7,4,3,6,0,4,22,45,82]
# f = open("output.txt", "w+")

start = 0
end = (len(A) - 1)
n = len(A)
inPlaceQuickSort(A,0,len(A)-1)

print ("Sorted array is:")
for i in range(n):
    print ("%d" %A[i])

# f.write(A[i].str(strip))

# f.close()
#
# def fileManager(filename):
#
#     with open(sys.argv[1]) as f:
#
#         for line in f:
#
#             a = line.split()
#
#             for i in a:
#                 if a[0] in  "+-*/^":
#                     ans = postfixEval(prefixToPostfix(line))
#                     print((ans))
#                     break
#                 else:
#                     postfixEval(line)
#                     ans = postfixEval(line)
#                     print((ans))
#                     break
#
#
# fileManager(sys.argv[1])

# def Rand(start, end, num):
#     res = []
#     for j in range(num):
#         res.append(random.randint(start, end))
#     return res
#
# # Driver Code
# Nu = input ("Please enter a number of integer: ")
# num = int(Nu)
# start = 0
# end = 10000
# alist = []
# #print(Rand(start, end, num))
# alist = (Rand(start, end, num))
# print(alist)

#quicksort with random pivot

# def quicksort(arr): # with random index
#     if (len(arr) <= 1):
#         return arr
#     else:
#         grt_arr = []
#         less_arr = []
#         rand_indx = random.randint(0,len(arr)-1)
#         pivot = arr[rand_indx] # picking up a random index
#         #for ele in arr[1:]:
#         for ele in (arr[0:rand_indx]+arr[rand_indx+1:]):
#             if (ele <= pivot):
#                 less_arr.append(ele)
#             elif (ele > pivot):
#                 grt_arr.append(ele)

#     return quicksort(less_arr)+[pivot]+quicksort(grt_arr)



# end = time.time()
# print(end - start)
