def solution(scoville, K):
    import heapq
    scoville.sort()
    answer = 0

    while scoville:
        if scoville[0] >= K:
            return answer
        x = heapq.heappop(scoville)
        if scoville:
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x + (y * 2))
        answer += 1

    return -1



print(solution([1, 2, 3, 9, 10, 12], 7))
