from collections import deque

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)

visit = [-1] * (N + 1)
visit[X] = 0
Q = deque([X])
while Q:
    tmp = Q.popleft()
    for i in arr[tmp]:
        if visit[i] == -1:
            visit[i] = visit[tmp] + 1
            Q.append(i)

for i in range(1, N + 1):
    if visit[i] == K:
        print(i)
if K not in visit:
    print(-1)
