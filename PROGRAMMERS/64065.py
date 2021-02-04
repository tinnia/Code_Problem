def solution(s):
    answer = []
    s = s[2:-2].split("},{").sort(key=len)
    for i in s:
        li = i.split(',')
        for j in li:
            if int(j) not in answer:
                answer.append(int(j))
    return answer