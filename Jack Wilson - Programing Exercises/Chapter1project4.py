# Jack Wilson Chapter 1, Project 4
# aproximates value of pi based on number of iterations
def piaprox(iterations):
    pitotal=1
    denominator=-3
    counter=0
    while counter<iterations:
        pitotal+=(1/denominator)
        if denominator<0:
            denominator=(denominator-2)*-1
            counter+=1
        else:
            denominator=(denominator+2)*-1
            counter+=1

    return (4*pitotal)


iterate=int(input('Enter in the number of iterations you would like to aproximate pi: '))
total=piaprox(iterate)
print(f'The approximation of pi in {iterate} iterations is {total}')