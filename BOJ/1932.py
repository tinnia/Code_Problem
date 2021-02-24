N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * i for i in range(1, N + 1)]
dp[0] = tri[0]
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][j]
        elif i == j:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

print(max(dp[N - 1]))
