st = input()

answer = stack = ''
i = 0
while 1:
    if i == len(st):
        break
    if st[i] == '<':
        if stack:
            answer += stack[::-1]
            stack = ''
        j = 0
        while 1:
            if st[i + j] == '>':
                answer += '>'
                i += j + 1
                break
            answer += st[i+j]
            j += 1
    elif st[i] == ' ':
        if stack:
            answer += stack[::-1] + ' '
            stack = ''
        i += 1
    else:
        stack += st[i]
        i += 1
answer += stack[::-1]

print(answer)
