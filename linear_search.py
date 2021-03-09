import sys
import io

_INPUT = """\
5
1 2 3 4 5
3
3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

c = 0
for e1 in T:
    for e2 in S:
        if e1 == e2:
            c += 1
            break

print(c)