import os 
from collections import defaultdict

# a is list of ints
def getLowAndHighSubsequence(a):
    n = len(a)
    lowCheck = [1] * n
    lowIndexSave = [-1] * n
    highCheck = [1] * n
    highIndexSave = [-1] * n
    for i in range(n):
        for j in range(i):
            # Low list
            if (a[j] < a[i] and lowCheck[i] < lowCheck[j] + 1):
                lowCheck[i] = lowCheck[j] + 1
                lowIndexSave[i] = j
            # High list
            if (a[j] > a[i] and highCheck[i] < highCheck[j] + 1):
                highCheck[i] = highCheck[j] + 1
                highIndexSave[i] = j


    ans = lowCheck[0]
    ans2 = highCheck[0]
    pos = 0
    pos2 = 0
    for i in range(n):
        if (lowCheck[i] > ans):
            ans = lowCheck[i]
            pos = i
        if (highCheck[i] > ans2):
            ans2 = highCheck[i]
            pos2 = i
        

    subseq = []
    subseq2 = []
    while (pos != -1):
        subseq.append(a[pos]);
        pos = lowIndexSave[pos];
    while (pos2 != -1):
        subseq2.append(a[pos2]);
        pos2 = highIndexSave[pos2];
    
    subseq.reverse()
    subseq2.reverse()
    return [subseq, subseq2]




def main():
    #global assendList
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    Arr = []
    firstLineSkip = True
    for x in numInput:
        if firstLineSkip:
            firstLineSkip = False
            continue
        Arr.extend(list(map(int, x.split())))
    

    ans = getLowAndHighSubsequence(Arr)
    output1 = ''
    output2 = ''
    for i in ans[0]:
        output1 += str(i) + ' '
    output1 += '\n'
    for i in ans[1]:
        output2 += str(i) + ' '
    
    #print(assendList)
    #assendList = list(dict.fromkeys(assendList))
    #assendOut = ''
    #dessendOut = ''
        
    #for x in range(0, len(Arr)):
    #    if x not in assendList:
    #        dessendOut += str(Arr[x]) + ' '
    #    else:
    #        assendOut += str(Arr[x]) + ' '
    #print(assendOut)
    #print(dessendOut)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(output1 + output2))


if __name__== "__main__":
  main()