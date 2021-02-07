def solution(s):
    cnt = i = 0
    while 1:
        cnt += s.count("0")
        s = format(len(s) - s.count("0"), 'b')
        i += 1
        if s == '1':
            break
    return [i, cnt]

print(solution("110010101001"))