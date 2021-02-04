def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    flag = num = 1
    i = j = 0
    while num <= sum(range(1, n + 1)):
        if flag == 1:
            answer[i][j] = num
            num, i = num + 1, i + 1
            if i == n or answer[i][j]:
                i, j, flag = i - 1, j + 1, 2

        elif flag == 2:
            answer[i][j] = num
            num, j = num + 1, j + 1
            if j == n or answer[i][j]:
                i, j, flag = i - 1, j - 2, 3

        elif flag == 3:
            answer[i][j] = num
            num, i, j = num + 1, i - 1, j - 1
            if answer[i][j]:
                i, j, flag = i + 2, j + 1, 1

    return sum(answer, [])


print(solution(4))
print(solution(5))
print(solution(6))
