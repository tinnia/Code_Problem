def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))


def solution(land):
    for i in range(len(land)):
        if i == len(land) - 1:
            return max(land[i])
        for j in range(4):
            land[i+1][j] += max(land[i][:j] + land[i][j+1:])
