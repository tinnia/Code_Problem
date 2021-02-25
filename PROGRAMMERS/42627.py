def solution(jobs):
    import heapq

    cnt = current = answer = 0
    last = -1
    heap = []
    jobs.sort()

    while cnt < len(jobs):
        for job in jobs:
            if last < job[0] <= current:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            w, d = heapq.heappop(heap)
            last = current
            current += w
            answer += current - d
            cnt += 1
        else:
            current += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
