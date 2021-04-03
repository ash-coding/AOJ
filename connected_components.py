import sys
import io

_INPUT = """\
10 9
0 1
0 2
3 4
5 7
5 6
6 7
6 8
7 8
8 9
3
0 1
5 9
1 3
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    friends[s].append(t)
    friends[t].append(s)
q = int(input())
questions = []
for _ in range(q):
    s, t = map(int, input().split())
    questions.append([s, t])
visited = [0] * n

def dfs(s, id):
    S = []
    S.append(s)
    visited[s] = id
    while S:
        u = S.pop()
        for i in range(len(friends[u])):
            v = friends[u][i]
            if visited[v] == 0:
                visited[v] = id
                S.append(v)

def assign_color():
    id = 1
    for i in range(n):
        visited[i] = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i, id)
            id += 1

def main():
    assign_color()
    for s, t in questions:
        if visited[s] == visited[t]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    main()