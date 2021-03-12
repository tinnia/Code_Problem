from collections import deque
import sys
input = sys.stdin.readline


def bfs(x):
    visit[x] = 1
    Q = deque([x])
    while Q:
        tmp = Q.popleft()
        for i in arr[tmp]:
            if visit[i]:
                continue
            dep[i] = dep[tmp] + 1
            visit[i] = 1
            parent[i] = tmp
            Q.append(i)


def find(x, y):
    if dep[x] < dep[y]:
        x, y = y, x
    while dep[x] != dep[y]:
        x = parent[x]
    while x != y:
        x, y = parent[x], parent[y]
    return x


N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dep = [0] * (N + 1)
visit = [0] * (N + 1)
parent = [0] * (N + 1)
bfs(1)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(find(a, b))
