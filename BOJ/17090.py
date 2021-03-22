import sys
sys.setrecursionlimit(10 ** 9)


def func(r, c):
    if visit[r][c] != -1:
        return visit[r][c]
    visit[r][c] = 0
    nr, nc = r, c
    if arr[r][c] == 'U':
        nr -= 1
    elif arr[r][c] == 'D':
        nr += 1
    elif arr[r][c] == 'L':
        nc -= 1
    else:
        nc += 1
    if 0 <= nr < N and 0 <= nc < M:
        visit[r][c] = func(nr, nc)
    else:
        visit[r][c] = 1
    return visit[r][c]


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[-1] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        answer += func(i, j)
print(answer)