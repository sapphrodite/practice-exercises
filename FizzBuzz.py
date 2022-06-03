# FizzBuzz Implementation by Christian Taylor
import math

print("This program will play FizzBuzz from the numbers 1 to N")
N = int(input("Enter a value for N: "))
print("The result is: ")

for x in range(1, N+1):
    if x % 15 == 0:
        print("Fizz Buzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print("%d" % x)



