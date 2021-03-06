def func(x, y, n):
    global white, blue
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                func(x, y, n // 2)
                func(x, y + n // 2, n // 2)
                func(x + n // 2, y, n // 2)
                func(x + n // 2, y + n // 2, n // 2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0
func(0, 0, N)
print(white)
print(blue)