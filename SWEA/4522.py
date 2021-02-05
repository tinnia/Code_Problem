for T in range(1, int(input()) + 1):
    st = list(input())
    flag = True
    for i in range(len(st) // 2):
        if st[i] == st[-1 - i] or st[i] == '?' or st[-1 - i] == '?':
            continue
        else:
            flag = False
            break
    if flag:
        print('#{} Exist'.format(T))
    else:
        print('#{} Not exist'.format(T))
