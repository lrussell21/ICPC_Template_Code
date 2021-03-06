import os 
from collections import defaultdict

months = None

fib = defaultdict(int)

def rabbitFib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Regular fibonocci until first rabbit dies.
    if n <= months:
        if(fib[n] == 0):
            fib[n] = rabbitFib(n - 1) + rabbitFib(n - 2)
            return fib[n]
        else:
            return fib[n]
    # Kill Off first rabbit
    elif n == months + 1:
        if(fib[n] == 0):
            fib[n] = rabbitFib(n - 1) + rabbitFib(n - 2) - 1
            return fib[n]
        else:
            return fib[n]
    else:
        if(fib[n] == 0):
            # Rabbits that die are subracted from fib.
            fib[n] = rabbitFib(n - 2) + rabbitFib(n - 1) - rabbitFib(n - (months + 1))
            return fib[n]
        else:
            return fib[n]

def main():
    global months
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    output = ''
    for x in numInput:
        x = x.split()
        months = int(x[1])
        y = rabbitFib(int(x[0]))
        output += str(y)
    

    print(fib)
    #out = ''
    #for x in fib:
    #    out += str(fib.get(x)) + ' '
    #print(out)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(output))


if __name__== "__main__":
  main()