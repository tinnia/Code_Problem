import sys

sys.setrecursionlimit(10 ** 9)
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def func(r, c):
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = 1
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[r][c] < arr[nr][nc]:
                dp[r][c] = max(dp[r][c], func(nr, nc) + 1)
    return dp[r][c]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, func(i, j))
print(answer)
