import random as r
import os

x1 = ''

for x in range(50000):
    a = r.randint(-10000, 10000)
    b = r.randint(-10000, 10000)
    x1 += str(a) + " " + str(b) + '\n'

# File Output
filename = "/output.txt"
dir_path = os.path.dirname(__file__)
filewrite = open(str(dir_path) + filename, 'w')
filewrite.write(str(x1))