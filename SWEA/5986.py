lst = [1] * 1000
lst[0] = lst[1] = 0
tmp = []
for i in range(2, 1000):
    if lst[i]:
        tmp.append(i)
        for j in range(2 * i, 1000, i):
            lst[j] = 0

for T in range(1, int(input()) + 1):
    n = int(input())
    answer = 0
    for i in range(len(tmp)):
        for j in range(i, len(tmp)):
            if n - (tmp[i] + tmp[j]) in tmp[j:]:
                answer += 1
    print('#{} {}'.format(T, answer))
