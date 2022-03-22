# find the fibonacci series (Jack Wilson)
from cmath import sqrt
from re import I

# function to calculate fibonacci series
def fib(n):
# counter that is used to calculate each fibonacci number
  i=2
# total of each iteration of fibonaccci numbers, gets added to each to be returned from the function
  temp=0
# Holds n-1 of the current iteration to calculate the total
  temp1=0
# Holds n-2 of the current iteration to calculate the total
  temp2=1
# if the fibonacci number is one, return one to prevent negative number
  if n==1:
    return 1
# Each fibonacci number is calculated until it reaches the inputted number
  while i<= n:
# Calculates current iteration to be eventually returned to main function when condition is met
      temp=temp1+temp2
# sets lower limit to the current upper limit for next iteration
      temp1=temp2
# sets upper limit to the current calculated fibonacci number to use in next iteration
      temp2=temp
# increases counter to keep loop claculating until condition is met
      i=i+1
# returns calculated fibonacci number to main function
  return temp

# function to calculate fibonacci series recursively
def fibrecursive(n):
# if the fibonacci number is zero, return zero to prevent negative number
    if n==0:
        return 0
# if the fibonacci number is one, return one to prevent negative number
    elif n==1:
      return 1
# recursive call to equation to calculate fibonacci number
    return fibrecursive(n-1) + fibrecursive(n-2)

# sets the value to be calculated from user input
value=int(input('Enter number to calculate fibonaci series: '))
# calls function to calculate inputted number
fn1=fib(value)
# calls function to calculate inputted number recursively
fn2=fibrecursive(value)
# prints calculated response
print(f'The calculated fibonacci series for {value} is {fn1}')
print(f'The fibonacci series calculated recursively is {fn2}')