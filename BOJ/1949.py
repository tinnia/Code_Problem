import sys

sys.setrecursionlimit(10 ** 9)

def dfs(x):
    visit[x] = 1
    dp[x][0] = people[x]
    for i in tree[x]:
        if not visit[i]:
            dfs(i)
            dp[x][0] += dp[i][1]
            dp[x][1] += max(dp[i][0], dp[i][1])


N = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

visit = [0 for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
dfs(1)
print(max(dp[1][0], dp[1][1]))