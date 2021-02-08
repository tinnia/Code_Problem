def solution(n, t, m, p):
    answer = '0'
    nums = "0123456789ABCDEF"
    num = 1
    while len(answer) < t * m:
        tmp = num
        tmp_ans = ''
        while tmp:
            tmp_ans = nums[tmp % n] + tmp_ans
            tmp //= n
        answer += tmp_ans
        num += 1

    return answer[p - 1:t * m:m]


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
