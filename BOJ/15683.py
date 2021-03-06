from copy import deepcopy


def func(arr, cnt):
    global ans
    if cnt == len(lst):
        res = 0
        for i in range(N):
            res += arr[i].count(0)
        ans = min(ans, res)
        return
    x, y, num = lst[cnt]
    for dir in di[num]:
        tmp = deepcopy(arr)
        for d in dir:
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 6:
                    break
                elif tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
                nx += dx[d]
                ny += dy[d]
        func(tmp, cnt + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
di = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [1, 3], [2, 1], [3, 0]],
    4: [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]],
    5: [[0, 1, 2, 3]]
}
ans = 65
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 6 and arr[i][j] != 0:
            lst.append((i, j, arr[i][j]))
func(arr, 0)
print(ans)
