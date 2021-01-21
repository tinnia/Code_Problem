for _ in range(10):
    T = int(input())
    pwd = list(map(int, input().split()))

    i = 1
    while 1:
        pwd[0] -= i
        if pwd[0] <= 0:
            pwd = pwd[1:8]
            pwd.append(0)
            break
        pwd.append(pwd[0])
        pwd = pwd[1:9]

        i += 1
        if i == 6:
            i = 1
    print(f'#{T}', *pwd)
