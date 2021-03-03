N = int(input())

prime, lst = [0] * (N + 1), []
for i in range(2, N + 1):
    if prime[i] == 0:
        lst.append(i)
    for j in range(i ** 2, N + 1, i):
        prime[j] = 1

ans = st = ed = 0
while 1:
    if sum(lst[st:ed]) >= N:
        st += 1
    elif ed == len(lst):
        break
    else:
        ed += 1
    if sum(lst[st:ed]) == N:
        ans += 1
print(ans)
