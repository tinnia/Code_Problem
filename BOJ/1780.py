def func(x, y, n):
    global one, two, three
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                func(x, y, n//3)
                func(x, y + n// 3, n//3)
                func(x, y + 2*(n//3), n//3)
                func(x + n//3, y, n//3)
                func(x + n//3, y + n// 3, n//3)
                func(x + n//3, y + 2*(n//3), n//3)
                func(x + 2*(n//3), y, n//3)
                func(x + 2*(n//3), y + n// 3, n//3)
                func(x + 2*(n//3), y + 2*(n//3), n//3)
                return
    if check == -1:
        one += 1
        return
    elif check == 0:
        two += 1
        return
    else:
        three += 1
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
one = two = three = 0
func(0, 0, N)
print(one)
print(two)
print(three)