def func(x, y, n):
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                print('(', end='')
                func(x, y, n // 2)
                func(x, y + n // 2, n // 2)
                func(x + n // 2, y, n // 2)
                func(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if check == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
func(0, 0, N)

