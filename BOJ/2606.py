def dfs(x):
    global cnt
    visit[x] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and arr[x][i] == 1:
            dfs(i)
            cnt += 1


n = int(input())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1

cnt = 0
visit = [0] * (n + 1)
dfs(1)
print(cnt)