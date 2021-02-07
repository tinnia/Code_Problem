def solution(n):
    answer = 0

    def func(idx, sum):
        nonlocal answer
        if sum >= n:
            if sum == n:
                answer += 1
            return
        func(idx + 1, sum + idx + 1)

    for i in range(1, n+1):
        func(i, i)
    return answer
