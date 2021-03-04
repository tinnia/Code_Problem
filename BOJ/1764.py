N, M = map(int, input().split())
arr1 = set([input() for _ in range(N)])
arr2 = set([input() for _ in range(M)])

arr = sorted(list(arr1 & arr2))
print(len(arr))
for i in arr:
    print(i)