N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

for i in dp:
    ans = max(ans, max(i))
print(ans ** 2)
