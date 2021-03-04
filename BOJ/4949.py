while 1:
    tmp = input()
    if tmp == '.':
        break
    stack, flag = [], True
    for i in tmp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print('yes')
    else:
        print('no')