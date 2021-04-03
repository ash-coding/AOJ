import sys
import io

_INPUT = """\
5
 -1 2 3 1 -1
 2 -1 -1 4 -1
 3 -1 -1 1 1
 1 4 1 -1 3
 -1 -1 1 3 -1
"""
sys.stdin = io.StringIO(_INPUT)

def prim(d, p, color, M, n):
    d[0] = 0
    while 1:
        minv = float('inf')
        u = -1
        for i in range(n):
            if minv > d[i] and color[i] != 2:
                u = i
                minv = d[i]
        if u == -1:
            break
        color[u] = 2
        for v in range(n):
            if color[v] != 2 and M[u][v] != float('inf'):
                if d[v] > M[u][v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = 1
    ans = 0
    for i in range(n):
        if p[i] != -1:
            ans += M[i][p[i]]
    return ans

def main():
    n = int(input())
    M = [[0] * n for _ in range(n)]
    color = [0] * n
    d = [float('inf')] * n
    p = [-1] * n
    for i in range(n):
        *q, = map(int, input().split())
        for j, x in enumerate(q):
            if x == -1:
                M[i][j] = float('inf')
            else:
                M[i][j] = x

    print(prim(d, p, color, M, n))

if __name__ == '__main__':
    main()