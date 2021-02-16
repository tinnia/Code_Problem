from collections import Counter

for T in range(1, int(input()) + 1):
    st = input()
    tmp = [i for i, v in Counter(st).items() if v % 2]
    tmp.sort()
    if len(tmp) == 0:
        print('#{} Good'.format(T))
    else:
        print('#{}'.format(T),end=' ')
        for i in range(len(tmp)):
            print(tmp[i], end='')
        print()
