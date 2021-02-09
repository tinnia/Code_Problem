for T in range(1, int(input()) + 1):
    n = list(map(int, input()))
    cnt = ans = 0
    for i in range(len(n)):
        while 1:
            if cnt < i:
                cnt += 1
                ans += 1
            else:
                cnt += n[i]
                break
    print('#{} {}'.format(T, ans))