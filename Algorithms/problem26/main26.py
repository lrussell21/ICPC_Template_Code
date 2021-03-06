import os 
from collections import defaultdict

    

def containsNegComp(array):
    di = defaultdict(int)

    for num in range(0, int(len(array))):
        if di.get(int(array[num])) != None:
            return [(di.get(int(array[num])) + 1), int(num) + 1]
        else:
            di[-1 * int(array[num])] = int(num)

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
        res = containsNegComp(ar)
        if res == -1:
            outputString += str(res) + ' '
        else:
            outputString += str(res[0]) + ' ' + str(res[1]) + ' '
        
        print(outputString)
        outputString = ''
    #morethanndivtwo(listOfArrays[1])
if __name__== "__main__":
  main()