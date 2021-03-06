
x , y = input("").split()
oddsum = 0
for x in range(int(x), int(y) + 1):
    if x % 2 == 1:
        oddsum = oddsum + x

print(oddsum)