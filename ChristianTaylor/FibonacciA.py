# Fibonacci implementation (iteratively)

import math
count = 1
n1 = 0
n2 = 1

N = int(input("Enter a value for N: "))
if N <= 0:
    print("N must be > 0")
    exit()

print("The", N, "\bth Fibonacci Number is: ")

if N == 1:
    print(n1)
elif N != 1:
    while count < N:
        ns = n1 + n2
        n1 = n2
        n2 = ns
        count += 1
    print(n1)


