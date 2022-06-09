# Jack Wilson Chapter 1, Project 7
def median(enteredList):
    enteredList.sort()
    length=len(enteredList)
    if length%2==0:
        halfLength=int((length)/2)
        return (enteredList[halfLength]+enteredList[halfLength-1])/2
    else:
        halfLength=int((length)/2)
        return enteredList[halfLength]


def mode(enteredList):
    enteredList.sort()
    previousElement=None
    currentElement=0
    initialTotal=0
    currentTotal=0

    for element in enteredList:
        currentElement=element
        if currentElement == previousElement:
            for item in enteredList:
                if item==currentElement:
                    currentTotal+=1
            if currentTotal>initialTotal:
                initialTotal=currentTotal
                finalElement=element
        currentTotal=0
        previousElement=element

    return finalElement


def mean(enteredList):
    length=len(enteredList)
    total=0
    counter=0
    while counter<length:
        total+=enteredList[counter]
        counter+=1
    return total/length


testList=[1,1,78,98,3,45,89,45,45]
print(f'Median: {median(testList)}')
print(f'Mode: {mode(testList)}')
print(f'Mean: {mean(testList)}')