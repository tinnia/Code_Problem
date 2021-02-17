from collections import deque


def dfs(i):
    print(i, end=' ')
    visit[i] = 1
    for j in range(1, n + 1):
        if visit[j] == 0 and arr[i][j] == 1:
            visit[j] = 1
            dfs(j)


def bfs(i):
    visited = [0] * (n + 1)
    Q = deque()
    Q.append(i)
    visited[i] = 1
    ans = [i]
    while Q:
        v = Q.popleft()
        for j in range(1, n + 1):
            if arr[v][j] == 1 and visited[j] == 0:
                visited[j] = 1
                ans.append(j)
                Q.append(j)
    print(*ans)


n, m, v = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

visit = [0] * (n + 1)
dfs(v)
print()
bfs(v)
