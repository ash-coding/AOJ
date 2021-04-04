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

def dijkstra(M, d, p, color, n, s):
    d[s] = 0
    p[s] = -1
    while 1:
        mincost = float('inf')
        for i in range(n):
            if color[i] != 2 and d[i] < mincost:
                mincost = d[i]
                u = i
        if mincost == float('inf'):
            break
        color[u] = 2
        for v in range(n):
            if color[v] != 2 and M[u][v] != 0:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    color[v] = 1

def main():
    n = int(input())
    M = [[0] * n for _ in range(n)]
    d = [float('inf')] * n
    p = [0] * n
    color = [0] * n
    for _ in range(n):
        u, k, *query, = map(int, input().split())
        for i in range(k):
            M[u][query[2 * i]] = query[2 * i + 1]
    dijkstra(M, d, p, color, n, 0)
    for i in range(n):
        print(i, d[i])

if __name__ == '__main__':
    main()