def solution(n):
    if n ** 0.5 % 1:
        return -1
    else:
        return (int(n**0.5) + 1) ** 2


print(solution(3))
print(solution(121))