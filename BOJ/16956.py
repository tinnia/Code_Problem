r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

flag = False
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < r and 0 <= nc < c:
                    if arr[nr][nc] == 'S':
                        flag = True
        elif arr[i][j] == 'S':
            continue
        else:
            arr[i][j] = 'D'
if flag:
    print(0)
else:
    print(1)
    for i in arr:
        print(''.join(i))
