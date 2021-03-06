
indexToGet = input('')
a = 0
b = 1
for index in range(int(indexToGet)):
    x = a + b
    a = b
    b = x
print(a)
