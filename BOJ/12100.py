from copy import deepcopy


def rotate(board):
    new_board = deepcopy(board)
    for i in range(N):
        for j in range(N):
            new_board[j][N - i - 1] = board[i][j]
    return new_board

def move(board):
    board= rotate(board)
    for j in range(N):
        idx = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[idx][j] == 0:
                    board[idx][j] = tmp
                elif board[idx][j] == tmp:
                    board[idx][j] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    board[idx][j] = tmp





def dfs(cnt):
    global ans, board
    if cnt == 5:
        for i in range(N):
            ans = max(ans, max(board[i]))

    tmp = deepcopy(board)
    for _ in range(4):
        move(tmp)
        dfs(cnt + 1)
        board = deepcopy(tmp)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0)
