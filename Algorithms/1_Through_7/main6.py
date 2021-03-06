
x = list(map(str, input("").split()))
thisdict = {}

for word in x:
    if thisdict.get(word) is None:
        thisdict[word] = 1
    else:
        thisdict[word] = thisdict[word] + 1

for key in thisdict:
    print(key, thisdict[key])