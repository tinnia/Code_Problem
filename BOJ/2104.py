import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
answer, target = 1, [lst.pop()]
for i in lst[::-1]:
    if i > target[-1]:
        answer += 1
        target.append(i)
print(answer)