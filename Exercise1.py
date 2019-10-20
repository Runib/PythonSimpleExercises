def printEvenVariables(variables):
    evenVariables =[]
    for num in variables:
        if num % 2 == 0:
            evenVariables.append(num)
        if num == 200:
            break
    print(evenVariables)