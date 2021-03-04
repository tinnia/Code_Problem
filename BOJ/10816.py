N = int(input())
lst = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
lst.sort()

dic = {}
for i in lst:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in card:
    try:
        print(dic[i], end=' ')
    except:
        print(0, end=' ')