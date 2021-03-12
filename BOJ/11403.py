from collections import deque


def bfs(r):
    Q = deque([r])
    while Q:
        x = Q.popleft()
        for i in arr[x]:
            if visit[r][i] == 0:
                visit[r][i] = 1
                Q.append(i)


N = int(input())
arr = [[] * N for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            arr[i].append(j)

visit = [[0] * N for _ in range(N)]
for i in range(N):
    bfs(i)
for i in visit:
    print(*i)
