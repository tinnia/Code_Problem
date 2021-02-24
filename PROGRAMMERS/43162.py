def solution(n, computers):
    answer, visit = 0, [0] * n
    for i in range(n):
        if visit[i] == 0:
            stack = [i]
            while stack:
                num = stack.pop()
                visit[num] = 1
                for j in range(n):
                    if num != j and visit[j] == 0 and computers[num][j]:
                        visit[j] = 1
                        stack.append(j)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
