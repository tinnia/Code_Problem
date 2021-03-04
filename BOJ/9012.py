for _ in range(int(input())):
    tmp = input()
    stack, flag = [], True
    for i in tmp:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print('YES')
    else:
        print('NO')