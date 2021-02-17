N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = 0
for i in range(N):
    ans += abs(i + 1 - lst[i])
print(ans)
