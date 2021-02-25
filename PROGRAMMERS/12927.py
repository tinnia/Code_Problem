import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for i in range(n):
        tmp = heapq.heappop(works) + 1
        heapq.heappush(works, tmp)
    return sum([i ** 2 for i in works])


print(solution(4, [4, 3, 3]))
