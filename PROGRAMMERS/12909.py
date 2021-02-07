def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        if stack:
            if s[i] == ')':
                stack.pop()
        else:
            answer = False
            break
    if stack:
        answer = False
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))