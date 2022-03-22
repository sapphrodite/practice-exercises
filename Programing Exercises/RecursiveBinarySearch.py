from random import random

# binary search function, requires array and element to be sent to it
def bsearch(a,e,low,high):

# loop to binary search current element
    while low<=high:
# sets the middle number between high and low
        mid=low+(high-low)//2
# if the currently searched element is equal to the entered element, return the current mid value
        if a[mid]==a[e]:
               return a[mid]
# If the current searched element value is less than the entered one, add to the lower element
        elif a[mid]<a[e]:
                low=mid+1
# If the current searched element value is greater than the entered one, add to the higher element
        elif a[mid]>a[e]:
                high=mid-1
# return -1 if not found
    return -1

# binary search function, requires array and element to be sent to it
def bsearchr(a,e,low,high):

# loop to binary search current element
    while low<=high:
# sets the middle number between high and low
        mid=low+(high-low)//2
# if the currently searched element is equal to the entered element, return the current mid value
        if a[mid]==a[e]:
               return a[mid]
# If the current searched element value is less than the entered one, add to the lower element
        elif a[mid]<a[e]:
            return bsearchr(a,e,mid+1,high)
# If the current searched element value is greater than the entered one, add to the higher element
        elif a[mid]>a[e]:
                return bsearchr(a,e,low,mid-1)
# return -1 if not found
    else:
     return -1


# Ask user how many elements the array should include
n=int(input('How many array elements would you like?: '))
# multiplies empty array by inputted number to make it the correct size
array=[0]*n
# counter
i=0
# loop that randomizes each array element until reaching size of array
while i<n:
# randomizes current element
    array[i]=random()
# increments counter to next element after randomization
    i+=1
# sorts array from lowest to highest
array.sort()

# another counter
k=0
#Loop that calls binary search function for each element, and prints the result
while k<n:
# calls binary search function and sets to variable, zero is set to the lowest value, and n-1 is set to the high since the array starts at zero
    f=bsearch(array,k,0,n-1)
# prints results
    print(f'Binary search of {k} found {f}')
# increments counter to print next element
    k+=1
# print(f'Binary search of {k} found {f}') (used for testing time)

# Runtime of non-recursive function, 500 elements 0.1 second, 2500: 0.17 seconds, 1250000:27 seconds
# Runtime of recursive function, 500 elements 0.1 second, 2500: 0.20 seconds, 1250000:47 seconds