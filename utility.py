
# Parameter Parsing
#    N, P = [int(x) for x in input().split(" ")]
#    Ri = [int(x) for x in input().split(" ")]

# Array with length N and default value V
# l = [v] * N
# > [v, v, v, ... ]
# s = 'v' * N
# > 'vvvvvv....v'

abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def stringReplace(str, i, c):
    return str[:i] + c + str[i+1:]

def backwardsLoop(n):
    n = [1,2,3,4,5,6,7,8,9]
    for x in range(len(n), 0, -1):
        print(x)

def minMaxValueIndex(values):
    minV = min(values)
    maxV = max(values)
    return (
        (minV, values.index(minV)),
        (maxV, values.index(maxV)),
    )

import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)