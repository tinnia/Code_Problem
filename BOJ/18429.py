from itertools import permutations

N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in permutations(lst, N):
    weight = 500
    for j in range(N):
        weight += i[j] - K
        if weight < 500:
            break
    else:
        ans += 1
print(ans)