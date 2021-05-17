idx = 1
while 1:
    stack = []
    cnt = 0
    s = input()
    if '-' in s:
        break
    for i in range(len(s)):
        if not stack and s[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    cnt += len(stack) // 2
    print(idx, ". ", cnt, sep='')
    idx += 1