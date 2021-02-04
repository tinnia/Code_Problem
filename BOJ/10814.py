N = int(input())
lst = []
for _ in range(N):
    x, y = input().split(' ')
    lst.append((int(x), y))
lst.sort(key=lambda x: x[0])
for i in lst:
    print(*i)