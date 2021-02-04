def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)

print(solution([3,0,6,1,5]))