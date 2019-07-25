# Check if array elements are consecutive | Added Method 3
# Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.
# Examples:
# a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.
#
# b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.
#
# c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.
#
# NO REPEAT d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.

import array

def check_array_consecutive(arr):
    if len(arr) == len(set(arr)):
        for i in range(set(arr)[0])
    for i in set(arr):
        print(i)
    arrset = set(arr)
    print(arrset)
    return False

arr = array.array('i', [5, 2, 3, 1, 4])
print (arr, type(arr))
check_array_consecutive(arr)














def bin2data(a, b):
    sum = {'00':[0,0],
           '01':[1,0],
           '10':[1,0],
           '11':[1,1]}

    print(len(a), len(b))
    exit()

    final = ''

    for i in a:
        for j in b:
            # print(sum[str(i)+str(j)])
            s = str(sum[str(i)+str(j)][0])
            c = str(sum[str(i)+str(j)][1])
            print(s, c)
##!## bin2data("1","1")