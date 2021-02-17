from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(i, j):
    Q = deque()
    Q.append((i, j))
    visit[i][j] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1 and not visit[nr][nc]:
                    visit[nr][nc] = 1
                    Q.append((nr, nc))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    visit = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visit[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)
