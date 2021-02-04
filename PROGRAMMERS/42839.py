from itertools import permutations


def solution(numbers):
    answer, res = 0, []
    for i in range(1, len(numbers) + 1):
        res += permutations(numbers, i)
    res = set([int(''.join(i)) for i in res if int(''.join(i)) != 0 and int(''.join(i)) != 1])

    for i in res:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer

print(solution("011"))