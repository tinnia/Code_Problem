def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    lst = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            lst[0] += 1
        if answers[i] == p2[i]:
            lst[1] += 1
        if answers[i] == p3[i]:
            lst[2] += 1

    for i in range(3):
        if lst[i] == max(lst[0], lst[1], lst[2]):
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
