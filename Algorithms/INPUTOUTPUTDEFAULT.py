import os 
from collections import defaultdict

    

def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    listOfArrays = []
    firstLineSkip = True
    for x in numInput:
        if firstLineSkip:
            firstLineSkip = False
            continue
        listOfArrays.append(x.split())
    


    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    #filewrite.write(str(x1))


if __name__== "__main__":
  main()