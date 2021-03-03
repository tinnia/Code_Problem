N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = tmp = sum(lst[:K])
for i in range(K, N):
    tmp += lst[i] - lst[i-K]
    ans = max(ans, tmp)
print(ans)