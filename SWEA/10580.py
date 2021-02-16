for T in range(1, int(input()) + 1):
    n = int(input())
    cnt = 0
    lst = []

    for _ in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort()
    print(lst)

    for i in range(n):
        a, b = lst[i][0], lst[i][1]
        for j in range(i + 1, n):
            if lst[j][0] > a and lst[j][1] < b:
                cnt += 1

    print("#{} {}".format(T, cnt))
