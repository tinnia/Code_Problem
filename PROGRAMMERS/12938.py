def solution(n, s):
    if n > s:
        return [-1]
    [x, y] = divmod(s, n)
    answer = [x] * n
    for i in range(y):
        answer[i] += 1
    return sorted(answer)


print(solution(2, 9))
print(solution(2, 8))
