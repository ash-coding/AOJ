import sys
import io

_INPUT = """\
aabaaa
aa
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    t = input()
    p = input()
    start = 0
    end = len(p)
    while end <= len(t):
        if t[start:end] == p:
            print(start)
        start += 1
        end += 1

if __name__ == '__main__':
    main()