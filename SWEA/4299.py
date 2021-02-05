for T in range(1, int(input()) + 1):
    d, h, m = map(int, input().split())
    ans = 0
    if d == 11 and h == 11 and m == 11:
        print('#{} 0'.format(T))
    elif d < 11 or (d == 11 and h < 11) or (d == 11 and h < 11 and m < 11):
        print('#{} -1'.format(T))
    else:
        ans += (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)
        print('#{} {}'.format(T, ans))
