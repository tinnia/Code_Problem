from collections import deque


def bfs(s, mode):
    visit = [-1] * (V + 1)
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


V = int(input())
lst = [[] for _ in range(V + 1)]
for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp) - 2, 2):
        lst[tmp[0]].append([tmp[i], tmp[i + 1]])
print(bfs(bfs(1, 1), 2))
