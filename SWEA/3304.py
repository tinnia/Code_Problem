for T in range(1, int(input()) + 1):
    X, Y = input().split()
    board = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
            else:
                board[i][j] = max(board[i - 1][j], board[i][j - 1])
    print('#{} {}'.format(T, board[-1][-1]))
