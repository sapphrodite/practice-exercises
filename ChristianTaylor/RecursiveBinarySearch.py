# Recursive Binary Search
import random
import time  # for part c

start = time.time()  # This is used for Part C

"""Part A"""
x = 0
array = []

while x < 1250000:  # For Part A, this number is 500, For Part C this number is 2500 & 1,250,000
    array.append(random.randrange(1, 1000))
    x += 1

array.sort()
# print(len(array))  #For testing
# print(array) #For testing

"""Part B"""


def binsearch(array, ele, f, l):  # f = first, l = last
    if l >= f:
        mid = f + (l - f) // 2

        if array[mid] == ele:
            print("Element is at index %d" % mid)
        elif array[mid] < ele:
            binsearch(array, ele, mid + 1, l)
        elif array[mid] > ele:
            binsearch(array, ele, f, mid - 1)
    else:
        print("-1")


ele = int(input("Enter an element: "))
binsearch(array, ele, 0, len(array) - 1)

"""Part C"""
# The array size above is changed to 2500 and 1,250,000
end = time.time()
print("The runtime of the program is :", end - start)

""" 
Results for Part C:
After testing multiple searches I found that the runtimes are roughly the same.
For compile time it was instant for 2500 elements.
But for 1,250,000 elements the compile time was about two seconds.
"""