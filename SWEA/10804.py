for T in range(1, int(input()) + 1):
    rule = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    st = input()
    answer = ''
    for i in range(len(st)-1, -1, -1):
        answer += rule[st[i]]

    print('#{} {}'.format(T, answer))
