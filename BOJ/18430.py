def dfs(r, c, cnt):
    global ans
    if c == M:
        c = 0
        r += 1
    if r == N:
        ans = max(ans, cnt)
        return
    if not visit[r][c]:
        # ㄱ
        if r + 1 < N and 0 <= c - 1 and not visit[r + 1][c] and not visit[r][c - 1]:
            visit[r][c] = visit[r + 1][c] = visit[r][c - 1] = 1
            dfs(r, c + 1, cnt + 2 * arr[r][c] + arr[r + 1][c] + arr[r][c - 1])
            visit[r][c] = visit[r + 1][c] = visit[r][c - 1] = 0
        # ㄴ
        if 0 <= r - 1 and c + 1 < M and not visit[r - 1][c] and not visit[r][c + 1]:
            visit[r][c] = visit[r - 1][c] = visit[r][c + 1] = 1
            dfs(r, c + 1, cnt + 2 * arr[r][c] + arr[r - 1][c] + arr[r][c + 1])
            visit[r][c] = visit[r - 1][c] = visit[r][c + 1] = 0
        # ┌
        if r + 1 < N and c + 1 < M and not visit[r + 1][c] and not visit[r][c + 1]:
            visit[r][c] = visit[r + 1][c] = visit[r][c + 1] = 1
            dfs(r, c + 1, cnt + 2 * arr[r][c] + arr[r + 1][c] + arr[r][c + 1])
            visit[r][c] = visit[r + 1][c] = visit[r][c + 1] = 0
        # ┘
        if 0 <= r - 1 and 0 <= c - 1 and not visit[r - 1][c] and not visit[r][c - 1]:
            visit[r][c] = visit[r - 1][c] = visit[r][c - 1] = 1
            dfs(r, c + 1, cnt + 2 * arr[r][c] + arr[r - 1][c] + arr[r][c - 1])
            visit[r][c] = visit[r - 1][c] = visit[r][c - 1] = 0
    dfs(r, c + 1, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
if N == 1 or M == 1:
    print(0)
else:
    visit = [[0] * M for _ in range(N)]
    ans = 0
    dfs(0, 0, 0)
    print(ans)
