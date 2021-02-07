def solution(nums):
    from itertools import combinations
    answer = 0

    # 소수 dp 만들기
    dp = [1] * (sum(nums) + 1)
    dp[0] = dp[1] = 0
    i = 2
    while i <= sum(nums):
        for j in range(2 * i, sum(nums) + 1, i):
            dp[j] = 0
        i += 1

    tmp = list(combinations(nums, 3))
    for k in tmp:
        if dp[sum(k)]:
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
