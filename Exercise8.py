import collections
import pprint

def countCharacters(FileName):
    file_input = input(FileName)
    with open(file_input, 'r') as info:
      count = collections.Counter(info.read().upper())
      value = pprint.pformat(count)
    print(value)