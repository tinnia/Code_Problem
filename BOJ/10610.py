N = input()
N = sorted(N, reverse=True)

if '0' not in N:
    print(-1)
else:
    tmp = 0
    for i in N:
        tmp += int(i)
    if tmp % 3 != 0:
        print(-1)
    else:
        print(''.join(N))