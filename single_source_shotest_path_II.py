import sys
import io

_INPUT = """\
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
"""
sys.stdin = io.StringIO(_INPUT)

import heapq
def dijkstra(M, d, p, color, n, s):
    d[s] = 0
    PQ = []
    heapq.heapify(PQ)
    heapq.heappush(PQ, [0, s])
    while PQ:
        f = heapq.heappop(PQ)
        u = f[1]
        c = f[0]
        color[u] = 2
        if d[u] < c:
            continue
        for j in range(len(M[u])):
            v = M[u][j][1]
            if color[v] == 2:
                continue
            if d[u] + M[u][j][0] < d[v]:
                d[v] = d[u] + M[u][j][0]
                heapq.heappush(PQ, [d[v], v])
                color[v] = 1

def main():
    n = int(input())
    M = [[] for _ in range(n)]
    d = [float('inf')] * n
    p = [-1] * n
    color = [0] * n
    for _ in range(n):
        u, k, *query, = map(int, input().split())
        for i in range(k):
            M[u].append([query[2 * i + 1], query[2 * i]])
    dijkstra(M, d, p, color, n, 0)
    for i in range(n):
        print(i, d[i])

if __name__ == '__main__':
    main()