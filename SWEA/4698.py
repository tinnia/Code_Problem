lst = [1] * 1000001
lst[0] = lst[1] = 0
tmp = []

for i in range(2, 1000001):
    if lst[i]:
        tmp.append(i)
        for j in range(2 * i, 1000001, i):
            lst[j] = 0

for T in range(1, int(input()) + 1):
    d, a, b = map(int, input().split())
    ans = 0
    for j in tmp:
        if a <= j <= b:
            if str(d) in str(j):
                ans += 1
        if j > b:
            break

    print('#{} {}'.format(T, ans))
