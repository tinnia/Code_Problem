string = list(input())
M = int(input())
left, right = string, []
cursor = len(string)
for _ in range(M):
    tmp = list(input().split())
    if tmp[0] == 'L' and left:
        right.append(left.pop())
    elif tmp[0] == 'D' and right:
        left.append(right.pop())
    elif tmp[0] == 'B' and left:
        left.pop()
    elif tmp[0] == 'P':
        left.append(tmp[1])
print(''.join(left + right[::-1]))