import sys
import io

_INPUT = """\
8
1 2 3 5 9 12 15 23
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A += [0]
    A.sort()
    for i in range(2, n):
        A[1], A[i] = A[i], A[1]
        while i != 1:
            A[i], A[i // 2] = A[i // 2], A[i]
            i //= 2
    A[1], A[n] = A[n], A[1]
    print(*A[1:])

if __name__ == '__main__':
    main()