string = input()
bomb = input()
stack = []
for st in string:
    stack.append(st)
    if st == bomb[-1] and len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')