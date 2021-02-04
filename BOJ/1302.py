N = int(input())
lst = {}
for _ in range(N):
    tmp = input()
    if tmp not in lst:
        lst[tmp] = 1
    else:
        lst[tmp] += 1

Max = max(lst.values())

ans = []
for k, v in lst.items():
    if v == Max:
        ans.append(k)

print(sorted(ans)[0])