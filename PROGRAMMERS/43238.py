def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for time in times:
            tmp += mid // time
            if tmp >= n:
                break
        if tmp < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer


print(solution(6, [7, 10]))
