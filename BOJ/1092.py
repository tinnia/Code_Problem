import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if box[0] > lst[0]:
    print(-1)
    exit()

ans = 0
while box:
    ans += 1
    for i in lst:
        for j in range(len(box)):
            if i >= box[j]:
                del box[j]
                break

print(ans)