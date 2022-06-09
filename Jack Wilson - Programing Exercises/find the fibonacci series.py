# find the fibonacci series (Jack Wilson)
def fib(number):
  counter=2
  total=0
  lowerLimit=0
  upperLimit=1
  if number==1:
    return 1
  while counter<= number:
      total=lowerLimit+upperLimit
      lowerLimit=upperLimit
      upperLimit=total
      counter= counter+1
  return total


def fibrecursive(number):
    if number==0:
        return 0
    elif number==1:
      return 1
    return fibrecursive(number-1) + fibrecursive(number-2)


value=int(input('Enter number to calculate fibonaci series: '))
fibonacci=fib(value)
fibonacciRecursive=fibrecursive(value)
print(f'The calculated fibonacci series for {value} is {fibonacci}')
print(f'The fibonacci series calculated recursively is {fibonacciRecursive}')