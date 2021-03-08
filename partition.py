import sys
import io

_INPUT = """\
12
13 19 9 5 12 8 7 4 21 2 6 11
"""
sys.stdin = io.StringIO(_INPUT)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = partition(A, 0, n - 1)
    res = []
    for i in range(n):
        if i == q:
            res.append('[' + str(A[i]) + ']')
        else:
            res.append(str(A[i]))
    print(*res)

if __name__ == "__main__":
    main()