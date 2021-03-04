N = int(input())
lst = list(map(int, input().split()))
ans = [-1] * N
stack = [0]
i = 1
while stack and i < N:
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack[-1]] = lst[i]
        stack.pop()
    stack.append(i)
    i += 1
print(*ans)