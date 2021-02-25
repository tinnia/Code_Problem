def check(queen, row, col, n):
    for i in range(row):
        if col == queen[i] or abs(col - queen[i]) == row - i:
            return False
    return True


def dfs(queen, row, n):
    if row == n:
        return 1
    cnt = 0
    for col in range(n):
        if check(queen, row, col, n):
            queen[row] = col
            cnt += dfs(queen, row + 1, n)
    return cnt


def solution(n):
    return dfs([0] * n, 0, n)


print(solution(4))