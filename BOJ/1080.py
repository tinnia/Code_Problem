N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


def change(x, y):
    for r in range(x, x + 3):
        for c in range(y, y + 3):
            A[r][c] = 1 - A[r][c]


def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True


cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            cnt += 1
            change(i, j)

if check():
    print(cnt)
else:
    print(-1)
