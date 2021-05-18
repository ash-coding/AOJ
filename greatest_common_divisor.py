import sys
import io

_INPUT = """\
147 105
"""
sys.stdin = io.StringIO(_INPUT)

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def main():
    x, y = map(int, input().split())
    ans = gcd(x, y)
    print(ans)

if __name__ == '__main__':
    main()