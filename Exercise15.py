def CheckIfContainsSublist(mainList):
    for var in mainList:
        if var is list:
            return True

    return False