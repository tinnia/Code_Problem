X, Y, P1, P2 = map(int, input().split())
x = set(range(P1, 10**6, X))
y = set(range(P2, 10**6, Y))
ans = x & y
print(min(ans) if ans else -1)