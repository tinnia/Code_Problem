from collections import deque


def bfs(s):
    visit = [0] * (N + 1)
    visit[s] = 1
    ans = 0
    Q = deque([s])
    while Q:
        x = Q.popleft()
        for i in lst[x]:
            if visit[i] == 0:
                visit[i] = 1
                ans += 1
                Q.append(i)
    return ans


for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)
    print(bfs(1))



# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         input()
#     print(N-1)