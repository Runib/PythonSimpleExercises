import operator

def SortDictionaryByValue(myDictionary):

    sorted_ascending = sorted(myDictionary.items(), key=operator.itemgetter(0))
    sorted_descending = dict( sorted(myDictionary.items(), key=operator.itemgetter(0),reverse=True))

    return sorted_ascending, sorted_descending