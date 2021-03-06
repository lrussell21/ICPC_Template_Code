import os 
from collections import defaultdict
import copy


def mergeSort(A):
    
    if len(A) > 1:

        B = A[int((len(A))/2):] # Should have a '-1' but for some reason not having makes it work
        C = A[0:int((len(A))/2)]
        #print(B)
        #print(C)
        mergeSort(B)
        mergeSort(C)

        # Doesn't work for some reason
        #A = mergeSortedArray(B, C)

        i = j = k = 0

        while i < len(B) and j < len(C): 
            if B[i] < C[j]: 
                A[k] = B[i] 
                i+= 1
            else: 
                A[k] = C[j] 
                j+= 1
            k+= 1
          
        while i < len(B): 
            A[k] = B[i] 
            i+= 1
            k+= 1
          
        while j < len(C): 
            A[k] = C[j] 
            j+= 1
            k+= 1

        #print(A)
        #return A


def mergeSortedArray(A, B):
    C = A
    C.extend(B)
    C.sort()
    print(C)
    return C
    #print(A, "\t", B)
    '''
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            A.reverse()
    elif len(B) == 2:
        if B[0] > B[1]:
            B.reverse()
    C = []
    aindex = 0
    bindex = 0
    blen = int(len(B))
    for x in A:
        if bindex < blen:
            if B[bindex] < x:
                for i in range(bindex, blen):
                    if B[i] <= x:
                        C.append(B[i])
                        bindex += 1
                    else:
                        break
        C.append(x)
    if bindex < blen - 1 : C.extend(B[bindex:blen])
    #print(C, "\n\n")
    return C
    '''


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

    #print(ArrayA)
    mergeSort(ArrayA)
    #print(ArrayA)
    #x = mergeSortedArray(ArrayA,ArrayB)
    str1 = ''
    for st in ArrayA: str1 += str(st) + ' '
    #print(str1)


    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(str1))


if __name__== "__main__":
  main()