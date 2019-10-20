def dict_depth(myDictionary):
    if isinstance(myDictionary, dict):
        return 1 + (max(map(dict_depth, myDictionary.values())) if myDictionary else 0)
    return 0