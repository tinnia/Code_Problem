import heapq

N, M = map(int, input().split())
arr = [[] for i in range(N + 1)]
inde = [0] * (N + 1)

heap = []
answer = []

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    inde[y] += 1

for i in range(1, N + 1):
    if inde[i] == 0:
        heapq.heappush(heap, i)
        print(heap)

while heap:
    data = heapq.heappop(heap)
    answer.append(data)
    for d in arr[data]:
        inde[d] -= 1
        if inde[d] == 0:
            heapq.heappush(heap, d)

for i in answer:
    print(i, end=' ')
