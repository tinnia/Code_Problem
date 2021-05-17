for _ in range(int(input())):
    N, M = map(int, input().split())
    answer = 1
    # mCn = m!/n!(m-n)!
    for i in range(M, M - N, -1):
        answer *= i
    for i in range(N, 1, -1):
        answer //= i

    print(answer)