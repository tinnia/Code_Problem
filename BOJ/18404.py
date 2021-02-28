from collections import deque

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]


def func(r, c):
    Q = deque()
    Q.append((r, c))
    while Q:
        v, w = Q.popleft()
        for i in range(8):
            nr = v + dr[i]
            nc = w + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                visit[nr][nc] = visit[v][w] + 1
                Q.append((nr, nc))


N, M = map(int, input().split())
x, y = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

visit = [[0] * N for _ in range(N)]
func(x - 1, y - 1)

ans = []
for i in lst:
    ans.append(visit[i[0]-1][i[1]-1])
print(*ans)
