
# Parameter Parsing
#    N, P = [int(x) for x in input().split(" ")]
#    Ri = [int(x) for x in input().split(" ")]

# Array with length N and default value V
# l = [v for _ in range(N)]
# l = [v] * N
# > [v, v, v, ... ]
# s = 'v' * N
# > 'vvvvvv....v'

# Interactive Tool
# python interactive_runner.py python local_testing_tool.py 0 -- python q4.py

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

def binary_search(nums, x, left=None, right=None, key=None):
    left = 0 if left is None else left
    right = len(nums) - 1 if right is None else right

    if right < left:
        return -1

    mid = left + (right - left) // 2
    value = key(nums[mid]) if key else nums[mid]
    print(left, mid, right, nums[left:right+1], 'value', value)
    if value == x:
        return mid
    elif value > x:
        return binary_search(nums, x, left, mid - 1, key)
    else:
        return binary_search(nums, x, mid + 1, right, key)
