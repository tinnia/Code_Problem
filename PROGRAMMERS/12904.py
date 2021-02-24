def check(st):
    return st == st[::-1]


def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if check(s[i:j]):
                answer = max(answer, len(s[i:j]))
    return answer


print(solution("aa"))
print(solution("abacde"))
