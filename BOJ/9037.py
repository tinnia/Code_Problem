for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        if lst[i] % 2:
            lst[i] += 1
    cnt = 0
    tmp = [0] * N
    while 1:
        if len(set(lst)) == 1:
            break
        cnt += 1
        for i in range(N):
            tmp[i] = lst[-1+i]//2 + lst[i]//2
            if (lst[-1+i]//2 + lst[i]//2) % 2:
                tmp[i] += 1
        lst = tmp
        tmp = [0] * N
    print(cnt)