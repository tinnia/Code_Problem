for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()

    cnt = i = 0
    for t in range(times[-1] + 1):
        if t != 0:
            if t % M == 0:
                cnt += K

        if t == times[i]:
            if cnt == 0:
                print('#{} Impossible'.format(T))
                break
            else:
                cnt -= 1
                i += 1

        if t == times[-1] and cnt != 0:
            print('#{} Possible'.format(T))
