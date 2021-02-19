from copy import deepcopy


def rotate(B, n):
    board1 = deepcopy(B)
    for i in range(n):
        for j in range(n):
            board1[j][n - i - 1] = B[i][j]
    return board1


def convert(lst, n):
    board1 = [i for i in lst if i]
    for i in range(1, len(board1)):
        if board1[i-1] == board1[i]:
            board1[i-1] *= 2
            board1[i] = 0
    board1 = [i for i in board1 if i]
    return board1 + [0] * (n - len(board1))


def dfs(n, B, cnt):
    tmp = max([max(i) for i in B])
    if cnt == 0:
        return tmp
    for _ in range(4):
        x = [convert(i, n) for i in B]
        if x != B:
            tmp = max(tmp, dfs(n, x, cnt-1))
        B = rotate(B, n)
    return tmp


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(dfs(N, board, 5))