import sys
import io

_INPUT = """\
4
1 2 2 4
2 1 4
3 0
4 1 3
"""
sys.stdin = io.StringIO(_INPUT)

import queue

def bfs(M, d, n, s):
    q = queue.Queue()
    q.put(s)
    d[s] = 0
    while not q.empty():
        u = q.get()
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != float('inf'):
                continue
            d[v] = d[u] + 1
            q.put(v)
    for i in range(n):
        print(str(i + 1) + ' ' + str((-1) if d[i] == float('inf') else d[i]))

def main():
    n = int(input())
    M = [[0] * n for _ in range(n)]
    d = [float('inf')] * n
    for _ in range(n):
        lst = list(map(int, input().split()))
        for i, x in enumerate(lst):
            x -= 1
            if i == 0:
                u = x
            elif i > 1:
                M[u][x] = 1
    bfs(M, d, n, 0)

if __name__ == '__main__':
    main()