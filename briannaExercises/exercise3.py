# Brianna Albergaria
# Python Exercises

# Python Exercise 3: Recursive Binary Search
# Part A: Randomly generate an array containing 500 elements - make sure
# it's sorted!
# Part B: Implement recursive binary search, returning -1 if the element is not
# found. Use this to search the array in part A for a given element.
# Part C: Measure the time taken of binary search as array sizes increase. How
# does it perform for 2500 elements? 1,250,000?

###############################################################################

import random
import time

###############################################################################

def binarySearch(a, low, high, key):
    mid = int((low+high)/2)
    if low <= high:
        if key == a[mid]:
            return a[mid] # base case
        elif key < a[mid]:
            return binarySearch(a, low, mid-1, key) # search bottom half
        elif key > a[mid]:
            return binarySearch(a, mid+1, high, key) # search top half
    else:
        return -1 # not found
    
###############################################################################

#random.seed(5) # DEBUG

arr = []
arrSize = 1250000

# generate list of random numbers
for i in range(0,arrSize):
    n = random.randint(1,arrSize)
    arr.append(n)

arr.sort()

key = int(input("Please enter the number to search: "))

# tic and toc around function call - timing
tic = time.perf_counter()
found = binarySearch(arr, 0, arrSize, key)
toc = time.perf_counter()

if found == -1:
    print("Number not found in the list.")
else:
    print(f"{found} found in the list.")

print(f"It took {toc-tic:0.6f} seconds to search a list of {arrSize} numbers.")