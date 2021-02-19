N, L, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if lst[i][1] <= L:
        lst[i] = 140
    elif lst[i][1] > L >= lst[i][0]:
        lst[i] = 100
    else:
        lst[i] = 0
lst.sort(reverse=True)
print(sum(lst[:K]))