N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    arr[x].append(y)

