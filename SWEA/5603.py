for T in range(1, int(input())+1):
    N = int(input())
    lst = [int(input()) for _ in range(N)]

    avg = sum(lst)//len(lst)
    ans = 0
    for move in lst:
        ans += abs(move-avg)

    print('#{} {}'.format(T, ans//2))