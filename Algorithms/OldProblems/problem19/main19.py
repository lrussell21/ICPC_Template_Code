import os 
from collections import defaultdict

def partition(A, start, end):
    pivot = A[start]
    low = start + 1
    high = end

    while True:

        while low <= high and A[high] >= pivot:
            high = high - 1

        while low <= high and A[low] <= pivot:
            low = low + 1

        if low <= high:
            temp = A[low]
            A[low] = A[high]
            A[high] = temp

        else:
            break

    temp = A[start]
    A[start] = A[high]
    A[high] = temp

    return high


def quick_sort(A, start, end):
    if start >= end:
        return

    p = partition(A, start, end)
    quick_sort(A, start, p-1)
    quick_sort(A, p+1, end)


def main():
    # File Input
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    ArrayA = []
    for index,x in enumerate(numInput, start = 0):
        if index == 1:
            ArrayA = list(map(int, x.split()))




    #str1 = ''
    #for st in ArrayA: str1 += str(st) + ' '
    #print(str1)
    print(ArrayA)

    quick_sort(ArrayA, 0, len(ArrayA) - 1)
    
    str1 = ''
    for st in ArrayA: str1 += str(st) + ' '
    print(str1)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(str1))


if __name__== "__main__":
  main()