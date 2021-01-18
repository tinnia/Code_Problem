for T in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    Max = -1111
    Sum = 0
    for i in range(N):
        Sum += lst[i]
        if Max < Sum:
            Max = Sum
        if Sum < 0:     # Sum이 0보다 작아지면 Reset 후 다음 index부터 다시 더하기
            Sum = 0
    print('#{} {}'.format(T, Max))