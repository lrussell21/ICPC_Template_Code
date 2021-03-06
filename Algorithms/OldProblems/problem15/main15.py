import os 
from collections import defaultdict

def binarySearch(A, k):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2 # '//' does floor division
        if A[m] == k:
            return m + 1
        elif k < A[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    ArrayA = []
    ArrayB = []
    for index,x in enumerate(numInput, start = 0):
        if index == 2:
            ArrayA = list(map(int, x.split()))
        elif index == 3:
            ArrayB = list(map(int, x.split()))
    
    print(ArrayA)
    print(ArrayB)

    outstr = ''
    for ki in ArrayB:
        outstr += str(binarySearch(ArrayA, ki)) + ' '


    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(outstr))


if __name__== "__main__":
  main()