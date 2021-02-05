dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def change(r, c, color):
    board[r][c] = color
    for i in range(8):
        nr = r
        nc = c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr <= 0 or nr > N or nc <= 0 or nc > N: break
            if board[nr][nc] == 0: break
            if board[nr][nc] == color:
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    board[nr][nc] = color
                break


def count(num):
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == num:
                cnt += 1
    return cnt


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0] * (N + 1) for _ in range(N + 1)]
    board[N // 2][N // 2 + 1] = board[N // 2 + 1][N // 2] = 1
    board[N // 2][N // 2] = board[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):
        c, r, stone = map(int, input().split())
        change(r, c, stone)

    print('#{} {} {}'.format(T, count(1), count(2)))
