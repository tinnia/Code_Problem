for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        lst[x][y] = 1
        lst[y][x] = 1

    cnt = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(j + 1, N + 1):
                if lst[i][j] and lst[j][k] and lst[k][i]:
                    cnt += 1

    print('#{} {}'.format(T, cnt))
