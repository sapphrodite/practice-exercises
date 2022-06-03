# Project 4 by Christian Taylor
import math

d = 1
count = 0
n = 0

iter = int(input("Enter the number of iterations: "))

for x in range(1, iter + 1):
    frac = (1 / d)
    n += 1
    if (n % 2) == 0:
        frac *= -1
    count += frac
    d += 2

pi = count * 4
print("The resulting value is equal to: %0.10f" % pi)
