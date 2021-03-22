lst = list(input())
stack = []
for i in lst:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')':
        tmp = 0
        while len(stack) != 0:
            x = stack.pop()
            if x == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * tmp)
                break
            elif x == '[':
                print(0)
                exit(0)
            else:
                tmp += x
    elif i == ']':
        tmp = 0
        while len(stack) != 0:
            x = stack.pop()
            if x == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif x == '(':
                print(0)
                exit(0)
            else:
                tmp += x

answer = 0
for i in stack:
    if i == '(' or i == '[':
        print(0)
        break
    else:
        answer += i
print(answer)
