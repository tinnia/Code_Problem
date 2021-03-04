for T in range(int(input())):
    n = int(input())
    lst = [input() for _ in range(n)]
    dic = {}
    for i in lst:
        dic[i] = 1

    flag = True
    for i in lst:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in dic and tmp != i:
                flag = False
    if flag:
        print('YES')
    else:
        print('NO')