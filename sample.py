myFile = None
def readInputLine():
    global myFile
    shouldReadFile = True
    if shouldReadFile:
        if myFile is None:
            myFile = open('sample.in')
        return myFile.readline()
    else:
        return input()

def do_work():
    N = int(readInputLine())
    P = [int(x) for x in readInputLine().split(" ")]
    return "{} {}".format(N, len(P))

T = int(readInputLine())
for i in range(1, T + 1):
    print("Case #{}: {}".format(i, do_work()))

if myFile is not None:
    myFile.close()