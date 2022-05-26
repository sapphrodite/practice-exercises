# FizzBuzz Implementation by Christian Taylor
import math

"""Intro"""
print("This program will play FizzBuzz from the numbers 1 to N")

"""User input"""
N = int(input("Enter a value for N: "))


"""Complies results and appends results to listfb"""
listfb = []
for x in range(1, N+1):
    if (x/15).is_integer() == True:
        listfb.append("Fizz Buzz,")
    elif (x/5).is_integer() == True:
        listfb.append("Buzz,") 
    elif (x/3).is_integer() == True:
        listfb.append("Fizz,") 
    else:
        listfb.append("%d," % x)
        
"""Print results"""
print("The result is: ")
for x in range(0, len(listfb), 10):
    print(*listfb[x:x+10])



