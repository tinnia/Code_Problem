def solution(a):
    answer = 2
    if len(a) <= 3:
        return len(a)

    left, right = a[0], a[-1]
    for i in range(1, len(a) - 1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1-i]:
            answer += 1
            right = a[-1-i]
    if left != right:
        return answer
    return answer - 1