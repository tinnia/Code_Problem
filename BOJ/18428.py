from itertools import combinations
from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check(r, c, d, arr):
    global N
    for i in range(1, N):
        nr = r + (dr[d] * i)
        nc = c + (dc[d] * i)
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] == 'O':
                return True
        else:
            break
    return True


def wall(lst, arr):
    for i in lst:
        r, c = i
        arr[r][c] = 'O'
    for t in teachers:
        for i in range(4):
            if not check(t[0], t[1], i, arr):
                return False
    return True


N = int(input())
arr = [list(input().split()) for _ in range(N)]
blank, teachers = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            blank.append((i, j))
            arr[i][j] = ''
        elif arr[i][j] == 'T':
            teachers.append((i, j))

for i in combinations(blank, 3):
    if wall(i, deepcopy(arr)):
        print('YES')
        break
else:
    print('NO')
