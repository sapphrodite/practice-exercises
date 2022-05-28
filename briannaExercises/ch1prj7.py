# Brianna Albergaria
# Python Exercises

# Statisticians would like to have a set of functions to compute the median and
# mode of a list of numbers. The median is the number that would appear at the
# midpoint of a list if it were sorted. The mode is the number that appears most
# frequently in the list. Define these functions in a module named stats.py. Also
# include a function named mean, which computes the average of a set of numbers.
# Each function expects a list of numbers as an argument and returns a single
# number.

###############################################################################

"""Functions to find mean, median, and mode."""

def mean(a):
    """Returns the mean of a given list, a."""
    return sum(a)/len(a) # average is the sum/length of list

def median(a):
    """Returns the median of a given list, a."""
    a.sort() # sort list
    if len(a) % 2 == 0: # check if even number sized list
        return a[int(len(a)/2)] # if even, median is length/2
    else:
        return a[int(len(a)/2)+1] # if odd, median is length/2 + 1

def mode(a):
    """Returns the mode of a given list, a."""
    a.sort() # sort list
    count = 1 # start counter variable at 1
    prevHighest = 0 # initialize previous highest count variable
    modeList = [] # initialize empty list to store the mode(s)
    # using list instead of int variable in case there are multiple values with the same value

    for i in range(0,len(a)-1): # loop to iterate through list
        if a[i+1] == a[i]: # check if next number is same as current
            count += 1 # if True, increment counter
        else:
            count = 1 # if False, reset counter to 1

        if count > prevHighest: # check for new mode
            modeList.clear() # if True, clear the list of old mode(s)
            modeList.append(a[i]) # append new mode to the mode list
            prevHighest = count # set the current count as the previous highest count
        elif count == prevHighest: # check for multiple modes
            modeList.append(a[i]) # if True, append it to the mode list

    return modeList # return the whole mode list

"""Program"""

a = [1,2,3,3,3,4,4,4,5,6] # initialize arbitrary list

print(f"The mean is {mean(a)}.")
print(f"The median is {median(a)}.")
print(f"The mode(s) is(are) {mode(a)}.")