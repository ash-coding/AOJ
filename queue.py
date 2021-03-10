import sys
import io

_INPUT = """\
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""
sys.stdin = io.StringIO(_INPUT)

def isEmpty(head, tail):
    return head == tail

def isFull(head, tail, MAX):
    return head == (tail + 1) % MAX

def enqueue(Q, name, time, head, tail, MAX):
    if isFull(head, tail, MAX):
        print('error')
        exit()
    Q[tail][1] = time
    Q[tail][0] = name
    if tail + 1 == MAX:
        return 0
    else:
        return tail + 1

def dequeue(Q, head, tail, MAX):
    if isEmpty(head, tail):
        print('error')
        exit()
    time = Q[head][1]
    name = Q[head][0]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return [name, time, head]

def main():
    n, quantum = map(int, input().split())
    MAX = n + 1
    
    Q = [['', 0] for _ in range(MAX)]
    for i in range(n):
        name, time = map(str, input().split())
        Q[i][0] = name
        Q[i][1] = int(time)
    
    head = 0
    tail = n
    acc_time = 0
    while not isEmpty(head, tail):
        deq = dequeue(Q, head, tail, MAX)
        head_origin = head
        name = deq[0]
        time = deq[1]
        head = deq[2]
        if time > quantum:
            acc_time += quantum
            tail = enqueue(Q, name, time - quantum, head, tail, MAX)
        else:
            acc_time += time
            print(Q[head_origin][0] + ' ' + str(acc_time))

if __name__ == "__main__":
    main()