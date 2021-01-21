for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    cnt = 0
    for time in range(people[-1]+1):



        if answer:
            print('#{} Possible'.format(T))
        else:
            print('#{} Impossible'.format(T))
