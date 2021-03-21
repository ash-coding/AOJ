import sys
import io

_INPUT = """\
5
3 4 0
4 -1 -1
1 -1 -1
2 -1 -1
0 1 2
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

def pre_parse(tree, u):
    if u == -1:
        return
    print(' ' + str(u), end = '')
    pre_parse(tree, tree[u].left)
    pre_parse(tree, tree[u].right)

def in_parse(tree, u):
    if u == -1:
        return
    in_parse(tree, tree[u].left)
    print(' ' + str(u), end = '')
    in_parse(tree, tree[u].right)

def post_parse(tree, u):
    if u == -1:
        return
    post_parse(tree, tree[u].left)
    post_parse(tree, tree[u].right)
    print(' ' + str(u), end = '')


def main():
    n = int(input())
    tree = []
    for _ in range(n):
        tree.append(Node())
    for _ in range(n):
        id, left, right = map(int, input().split())
        tree[id].left = left
        tree[id].right = right
        if left != -1:
            tree[left].parent = id
        if right != -1:
            tree[right].parent = id
    for i in range(n):
        if tree[i].parent == -1:
            root = i
    
    print('Preorder')
    pre_parse(tree, root)

    print('\nInorder')
    in_parse(tree, root)

    print('\nPostorder')
    post_parse(tree, root)
    print('')

if __name__ == '__main__':
    main()