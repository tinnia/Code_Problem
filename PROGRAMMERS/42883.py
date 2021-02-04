def solution(number, k):
    answer = [number[0]]
    for i in number[1:]:
        while answer and answer[-1] < i and k > 0:
            k -= 1
            answer.pop()
        answer.append(i)

    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("1924", 3))
