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

import stats # import stats.py module

a = [1,2,3,3,3,4,4,4,5,6] # initialize arbitrary list

print(f"The mean is {stats.mean(a)}.")
print(f"The median is {stats.median(a)}.")
print(f"The mode(s) is(are) {stats.mode(a)}.")