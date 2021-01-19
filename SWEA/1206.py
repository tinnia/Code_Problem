for T in range(1, 11):
    l = int(input())
    building = list(map(int, input().split()))

    ans = 0
    for i in range(2, l-2):
        Max = max(building[i-2], building[i-1], building[i+1], building[i+2])
        if building[i] - Max > 0:
            ans += building[i] - Max

    print('#{} {}'.format(T, ans))