def DaysBetweenDAtes(firstDate, secondDate):
    try:
        return abs((firstDate-secondDate).days)
    except:
        print("Date with bad values")