N = int(input())
K = int(input())

answer = 0
l, h = 0, K
while l <= h:
    mid = (l + h) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt < K:
       l = mid + 1
    else:
        answer = mid
        h = mid - 1

print(answer)