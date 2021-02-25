def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * ((M - 1) * 2 + N) for _ in range((M - 1) * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[M + i - 1][M + j - 1] = lock[i][j]

    def remove(r, c):
        for i in range(M):
            for j in range(M):
                board[i + r][j + c] -= key[i][j]

    def check(r, c):
        for i in range(M):
            for j in range(M):
                board[i + r][j + c] += key[i][j]
        for i in range(N):
            for j in range(N):
                if board[M + i - 1][M + j - 1] != 1:
                    return False
        return True

    for _ in range(4):
        for i in range(M + N - 1):
            for j in range(M + N - 1):
                if check(i, j):
                    return True
                remove(i, j)
        key = list(zip(*key[::-1]))
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
