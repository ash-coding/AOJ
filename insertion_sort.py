import sys
import io

_INPUT = """\
6
5 2 4 6 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    v = a[i]
    j = i - 1
    while j >= 0 and a[j] > v:
        a[j + 1], a[j] = a[j], a[j + 1]
        j -= 1
    a[j + 1] = v
    print(*a)
