for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tmp = [0] * N
    tmp[M] = 1

    cnt = 0
    while 1:
        if lst[0] == max(lst):
            cnt += 1
            if tmp[0]:
                print(cnt)
                break
            else:
                lst.pop(0)
                tmp.pop(0)
        else:
            lst.append(lst.pop(0))
            tmp.append(tmp.pop(0))
