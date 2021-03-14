import sys
import io

_INPUT = """\
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
    def __init__(self):
        self.id = -1
        self.cnum = 0
        self.children = []
        self.parent = -1
        self.depth = -1
        self.type = ''

def output(Node):
    t1 = 'node ' + str(Node.id) + ': '
    t2 = 'parent = ' + str(Node.parent) + ', '
    t3 = 'depth = ' + str(Node.depth) + ', '
    t4 = Node.type + ', '
    t5 = '['
    for i, c in enumerate(Node.children):
        if i == Node.cnum - 1:
            t5 += str(c)
        else:
            t5 += str(c) + ', '
    t5 += ']'
    print(t1 + t2 + t3 + t4 + t5)

def calculate_depth(tree, id, depth):
    tree[id].depth = depth
    if tree[id].children:
        for c in tree[id].children:
            calculate_depth(tree, c, depth + 1)

def main():
    n = int(input())
    tree = []
    for _ in range(n):
        node = Node()
        tree.append(node)

    for _ in range(n):
        inp = list(map(int, input().split()))
        for j, e in enumerate(inp):
            if j == 0:
                tree[e].id = e
                u = e
            elif j == 1:
                tree[u].cnum = e
            else:
                tree[u].children.append(e)
                tree[e].parent = tree[u].id

    for t in tree:
        if t.parent == -1:
            root = t.id

    calculate_depth(tree, root, 0)

    for t in tree:
        if t.parent == -1:
            t.type = 'root'
        elif t.cnum == 0:
            t.type = 'leaf'
        else:
            t.type = 'internal node'

    for t in tree:
        output(t)

if __name__ == "__main__":
    main()