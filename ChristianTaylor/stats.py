# Project 7 (Statistics) by Christian Taylor
import math
import statistics


def median(n):
    """Returns the median of a list of numbers."""
    n.sort()
    print("The Sorted array is:", n)
    return statistics.median(n)


def mode(n):
    """Returns the mode of a list of numbers."""
    return statistics.mode(n)


def mean(n):
    """Returns the mean of a list of numbers."""
    result = math.fsum(n) / len(n)
    # Could also use statistics.mean(n)
    return result


"""User input for array"""
l = list(map(int, input("Enter an array of numbers: ").strip().split()))

"""Compute results"""
a = median(l)
b = mode(l)
c = mean(l)

"""Print results"""
print("The Median of the numbers is: %0.2f" % a)
print("The Mode of the numbers is: %0.2f" % b)
print("The Mean of the numbers is: %0.2f" % c)
