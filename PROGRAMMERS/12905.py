def solution(board):
    ans = 0
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == 1:
                board[r][c] += min(board[r - 1][c - 1], board[r - 1][c], board[r][c - 1])
    for i in board:
        ans = max(ans, max(i))
    return ans ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))