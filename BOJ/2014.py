import heapq

K, N = map(int, input().split())
lst = list(map(int, input().split()))

answer = [x for x in lst]
for i in range(N):
    tmp = heapq.heappop(answer)
    for j in range(K):
        heapq.heappush(answer, tmp * lst[j])
        if tmp % lst[j] == 0:
            break
else:
    print(tmp)