N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if lst[i] <= K:
        ans += K//lst[i]
        K %= lst[i]
print(ans)