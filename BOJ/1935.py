N = int(input())
lst = input()
dict = {}
for i in range(1, N + 1):
    dict[chr(i + 64)] = int(input())

stack = []
for i in lst:
    if i.isalpha():
        stack.append(dict[i])
    else:
        if i == '*':
            stack[-2] = stack[-1] * stack[-2]
            stack.pop()
        elif i == '/':
            stack[-2] = stack[-2] / stack[-1]
            stack.pop()
        elif i == '+':
            stack[-2] = stack[-2] + stack[-1]
            stack.pop()
        elif i == '-':
            stack[-2] = stack[-2] - stack[-1]
            stack.pop()
print(f'{stack[0]:.2f}')