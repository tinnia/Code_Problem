T=int(input())
num = []
for tc in range(T):
    n=input()
    while 1:
        tmp = 0
        if len(n) == 1:
            num.append(n)
            break
        for i in range(len(n)):
            tmp += int(n[i])
        n = str(tmp)
for tc in range(T):
    print('#{} {}'.format(tc+1,num[tc]))