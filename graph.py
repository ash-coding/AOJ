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

def main():
    n = int(input())
    adj = [[0] * n for _ in range(n)]
    for _ in range(n):
        lst = list(map(int, input().split()))
        for i, e in enumerate(lst):
            e -= 1
            if i == 0:
                v = e
            if i > 1:
                adj[v][e] = 1
    for e in adj:
        print(*e)

if __name__ == '__main__':
    main()