for T in range(1, int(input()) + 1):
    N = int(input())
    lst = list(input().split())
    ans = []
    cnt = 0
    for i in range(len(lst)):
        if '.' in lst[i] or '?' in lst[i] or '!' in lst[i]:
            if len(lst[i]) == 2 and lst[i][0].isupper():
                cnt += 1
            elif lst[i][:-1].isalpha():
                if lst[i][0].isupper() and lst[i][1:-1].islower():
                    cnt += 1
            ans.append(cnt)
            cnt = 0
        else:
            if len(lst[i]) == 1 and lst[i][0].isupper():
                cnt += 1
            elif lst[i].isalpha():
                if lst[i][0].isupper() and lst[i][1:].islower():
                    cnt += 1
    print('#{}'.format(T), end=' ')
    print(*ans)