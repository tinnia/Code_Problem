for T in range(1, int(input()) + 1):
    lst = ['' for _ in range(15)]
    for _ in range(5):
        tmp = input()
        for i in range(len(tmp)):
            lst[i] += tmp[i]
    print('#{} '.format(T), end='')
    for i in range(len(lst)):
        print(lst[i], end='')
    print()