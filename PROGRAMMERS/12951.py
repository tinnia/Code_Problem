def solution(s):
    answer = ''
    s = s.lower()
    lst = s.split(' ')
    for i in lst:
        i = i.capitalize()
        answer += i + ' '
    return answer
