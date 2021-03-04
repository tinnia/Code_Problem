from collections import deque

N, K = map(int, input().split())
Q = deque(list(range(1, N + 1)))
print('<', end='')
while Q:
    for i in range(K - 1):
        Q.append(Q[0])
        Q.popleft()
    print(Q.popleft(), end='')
    if Q:
        print(', ', end='')
print('>')
