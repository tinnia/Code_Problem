for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    tmp = format(M, 'b')
    if len(tmp) < N:
        print("#{} OFF".format(T))
    else:
        if "0" in tmp[-N:]:
            print('#{} OFF'.format(T))
        else:
            print('#{} ON'.format(T))