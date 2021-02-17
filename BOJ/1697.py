from collections import deque


def bfs():
    Q = deque()
    Q.append(N)
    while Q:
        x = Q.popleft()
        if x == K:
            print(visit[x])
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and not visit[i]:
                visit[i] = visit[x] + 1
                Q.append(i)


N, K = map(int, input().split())
visit = [0] * 100001
bfs()
