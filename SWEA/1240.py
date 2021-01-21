rule = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = [list(input()) for _ in range(N)]

    pwd = tmp = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if nums[i][j] == '1':
                tmp = nums[i][j-55:j+1]
                break

    for i in range(0, 56, 7):
        pwd.append(rule[str(''.join(tmp[i:i+7]))])

    ans = 0
    for i in range(8):
        if i % 2:
            ans += pwd[i]
        else:
            ans += pwd[i]*3
    if ans % 10:
        print('#{} 0'.format(T))
    else:
        print('#{} {}'.format(T, sum(pwd)))