import heapq

N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
Min = heap[0]
for _ in range(N - 1):
    for i in map(int, input().split()):
        if Min < i:
            heapq.heappush(heap, i)
            heapq.heappop(heap)
            Min = heap[0]
print(heap[0])