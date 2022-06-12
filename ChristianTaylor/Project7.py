# Project 7 (Statistics) by Christian Taylor
import math
import statistics

ls = list(map(int, input("Enter an array of numbers: ").strip().split()))

ls.sort()
a = statistics.median(ls)
b = statistics.mode(ls)
c = statistics.mean(ls)

print("The Median of the numbers is: %0.2f" % a)
print("The Mode of the numbers is: %0.2f" % b)
print("The Mean of the numbers is: %0.2f" % c)
