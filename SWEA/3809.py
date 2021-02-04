for T in range(1, int(input()) + 1):
    N = int(input())
    tmp = ''
    while len(tmp) < N:
        tmp += ''.join(map(str, input().split()))

    num = ans = 0
    while 1:
        if str(num) not in tmp:
            ans = num
            break
        num += 1
    print('#{} {}'.format(T, ans))