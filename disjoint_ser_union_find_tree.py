import sys
import io

_INPUT = """\
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
"""
sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(100000)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def root(self, x):
        if self.par[x] == x:
            return x
        return self.root(self.par[x])
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.par[ry] = rx
        else:
            self.par[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1

    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

def main():
    n, q = map(int, input().split())
    union_find_tree = UnionFind(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            union_find_tree.unite(x, y)
        else:
            if union_find_tree.same(x, y):
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    main()