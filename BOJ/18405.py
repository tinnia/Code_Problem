from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
Q = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            Q.append((arr[i][j], i, j, 0))

Q.sort()  # 바이러스 순서대로
Q = deque(Q)

while Q:
    virus, r, c, cnt = Q.popleft()
    if cnt == S:
        break
    else:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                arr[nr][nc] = virus
                Q.append((arr[nr][nc], nr, nc, cnt + 1))


print(arr[X - 1][Y - 1])
