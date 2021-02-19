N = int(input())
K = int(input())
lst = list(map(int, input().split()))

if K >= N:
    print(0)
else:
    lst.sort()
    gap = []
    for i in range(len(lst)-1):
        gap.append(lst[i+1] - lst[i])
    gap.sort(reverse=True)
    for _ in range(K-1):
        gap.pop(0)
    print(sum(gap))