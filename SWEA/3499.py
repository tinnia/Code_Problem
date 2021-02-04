for T in range(1, int(input()) + 1):
    N = int(input())
    lst = list(input().split())
    ans = []
    if N % 2:
        lst = lst + ['']
    for i in range(len(lst)//2):
        ans.append(lst[i])
        ans.append(lst[i + len(lst)//2])

    print('#{}'.format(T), end=' ')
    print(*ans)