def solution(S):
    if len(S) % 2:
        return S[len(S) // 2]
    return S[len(S) // 2 - 1:len(S) // 2 + 1]


print(solution('abcde'))
print(solution('qwer'))
