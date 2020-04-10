
def compute():
    N = int(input())
    P = [int(x) for x in input().split(" ")]

    return "{} {}".format(N, len(P))

T = int(input())
for i in range(1, T + 1):
    print("Case #{}: {}".format(i, compute()))
