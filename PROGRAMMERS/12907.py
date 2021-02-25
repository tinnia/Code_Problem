def solution(n, money):
    dp = [1] + [0] * n
    for i in money:
        for j in range(i, n + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[n] % 1000000007

# def solution(n, money):
#     dp = [[0] * (n + 1) for _ in range(len(money))]
#     dp[0][0] = 1
#     for i in range(money[0], n + 1, money[0]):
#         dp[0][i] = 1
#
#     for i in range(1, len(money)):
#         for j in range(n + 1):
#             if j >= money[i]:
#                 dp[i][j] = (dp[i-1][j] + dp[i][j - money[i]]) % 1000000007
#             else:
#                 dp[i][j] = dp[i-1][j]
#
#     return dp[-1][-1]



print(solution(5, [1, 2, 5]))