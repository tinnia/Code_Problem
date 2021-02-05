for T in range(1, int(input()) + 1):
    word = list(input())
    cnt = int(input())
    idx = list(map(int, input().split()))
    lst = [0] * (len(word) + 1)
    for i in idx:
        lst[i] += 1

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > 0:
            word.insert(i, lst[i] * '-')

    print('#{} {}'.format(T, ''.join(word)))