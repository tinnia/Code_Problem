def solution(brown, yellow):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4
    y = (brown + yellow) // x
    return [int(max(x, y)), int(min(x, y))]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(50, 22))
# print(solution(10,2))
