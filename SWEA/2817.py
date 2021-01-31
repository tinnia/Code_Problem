def function(idx, sum):
    global ans
    if sum > K:
        return
    if idx >= N:
        if sum == K:
            ans += 1
        return
    function(idx + 1, sum + nums[idx])
    function(idx + 1, sum)


for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    function(0, 0)

    print('#{} {}'.format(T, ans))
