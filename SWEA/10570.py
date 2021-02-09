def check(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[-1 - i]:
            return False
    else:
        return True


for T in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        if i ** 0.5 == int(i ** 0.5) and check(i) and check(int(i ** 0.5)):
            cnt += 1
    print('#{} {}'.format(T, cnt))
