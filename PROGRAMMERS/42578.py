def solution(clothes):
    answer = 1
    dic = dict()

    for n, k in clothes:
        if k not in dic:
            dic[k] = 1
        else:
            dic[k] += 1
    for i in dic.values():
        answer *= (i+1)
    return answer -1