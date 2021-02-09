for T in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    s = sum(lst) // N
    ans = 0
    for i in lst:
        if i <= s:
            ans += 1

    print('#{} {}'.format(T, ans))