import os 
from collections import defaultdict


def mergeSortedArray(A, B):

    C = []
    aindex = 0
    bindex = 0
    blen = len(B)
    for x in A:
        if bindex <= blen:
            if B[bindex] < x:
                for i in range(bindex, blen):
                    if B[i] <= x:
                        C.append(B[i])
                        bindex += 1
                    else:
                        break
        C.append(x)
    if bindex < blen : C.extend(B[bindex:blen])

    return C


def main():
    # File Input
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    ArrayA = []
    ArrayB = []
    firstLineSkip = True
    for index,x in enumerate(numInput, start = 0):
        if index == 1:
            ArrayA = list(map(int, x.split()))
        elif index == 3:
            ArrayB = list(map(int, x.split()))
    


    x = mergeSortedArray(ArrayA,ArrayB)
    str1 = ''
    for st in x: str1 += str(st) + ' '
    print(str1)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(str1))


if __name__== "__main__":
  main()