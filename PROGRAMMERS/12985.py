def solution(n, a, b):
    answer = 0
    while 1:
        answer += 1
        if (a % 2 == 0 and a - 1 == b) or (a % 2 != 0 and a + 1 == b):
            return answer
        a = a // 2 + a % 2
        b = b // 2 + b % 2


print(solution(8,4,7))
print(solution(8,1,2))
print(solution(8,2,3))
print(solution(8,4,7))
