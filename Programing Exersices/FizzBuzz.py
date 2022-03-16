# FizzBuzz
# Takes user's input to play FizzBuzz
n=int(input('Enter in number to play FizzBuzz: '))
# Counter that represents numbers divisible by the inputted number
i=1
# Runs through each number to see its divisibility, and prints the result
while i<=n:
# if the current iteration is divisible by 15 print fizz buzz
    if i%15==0:
        print('Fizz Buzz, ')
# increases counter for next iteration
        i+=1
# if the current iteration is divisible by 5 print fizz buzz
    elif i%5==0:
            print('Buzz, ')
# increases counter for next iteration
            i+=1
# if the current iteration is divisible by 3 print fizz buzz
    elif i%3==0:
           print('Fizz, ')
# increases counter for next iteration
           i+=1
# if not divisible by 3,5, or 15, print the current number
    else:
        print(f'{i}, ')
# increases counter for next iteration
        i+=1