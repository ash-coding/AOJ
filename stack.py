import sys
import io

_INPUT = """\
1 2 + 3 4 - *
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    A = list(map(str, input().split()))
    
    S =[]
    for i in A:
        if i == '+':
            num = int(S.pop()) + int(S.pop())
            S.append(num)
        elif i == '-':
            num = - int(S.pop()) + int(S.pop())
            S.append(num)
        elif i == '*':
            num = int(S.pop()) * int(S.pop())
            S.append(num)
        else:
            S.append(i)

    print(int(S.pop()))

if __name__ == "__main__":
    main()