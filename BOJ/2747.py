# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(int(input())))

n = int(input())
dp = [0, 1]
for _ in range(2, n + 1):
    dp.append(dp[-1] + dp[-2])

print(dp[n])
