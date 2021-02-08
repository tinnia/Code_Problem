from itertools import combinations


def solution(relation):
    answer = 0
    l = len(relation[0])
    stack = []
    for i in range(1, l+1):
        relate = combinations(range(l), i)
        for j in relate:
            tmp = [tuple(r[k] for k in j) for r in relation]
            if len(set(tmp)) == len(relation):
                stack.append(j)

    i = 0
    while 1:
        ans = []
        visit = [0] * len(stack)
        if 0 not in visit:
            break
        visit[i] = 1
        for j in range(i+1, len(stack)):
            if visit[j] == 0 and len(stack[i]) == len(set(stack[i]) & set(stack[j])):
                visit[j] = 1
            else:
                ans.append(stack[j])
        stack = ans
        answer += 1
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))