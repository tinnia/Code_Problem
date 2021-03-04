from collections import deque


def bfs(s, mode):
    visit = [-1] * (n + 1)
    visit[s] = 0
    Q = deque([s])
    while Q:
        x = Q.popleft()
        for y, w in lst[x]:
            if visit[y] == -1:
                visit[y] = visit[x] + w
                Q.append(y)
    if mode == 1:
        return visit.index(max(visit))
    else:
        return max(visit)


n = int(input())
lst = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, w = map(int, input().split())
    lst[x].append([y, w])
    lst[y].append([x, w])
print(bfs(bfs(1, 1), 2))
