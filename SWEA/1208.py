for T in range(1, 11):
    num = int(input())
    box = list(map(int, input().split()))
    for i in range(num):
        Max_i, Min_i = box.index(max(box)), box.index(min(box))
        box[Max_i] -= 1
        box[Min_i] += 1

    print('#{} {}'.format(T, max(box)-min(box)))