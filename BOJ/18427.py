N, M, H = map(int, input().split())

dp = [0] * (H + 1)
dp[0] = 1   # 초기화
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(H, -1, -1):
        for k in tmp:
            if j >= k:
                dp[j] = (dp[j] + dp[j - k]) % 10007
print(dp[H])

