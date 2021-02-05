for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    cnt = 0
    for i in range(k):
        cnt += score[-1 - i]
    print('#{} {}'.format(tc, cnt))
