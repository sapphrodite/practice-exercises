# Fibonacci implementation (recursively)
import math


def fibon(n1, n2, count):
    while count < N:
        ns = n1 + n2
        n1 = n2
        n2 = ns
        count += 1
        fibon(n1, n2, count)
    return n1


n1 = 0
n2 = 1
count = 1

N = int(input("Enter a value for N: "))
if N <= 0:
    print("N must be > 0")
elif N == 1:
    print("The 1st fibonacci number is: 0")
else:
    result = fibon(n1, n2, count)
    print("The", N, "\bth fibonacci number is: ", result)


"""
The first version (iteratively) has better performance since the runtime is faster.

"""