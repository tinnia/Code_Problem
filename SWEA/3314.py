for T in range(1, int(input())+1):
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        if lst[i] < 40:
            lst[i] = 40
    print('#{} {}'.format(T, int(sum(lst)/len(lst))))