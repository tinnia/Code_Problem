def solution(n):
    answer = ''
    rule = ['4', '1', '2']
    while n:
        n, m = divmod(n, 3)
        answer = rule[m] + answer
        if not m:
            n -= 1
    return answer

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))