for T in range(int(input())):
    func = input()
    func.replace('RR', '')
    n = int(input())
    if n == 0:
        lst = input()
        lst = []
    else:
        lst = input()[1:-1].split(',')

    R_flag = error = True
    for p in func:
        if p == 'R':
            R_flag = not R_flag
        elif p == 'D':
            if R_flag:
                if lst:
                    lst.pop(0)
                else:
                    error = False
                    break
            else:
                if lst:
                    lst.pop()
                else:
                    error = False
                    break

    if error:
        if R_flag:
            print('[' + ','.join(lst) + ']')
        else:
            print('[' + ','.join(reversed(lst)) + ']')
    else:
        print('error')