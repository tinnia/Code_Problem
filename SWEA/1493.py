def function(val):
    for i in range(1, 300):
        for j in range(1, 300):
            if board[i][j] == val:
                return (i, j)


for T in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    board = [[0] * 300 for _ in range(300)]

    val = 1
    for i in range(1, 300):
        r, c = i, 1
        for j in range(i):
            board[r][c] = val
            val += 1
            r -= 1
            c += 1

    R = function(p)[0] + function(q)[0]
    C = function(p)[1] + function(q)[1]
    print('#{} {}'.format(T, board[R][C]))