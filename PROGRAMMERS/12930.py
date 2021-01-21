def solution(s):
    answer = ''
    tmp = list(s.split(' '))
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if j % 2:
                answer += tmp[i][j].lower()
            else:
                answer += tmp[i][j].upper()
        answer += ' '
    return answer[:-1]

print(solution('try hello world'))