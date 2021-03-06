import os 

def main():
    filename = "/testfile.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    lines = f.readlines()
    odd = False
    outputLines = []
    for x in lines:
        if odd:
            outputLines.append(x)
            odd = False
        else:
            odd = True
    for x in outputLines:
        print(x, end = '') # No newline because it is inlcuded in string
if __name__== "__main__":
  main()