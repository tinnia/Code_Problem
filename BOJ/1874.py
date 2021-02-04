n = int(input())
stack, ans, cnt = [], [], 1

for i in range(n):
    tmp = int(input())

    while cnt <= tmp:
        stack.append(cnt)
        ans.append("+")
        cnt += 1

    if stack[-1] == tmp:
        stack.pop()
        ans.append("-")
    else:
        ans = ["NO"]
        break

for i in range(len(ans)):
    print(ans[i])