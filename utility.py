
#Parameter parsing new lines of integers
if False:
    N, P = [int(x) for x in input().split(" ")]
    Ri = [int(x) for x in input().split(" ")]
    pairs = []
    for _ in range(P):
        pairs.append([int(x) for x in input().split(" ")])

# Replace a single character within a string
def stringReplace(str, i, c):
    return str[:i] + c + str[i+1:]

# Loop backwards:
#   for x in range (len(n), 0, -1):

# Min/Max values and index
def minMaxValueIndex(values):
    minV = min(values)
    maxV = max(values)
    return (
        (minV, values.index(minV)),
        (maxV, values.index(maxV)),
    )

# Template for list of characters
abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Truncate to integer based on 0.5
import math
def normal_round(n):
    return math.floor(n) if n - math.floor(n) < 0.5 else math.ceil(n)

def Reverse(s):
  return s[::-1]

def BitFlip(s):
  return ''.join(str(1 - int(c)) for c in s)

# Log during interactive session
# print('asdf', '\t', 'fdsa', flush=True, file=sys.stderr)
