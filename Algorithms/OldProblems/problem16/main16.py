import os 
from collections import defaultdict

    

def morethanndivtwo(array):
    di = defaultdict(int)

    for num in array:
        if di.get(num) == None:
            di[num] = 1
        else:
            di[num] = di.get(num) + 1

    for key in di:
        if di.get(key) > len(array) / 2:
            return key

    return -1
    #print(di)

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
    
    #print(listOfArrays)
    outputString = ''
    for ar in listOfArrays:
        res = morethanndivtwo(ar)
        outputString += str(res) + ' '
    #morethanndivtwo(listOfArrays[1])
    print(outputString)
if __name__== "__main__":
  main()