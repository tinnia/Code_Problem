N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
st, ed, ans = 0, 0, 2e9 + 1

while st < N and ed < N:
    tmp = arr[ed] - arr[st]
    if tmp >= M:
        ans = min(ans, tmp)
        st += 1
    else:
        ed += 1
print(ans)
