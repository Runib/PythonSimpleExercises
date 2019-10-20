import string

def ChangeString(theString):
    substring = "not poor"
    if substring in theString:
        theString.replace(substring, "good")
    return theString