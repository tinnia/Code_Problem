N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if nums[i] + nums[j] + nums[k] <= M:
                ans = max(ans, nums[i] + nums[j] + nums[k])
print(ans)