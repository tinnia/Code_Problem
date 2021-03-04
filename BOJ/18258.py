import sys
from collections import deque
N = int(sys.stdin.readline())
Q = deque([])
for i in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        Q.append(tmp[1])
    elif tmp[0] == 'pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif tmp[0] == 'size':
        print(len(Q))
    elif tmp[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif tmp[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])