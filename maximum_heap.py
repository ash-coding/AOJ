import sys
import io

_INPUT = """\
10
4 1 3 2 16 9 10 14 8 7
"""
sys.stdin = io.StringIO(_INPUT)

import heapq

n = int(input())
H = list(map(int, input().split()))

H = list(map(lambda x: x * (-1), H))
heapq.heapify(H)

ans = [0] * n
for i in range(n):
    ans[i] = heapq.heappop(H) * (-1)

print(' ', end = '')
print(*ans)