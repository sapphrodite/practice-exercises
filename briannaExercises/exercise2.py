# Brianna Albergaria
# Python Exercises

# Python Exercise 2: FizzBuzz
# Write a function that plays FizzBuzz (https://en.wikipedia
# org/wiki/Fizz_buzz) for the numbers from 1 to N.

###############################################################################

def fizzBuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0: # divisible by both 3 and 5
            print("Fizz Buzz")
        elif i % 3 == 0: # divisible by 3
            print("Fizz")
        elif i % 5 == 0: # divisible by 5
            print("Buzz")
        else:
            print(f"{i}")

###############################################################################

n = int(input("Enter the max value you'd like to FizzBuzz to: "))
fizzBuzz(n)
print("")