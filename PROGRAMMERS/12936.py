from math import factorial


def solution(n, k):
    answer, numbers = [], list(range(1, n + 1))
    l = len(numbers)

    # def factorial(num):
    #     if num == 1:
    #         return 1
    #     return num * factorial(num - 1)

    while len(answer) != l:
        n -= 1
        idx, rest = divmod(k, factorial(n))
        if rest == 0:
            idx -= 1
        answer.append(numbers[idx])
        numbers.remove(numbers[idx])
        k = rest

    return answer


print(solution(4, 1))
print(solution(4, 2))
print(solution(4, 3))
print(solution(4, 4))
print(solution(4, 5))
print(solution(4, 6))
