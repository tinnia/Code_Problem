dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
tank = '^v<>'
dic = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

for T in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    Map = [list(input()) for _ in range(H)]
    N = int(input())
    word = input()

    r = c = d = 0
    for i in range(H):
        for j in range(W):
            if Map[i][j] == '<' or Map[i][j] == '^' or Map[i][j] == '>' or Map[i][j] == 'v':
                r, c, d = i, j, tank.index(Map[i][j])

    for wd in word:
        if wd == 'S':
            nr, nc = r + dr[d], c + dc[d]
            while 1:
                if nr < 0 or nc < 0 or nr >= H or nc >= W or Map[nr][nc] == '#':
                    break
                if Map[nr][nc] == '*':
                    Map[nr][nc] = '.'
                    break
                nr, nc = nr + dr[d], nc + dc[d]
        else:
            d = dic[wd]
            Map[r][c] = tank[d]
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= H or nc >= W: continue
            if Map[nr][nc] == '.':
                Map[nr][nc] = tank[d]
                Map[r][c] = '.'
                r, c = nr, nc

    print('#{}'.format(T), end=' ')
    for i in range(H):
        print(''.join(Map[i]))
