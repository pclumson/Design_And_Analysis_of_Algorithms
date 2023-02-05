import random 
from random import randint
# This is quicksort partition function


# def partition(a, p, r):
#     x = a[r - 1]
#     i = p - 1
#     for k in range(p, r - 1):
#         if a[k] < x:
#             i += 1
#             a[i], a[k] = a[k], a[i]
#     i += 1
#     a[i], a[r - 1] = a[r - 1], a[i]
#     j = i
#     for k in range(i + 1, r):
#         if a[k] == x:
#             j += 1
#             a[j], a[k] = a[k], a[j]
#         k -= 1
#     return (i + j) // 2


# quicksort modified to sort for non increasing order

# def partition(a, p, r):
#     x = a[r - 1]
#     i = p - 1
#     for j in range(p, r - 1):
#         if a[j] >= x:
#             i += 1
#             a[i], a[j] = a[j], a[i]
#     i += 1
#     a[i], a[r - 1] = a[r - 1], a[i]
#     return i
# def quicksort(a, p, r):
#     if p < r - 1:
#         q = partition(a, p, r)
#         quicksort(a, p, q)
#         quicksort(a, q + 1, r)

#quicksort with equal element values

# def partition(a, p, r):
#     x = a[r - 1]
#     i = p - 1
#     for k in range(p, r - 1):
#         if a[k] < x:
#             i += 1
#             a[i], a[k] = a[k], a[i]
#     i += 1
#     a[i], a[r - 1] = a[r - 1], a[i]
#     j = i
#     for k in range(i + 1, r):
#         if a[k] == x:
#             j += 1
#             a[j], a[k] = a[k], a[j]
#         k -= 1
#     return i, j

# randomized quicksort

def partition(a, p, r):
    x = a[r - 1]
    i = p - 1
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    j = i
    for k in range(i + 1, r):
        if a[k] == x:
            j += 1
            a[j], a[k] = a[k], a[j]
        k -= 1
    return i, j

def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)

def quicksort(a, p, r):
    while p < r - 1:
        q, t = randomized_partition(a, p, r)
        if q - p < r - t:
            quicksort(a, p, q)
            p = t + 1
        else:
            quicksort(a, t + 1, r)
            r = q


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


#with fixed pivot
# def quicksortfixedpivot(arr): # with fixed index
#     if (len(arr) <= 1):
#         return arr
#     else:
#         grt_arr = []
#         less_arr = []
#         pivot = arr[0] # picking up a fixed 0 index
#         for ele in arr[1:]:
#             if (ele <= pivot):
#                 less_arr.append(ele)
#             elif (ele > pivot):
#                 grt_arr.append(ele)

#     return quicksortfixedpivot(less_arr)+[pivot]+quicksortfixedpivot(grt_arr)

# create a list of random numbers
# arr1 = (random.sample(range(0,10000000),1000000))

# # running time 
# %%time
# out1 = (quicksort(arr1))

# %%time
# out2 = (quicksortfixedpivot(arr1))