from random import random

# binary search function, requires array and element to be sent to it
def binarysearch(array,element,low,high):

    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==array[element]:
               return array[mid]
        elif array[mid]<array[element]:
                low=mid+1
        elif array[mid]>array[element]:
                high=mid-1
    return -1


# binary search function, requires array and element to be sent to it
def binarysearchrecursive(array,element,low,high):

    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==array[element]:
               return array[mid]
        elif array[mid]<array[element]:
            return binarysearchrecursive(array,element,mid+1,high)
        elif array[mid]>array[element]:
                return binarysearchrecursive(array,element,low,mid-1)
    else:
     return -1


n=int(input('How many array elements would you like?: '))
array=[0]*n
i=0
while i<n:
    array[i]=random()
    i+=1
array.sort()

k=0
while k<n:
    f=binarysearch(array,k,0,n-1)
    print(f'Binary search of {k} found {f}')
    k+=1
# print(f'Binary search of {k} found {f}') (used for testing time)

# Runtime of non-recursive function, 500 elements 0.1 second, 2500: 0.17 seconds, 1250000:27 seconds
# Runtime of recursive function, 500 elements 0.1 second, 2500: 0.20 seconds, 1250000:47 seconds