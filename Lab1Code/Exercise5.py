def InputNumber():
    return input("Put your number here: ")

def ValidationNumber(number):
    try:
        intNumber = int(number)
        return intNumber
    except:
        print("Put number!")
        return -1

def CheckOddOrEven(validNumber):
    if validNumber % 2 == 0:
        print("It is even number")
    else:
        print("It is odd number")

def UserInput():
    userNumber = InputNumber()
    while(1):
        validNumber = ValidationNumber(userNumber)
        if validNumber != -1:
            break
    CheckOddOrEven(validNumber)