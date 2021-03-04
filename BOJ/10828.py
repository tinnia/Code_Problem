import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    tmp = input().split()
    if tmp[0] == "push":
        stack.append(int(tmp[1]))
    elif tmp[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack.pop())
    elif tmp[0] == "size":
        print(len(stack))
    elif tmp[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif tmp[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])