import sys
import io

_INPUT = """\
5
5 3 2 4 1
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))

cnt = 0
flag = 1
i = 0
while flag:
    flag = 0
    for j in reversed(range(i + 1, n)):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = 1
            cnt += 1
    i += 1

print(*a)
print(cnt)
