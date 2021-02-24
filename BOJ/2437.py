N = int(input())
lst = sorted(list(map(int, input().split())))

ans = 1
for i in lst:
    if i <= ans:
        ans += i
    else:
        break
print(ans)
