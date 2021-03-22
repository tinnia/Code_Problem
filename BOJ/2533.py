N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

print(tree)

dp = [[0,0] for _ in range(N + 1)]

visit = [0] * (N + 1)

def func(x):
    visit[x] = 1
    print(visit)
    dp[x][0] = 1
    dp[x][1] = 0
    print(dp)
    for i in tree[x]:
        print(i)
        if not visit[i]:
            func(i)
            dp[x][0] += dp[i][1]
            dp[x][1] += max(dp[i][0], dp[i][1])
            print(dp)


func(1)
print(dp)