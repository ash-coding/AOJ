import sys
import io

_INPUT = """\
12
8 6 11 4 1 9 12 5 7 3 2 10
"""
sys.stdin = io.StringIO(_INPUT)

import heapq

n = int(input())
H = list(map(int, input().split()))

H = list(map(lambda x: x * (-1), H))
heapq.heapify(H)
H = list(map(lambda x: x * (-1), H))
print(' ', end = '')
print(*H)
