for T in range(1, int(input()) + 1):
    A, B, C, D = map(int, input().split())
    if not B and not C:
        if not A and D:
            tmp = '1' * (D + 1)
        elif not D and A:
            tmp = '0' * (A + 1)
        else:
            tmp = 'impossible'
    elif abs(B - C) > 1:
        tmp = 'impossible'
    elif B - C == 1:
        tmp = '0' * A + '01' * B + '1' * D
    elif C - B == 1:
        tmp = '1' * D + '10' * C + '0' * A
    else:
        tmp = '1' * D + '10' * B + '0' * A + '1'
    print("#{} {}".format(T, tmp))