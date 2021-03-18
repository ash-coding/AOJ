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
        self.id = -1
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.left = -1
        self.right = -1
        self.type = ''

def output(Node):
    print('node ' + str(Node.id) + ': '\
            + 'parent = ' + str(Node.parent) + ', '\
            + 'sibling = ' + str(Node.sibling) + ', '\
            + 'degree = ' + str(Node.degree) + ', '\
            + 'depth = ' + str(Node.depth) + ', '\
            + 'height = ' + str(Node.height) + ', '\
            + Node.type)

def calculate_depth(tree, id, depth):
    tree[id].depth = depth
    if tree[id].left != -1:
        calculate_depth(tree, tree[id].left, depth + 1)
    if tree[id].right != -1:
        calculate_depth(tree, tree[id].right, depth + 1)

def calculate_height(tree, id):
    if tree[id].left != -1:
        tree[id].height = max(tree[id].height, calculate_height(tree, tree[id].left) + 1)
    if tree[id].right != -1:
        tree[id].height = max(tree[id].height, calculate_height(tree, tree[id].right) + 1)
    return tree[id].height

def main():
    n = int(input())
    tree = []
    for _ in range(n):
        node = Node()
        tree.append(node)

    for _ in range(n):
        id, left, right = map(int, input().split())
        tree[id].id = id
        tree[id].left = left
        tree[id].right = right
        if left != -1:
            tree[left].sibling = right
            tree[left].parent = id
            tree[id].degree += 1
        if right != -1:
            tree[right].sibling = left
            tree[right].parent = id
            tree[id].degree += 1
        
    for t in tree:
        if t.parent == -1:
            root = t.id

    calculate_depth(tree, root, 0)
    calculate_height(tree, root)

    for t in tree:
        if t.parent == -1:
            t.type = 'root'
        elif t.left == -1 and t.right == -1:
            t.type = 'leaf'
        else:
            t.type = 'internal node'

    for t in tree:
        output(t)

if __name__ == "__main__":
    main()