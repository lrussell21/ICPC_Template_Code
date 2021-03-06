import os 
from collections import defaultdict
from itertools import permutations
from itertools import islice

threeSet = set()


def ThreeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = nums[i]*-1
        s,e = i+1, N-1
        while s<e:
            if nums[s]+nums[e] == target:
                return [nums[i], nums[s], nums[e]]
                s = s+1
                while s<e and nums[s] == nums[s-1]:
                    s = s+1
            elif nums[s] + nums[e] < target:
                s = s+1
            else:
                e = e-1
    return -1
    #return result


def getIndex(Arr, nums):
    index = []
    indexCount = 0
    print(nums)
    print(Arr)
    for i in range(len(Arr)):
        if len(index) >= 3:
            break
        if Arr[i] in nums:
            index.append(i)
    print(index)
    return index
        
'''
def ThreeSum(Arr):
    for x in range(0, len(Arr) - 2):
        for y in range(x + 1, len(Arr) - 1):
            for z in range(y + 1, len(Arr)):
                if (Arr[x], Arr[y], Arr[x]) in threeSet:
                    continue
                elif Arr[x]+Arr[y]+Arr[z] == 0:
                    return [x, y, z]
                else:
                    threeSet.add((Arr[x], Arr[y], Arr[x]))
                print(Arr[x], " + ", Arr[y], " + ", Arr[z], " = ", Arr[x]+Arr[y]+Arr[z])
    return -1

def ThreeSum(Arr):
    for i in permutations(Arr, 3):
        print(i)
'''

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
        
        listOfArrays.append(list(map(int, x.strip().split())))
    
    output = ""
    for arr in listOfArrays:
        print(arr)
        backupArr = arr[:]
        out = ThreeSum(arr)
        if out != -1:
            out = getIndex(backupArr, out)
        outputTemp = ""
        if out != -1:
            for num in out:
                outputTemp += str(num + 1) + " "
        else:
            outputTemp = str(out)
        output += outputTemp + "\n"


    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(output))


if __name__== "__main__":
  main()