def dfs(r, c, d, cnt):
    global flag
    if cnt == 5:
        flag = True
        return
    if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N:
        if lst[r + dr[d]][c + dc[d]] == 'o':
            dfs(r + dr[d], c + dc[d], d, cnt + 1)
        else:
            return
    else:
        return


dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

for T in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    flag = False
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if flag:
                break
            if lst[i][j] == 'o':
                for d in range(4):
                    if d == 0:
                        if N - j >= 5:
                            dfs(i, j, d, 1)
                    elif d == 1:
                        if N - j >= 5 and N - i >= 5:
                            dfs(i, j, d, 1)
                    elif d == 2:
                        if N - i >= 5:
                            dfs(i, j, d, 1)
                    else:
                        if N - i >= 5 and j >= 4:
                            dfs(i, j, d, 1)
                    if flag:
                        break

    if flag:
        print('#{} YES'.format(T))
    else:
        print('#{} NO'.format(T))
