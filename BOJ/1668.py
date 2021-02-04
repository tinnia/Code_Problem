def func(lst):
    tmp = lst[0]
    cnt = 1
    for i in lst:
        if i > tmp:
            cnt += 1
        tmp = max(tmp, i)
    return cnt


N = int(input())
lst = [int(input()) for _ in range(N)]

print(func(lst))
lst.reverse()
print(func(lst))