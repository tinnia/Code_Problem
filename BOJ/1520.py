import sys

sys.setrecursionlimit(10 ** 9)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def func(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    if visit[r][c] != -1:
        return visit[r][c]
    visit[r][c] = 0
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if 0 <= nr < M and 0 <= nc < N:
            if arr[nr][nc] < arr[r][c]:
                visit[r][c] += func(nr, nc)
    return visit[r][c]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visit = [[-1] * N for _ in range(M)]
print(func(0, 0))
