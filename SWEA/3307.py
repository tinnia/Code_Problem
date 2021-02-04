for T in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = [1] * N
    for i in range(1, N):
        for j in range(i):
            if lst[j] < lst[i]:
                result[i] = max(result[i], result[j] + 1)
    print(max(result))