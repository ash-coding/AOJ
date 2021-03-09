import sys
import io

_INPUT = """\
5
1 2 3 4 5
3
3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

def binary_search(S, n, t):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if t == S[mid]:
            return 1
        elif t < S[mid]:
            right = mid
        else:
            left = mid + 1
    return 0

def main():
    n = int(input())
    S = list(map(int, input().split()))
    _ = int(input())
    T = list(map(int, input().split()))

    c = 0
    for e in T:
        c += binary_search(S, n, e)
    print(c)

if __name__ == "__main__":
    main()