import sys
import io

_INPUT = """\
10
4 1 3 2 16 9 10 14 8 7
"""
sys.stdin = io.StringIO(_INPUT)

def max_heapify(A, n, i):
    l = 2 * i
    r = 2 * i + 1
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(n // 2, 0, -1):
        max_heapify(A, n, i)
    print(' ', end = '')
    print(*A[1:])

if __name__ == '__main__':
    main()