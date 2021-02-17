from collections import deque

import sys

input = sys.stdin.readline


def bfs(i):
    Q = deque()
    Q.append(i)
    visit = [0] * (n + 1)
    cnt = visit[i] = 1
    while Q:
        x = Q.popleft()
        for j in arr[x]:
            if not visit[j]:
                visit[j] = 1
                cnt += 1
                Q.append(j)
    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[y].append(x)

ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = bfs(i)

for i in range(1, n + 1):
    if ans[i] == max(ans):
        print(i, end=' ')
