N = int(input())
value = [0] + list(map(int, input().split()))

tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

def dfs(x):
    visit[x] = 1
    dp[x][0] = tree[x]


dp = [[0, 0] for _ in range(N + 1)]
visit = [0] * (N + 1)
dfs(1)