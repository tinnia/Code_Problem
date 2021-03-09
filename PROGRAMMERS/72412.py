from itertools import combinations
from collections import defaultdict


def solution(info, query):
    dic = defaultdict(list)
    for i in info:
        rule, score = i.split(' ')[:-1], i.split(' ')[-1]
        for num in range(5):
            for r in combinations(rule, num):
                dic[''.join(r)].append(int(score))

    for key in dic:
        dic[key].sort()

    answer = []
    for q in query:
        tmp = q.replace(' and ', '').replace('-', '')
        rule, score = tmp.split(' ')[0], tmp.split(' ')[1]
        if rule in dic:
            temp = dic[rule]
            if temp:
                st, ed = 0, len(temp) - 1
                while st <= ed:
                    mid = (st + ed)//2
                    if temp[mid] >= int(score):
                        ed = mid - 1
                    else:
                        st = mid + 1
                answer.append(len(temp) - st)
        else:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                   "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                   "- and - and - and chicken 100", "- and - and - and - 150"]))
