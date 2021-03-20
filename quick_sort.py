import sys
import io

_INPUT = """\
6
D 3
H 2
D 1
S 3
D 2
C 1
"""
sys.stdin = io.StringIO(_INPUT)

from operator import itemgetter
def partition(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def main():
    n = int(input())
    A = []
    for _ in range(n):
        c, v = map(str, input().split())
        A.append([int(v), c])

    B = sorted(A, key = itemgetter(0))
    quick_sort(A, 0, n - 1)

    stable = True
    for i in range(n):
        if A[i][1] != B[i][1]:
            stable = False
            break
    
    if stable:
        print('Stable')
    else:
        print('Not stable')

    for e in A:
        print(e[1] + ' ' + str(e[0]))

if __name__ == "__main__":
    main()

"""
def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

n = int(input())
A = []
for _ in range(n):
    c, v = map(str, input().split())
    A.append([c, int(v)])
quick_sort(A, 0, n - 1)
for e in A:
    print(e[0] + ' ' + str(e[1]))
"""