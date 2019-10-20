def CheckString(stringToCheck):
    try:
        if stringToCheck[:2].lower() is not "is":
            return "Is" + stringToCheck
    except:
        print("Bad string values")