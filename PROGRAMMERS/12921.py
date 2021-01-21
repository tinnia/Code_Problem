def solution(n):
    dp = [0, 0] + [1] * (n - 1)
    answer = 0
    for i in range(2, n + 1):
        if dp[i]:
            answer += 1
            # 소수가 맞다면, 그에 해당하는 배수들을 다 지운다.
            for j in range(2*i, n+1, i):
                dp[j] = 0
    return answer
