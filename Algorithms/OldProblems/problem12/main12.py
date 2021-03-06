import os
from collections import defaultdict

# Function to do insertion sort 
def insertionSort(arr): 
    totalCount = 0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j]
                totalCount += 1
                j -= 1
        arr[j+1] = key
    print("Swaps:", totalCount)
    return totalCount


def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    data = numInput[1].split()

    for x in range(len(data)):
        data[x] = int(data[x])

    print(data)
    x1 = insertionSort(data)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(x1))


if __name__ == "__main__":
    main()