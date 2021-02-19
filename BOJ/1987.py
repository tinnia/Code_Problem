from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global ans
    Q = deque()
    Q.append((0, 0, arr[0][0]))
    visit = [[''] * C for _ in range(R)]
    visit[0][0] = arr[0][0]
    while Q:
        r, c, data = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in data:
                if visit[nr][nc] == data + arr[nr][nc]: continue
                visit[nr][nc] = data + arr[nr][nc]
                Q.append((nr, nc, data + arr[nr][nc]))
                ans = max(ans, len(data) + 1)
    return


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

ans = 1
bfs()
print(ans)