# N = int(input())
# lst = list(map(int, input().split()))
# dp = [1] * N
# for i in range(N):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

N = int(input())
lst = list(map(int, input().split()))
dp = [0]

for i in range(N):
    l, h = 0, len(dp) - 1
    while l <= h:
        mid = (l + h) // 2
        if dp[mid] < lst[i]:
            l = mid + 1
        else:
            h = mid - 1
    if l >= len(dp):
        dp.append(lst[i])
    else:
        dp[l] = lst[i]
print(len(dp) - 1)