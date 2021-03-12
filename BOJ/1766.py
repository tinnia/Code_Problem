# import heapq
#
# N, M = map(int, input().split())
# arr = [[] for i in range(N + 1)]
# inde = [0] * (N + 1)
#
# heap = []
# answer = []
#
# for _ in range(M):
#     x, y = map(int, input().split())
#     arr[x].append(y)
#     inde[y] += 1
#
# for i in range(1, N + 1):
#     if inde[i] == 0:
#         heapq.heappush(heap, i)
#         print(heap)
#
# while heap:
#     data = heapq.heappop(heap)
#     answer.append(data)
#     for d in arr[data]:
#         inde[d] -= 1
#         if inde[d] == 0:
#             heapq.heappush(heap, d)
#
# for i in answer:
#     print(i, end=' ')
import heapq

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
rank = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    rank[y] += 1

print(arr, rank)
heap = []
for i in range(1, N + 1):
    if rank[i] == 0:
        heapq.heappush(heap, i)

print(heap)
answer = []
while heap:
    tmp = heapq.heappop(heap)
    answer.append(tmp)
    for i in arr[tmp]:
        rank[i] -= 1
        if rank[i] == 0:
            heapq.heappush(heap, i)
print(*answer)