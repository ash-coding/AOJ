import sys
import io

_INPUT = """\
4
1 1 2
2 1 4
3 0
4 1 3
"""
sys.stdin = io.StringIO(_INPUT)

time = 0

def dfs_visit(M, color, d, f, n, u):
    global time
    color[u] = 2
    time += 1
    d[u] = time
    for v in range(n):
        if M[u][v] == 0:
            continue
        elif color[v] == 0:
            dfs_visit(M, color, d, f, n, v)
    color[u] = 1
    time += 1
    f[u] = time


def dfs(M, color, d, f, n):
    for u in range(n):
        if color[u] == 0:
            dfs_visit(M, color, d, f, n, u)
    for u in range(n):
        print(str(u + 1) + ' ' + str(d[u]) + ' ' + str(f[u]))
    

def main():
    n = int(input())
    M = [[0] * n for _ in range(n)]
    color = [0] * n
    d = [0] * n
    f = [0] * n

    for _ in range(n):
        lst = list(map(int, input().split()))
        for i, x in enumerate(lst):
            if i == 0:
                u = x - 1
            elif i == 1:
                _ = x
            else:
                M[u][x - 1] = 1
    dfs(M, color, d, f, n)

if __name__ == '__main__':
    main()