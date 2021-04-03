import sys
import io

_INPUT = """\
16
insert 35 99
insert 3 80
insert 1 53
insert 14 25
insert 80 76
insert 42 3
insert 86 47
insert 21 12
insert 7 10
insert 6 90
print
find 21
find 22
delete 35
delete 99
print
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

def right_rotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def left_rotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def insert(t, key, priority):
    if t == None:
        return Node(key, priority)
    if key == t.key:
        return t
    if key < t.key:
        t.left = insert(t.left, key, priority)
        if t.priority < t.left.priority:
            t = right_rotate(t)
    else:
        t.right = insert(t.right, key, priority)
        if t.priority < t.right.priority:
            t = left_rotate(t)
    return t            

def delete(t, key):
    if t == None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    return t

def _delete(t, key):
    if t.left == None and t.right == None:
        return None
    elif t.left == None:
        t = left_rotate(t)
    elif t.right == None:
        t = right_rotate(t)
    else:
        if t.left.priority > t.right.priority:
            t = right_rotate(t)
        else:
            t = left_rotate(t)
    return delete(t, key)

def find(t, key):
    if t == None:
        return False
    if t.key == key:
        return True
    if key < t.key:
        return find(t.left, key)
    else:
        return find(t.right, key)

def inorder(t, inout):
    if t == None:
        return
    inorder(t.left, inout)
    inout.append(t.key)
    inorder(t.right, inout)

def preorder(t, preout):
    if t == None:
        return
    preout.append(t.key)
    preorder(t.left, preout)
    preorder(t.right, preout)

def main():
    m = int(input())
    treap = None
    for _ in range(m):
        query = input()
        if query[0] == 'i':
            _, key, priority = query.split()
            treap = insert(treap, int(key), int(priority))
        elif query[0] == 'd':
            _, key = query.split()
            treap = delete(treap, int(key))
        elif query[0] == 'f':
            _, key = query.split()
            if find(treap, int(key)):
                print('yes')
            else:
                print('no')
        elif query[0] == 'p':
            inout = []
            inorder(treap, inout)
            preout = []
            preorder(treap, preout)
            print('', *inout)
            print('', *preout)

if __name__ == '__main__':
    main()