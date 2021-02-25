import heapq


def solution(operations):
    answer = []
    for oper in operations:
        oper = oper.split()
        if oper[0] == 'I':
            heapq.heappush(answer, int(oper[1]))
        if oper[0] == 'D' and answer:
            if oper[1] == '-1':
                heapq.heappop(answer)
            else:
                answer.pop()
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
