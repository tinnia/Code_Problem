def solution(tickets):
    dic = dict()
    for i in tickets:
        if i[0] not in dic:
            dic[i[0]] = []
        dic[i[0]].append(i[1])

    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            answer.append(stack.pop())
        else:
            dic[top].sort(reverse=True)
            stack.append(dic[top][-1])
            dic[top] = dic[top][:-1]
    return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
