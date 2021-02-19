n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    group = input()
    dic[group] = []
    for _ in range(int(input())):
        dic[group].append(input())
    dic[group].sort()
# print(dic)
for _ in range(m):
    tmp = input()
    if int(input()):
        for k, v in dic.items():
            if tmp in v:
                print(k)
                break
    else:
        for i in dic[tmp]:
            print(i)
