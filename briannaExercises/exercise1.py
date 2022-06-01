# Brianna Albergaria
# Python Exercises

# Python Exercise 1: Fibonacci Numbers
# Part A: Implement a function that iteratively calculates the Nth Fibonacci
# number, given an integer N.
# Part B: Re-Implement the function from part A using recursion. Which version 
# has better performance for large values of N? Why?

###############################################################################

# iterative
def fibonacci1(n):
    a = 1
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return a

# recursive
def fibonacci2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

###############################################################################

n = int(input("Please enter a value for N: "))
print("")

print(f"Fibonacci number at N = {n}:")

print(f"Iteratively: {fibonacci1(n)}")

# not super necessary, mostly just for fun
if n > 30:
    print("\nLarge numbers will take a few moments to compute recursively.")
    cmd = input("Are you sure you would like to proceed? (yes/no): ")
    if cmd == "yes":
        print(f"Recursively: {fibonacci2(n)}")
    elif cmd == "no":
        print("Program terminated by user.")
    else:
        print("Unknown command. Terminating program.")