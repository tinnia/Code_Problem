for tc in range(1, int(input()) + 1):
    word = list(input())
    vw = 'aeiou'
    word2 = []
    for i in range(len(word)):
        if word[i] not in vw:
            word2.append(word[i])
    print('#{} {}'.format(tc, ''.join(word2)))
