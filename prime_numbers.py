import sys
import io

_INPUT = """\
6
2
3
4
5
6
7
"""
sys.stdin = io.StringIO(_INPUT)

def is_prime(x):
    if x == 2:
        return 1
    if x < 1 or x % 2 == 0:
        return 0
    i = 3
    while i * i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1

def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        x = int(input())
        ans += is_prime(x)
    print(ans)

if __name__ == '__main__':
    main()