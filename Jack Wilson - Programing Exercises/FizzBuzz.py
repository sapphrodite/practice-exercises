# FizzBuzz (Jack Wilson)
number=int(input('Enter in number to play FizzBuzz: '))
counter=1

while counter<=number:

    if counter%15==0:
        print('Fizz Buzz, ')

    elif counter%5==0:
            print('Buzz, ')

    elif counter%3==0:
           print('Fizz, ')

    else:
        print(f'{counter}, ')
    counter+=1