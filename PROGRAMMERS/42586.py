def solution(progresses, speeds):
    answer = []
    stack = [round((100 - progresses[0]) / speeds[0] + 0.5)]
    for i in range(1, len(progresses)):
        if stack[-1] >= (round((100 - progresses[i]) / speeds[i] + 0.5)):
            stack.append(stack[-1])
        else:
            answer.append(len(stack))
            stack = []
            stack.append(round((100 - progresses[i]) / speeds[i] + 0.5))
    answer.append(len(stack))
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([95, 95, 95, 95], [4, 3, 2, 1]))
