def solution(d, budget):
    d.sort()
    cnt = 0
    for val in d:
        if val <= budget:
            budget -= val
            cnt += 1
    return cnt