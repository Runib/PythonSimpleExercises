import os

def printFilesInCurrentDirectory():
    files = os.listdir(os.curdir)
    print(files)