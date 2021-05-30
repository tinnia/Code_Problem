class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            garo, sero = [], []
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] not in garo:
                    garo.append(board[i][j])
                elif board[i][j].isdigit() and board[i][j] in garo:
                    return False
                if board[j][i].isdigit() and board[j][i] not in sero:
                    sero.append(board[j][i])
                elif board[j][i].isdigit() and board[j][i] in sero:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                stack, r, c = [], 0, 0
                while r < 3:
                    if board[i + r][j + c].isdigit() and board[i + r][j + c] not in stack:
                        stack.append(board[i + r][j + c])
                    elif board[i + r][j + c].isdigit() and board[i + r][j + c] in stack:
                        return False
                    c += 1
                    if c == 3:
                        r, c = r + 1, 0
        return True