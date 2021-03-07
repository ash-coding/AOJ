import sys
import io

_INPUT = """\
6
5 6 4 2 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            minj = j
    if minj != i:
        a[i], a[minj] = a[minj], a[i]
        cnt += 1

print(*a)
print(cnt)