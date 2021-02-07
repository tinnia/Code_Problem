def solution(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    if s:
        return 0
    else:
        return 1

print(solution("baabaa"))
print(solution("cdcd"))

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1