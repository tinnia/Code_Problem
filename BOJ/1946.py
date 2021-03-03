for _ in range(int(input())):
    N = int(input())
    lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])

    ans, pre = 0, 100001
    for i, j in lst:
        if j < pre:
            ans += 1
            pre = j
    print(ans)
