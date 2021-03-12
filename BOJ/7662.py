import heapq

for _ in range(int(input())):
    K = int(input())
    heap = []
    for _ in range(K):
        rule, num = map(str, input().split())
        if rule == 'I':
            heapq.heappush(heap, )
        else:
            if heap:
                if num == '-1':
                    heapq.heappop(heap)


    if heap:
        print(max(heap), min(heap))
    else:
        print('EMPTY')