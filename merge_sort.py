import sys
import io

_INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
"""
sys.stdin = io.StringIO(_INPUT)

cnt = 0

def merge(S, n, left, mid, right):
    global cnt
    L = S[left:mid]
    R = S[mid:right]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1

def merge_sort(S, n, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(S, n, left, mid)
        merge_sort(S, n, mid, right)
        merge(S, n, left, mid, right)

def main():
    n = int(input())
    S = list(map(int, input().split()))
    merge_sort(S, n, 0, n)
    print(*S)
    print(cnt)

if __name__ == "__main__":
    main()