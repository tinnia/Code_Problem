def check(i, j, visit):
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if (nr, nc) in visit:
            return False
    else:
        if (i, j) in visit:
            return False
        else:
            return True

def dfs(visit, cnt):
    global answer
    if cnt >= answer: return
    if len(visit) == 15:
        answer = min(answer, cnt)
    for i in range(1, N -1):
        for j in range(1, N - 1):
            if check(i, j, visit):
                tmp = [(i,j)]
                tmp_cnt = arr[i][j]
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    tmp.append((nr, nc))
                    tmp_cnt += arr[nr][nc]
                dfs(visit + tmp, cnt + tmp_cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
dfs([], 0)
print(answer)
