N, K = map(int, input().split())
time = N * 3600 + 60 * 60

ans = 0
for i in range(time):
    h = str(int(i/3600)) if len(str(int(i/3600))) == 2 else '0' + str(int(i/3600))
    i -= int(h) * 3600
    m = str(int(i/60)) if len(str(int(i/60))) == 2 else '0' + str(int(i/60))
    i -= int(m) * 60
    s = str(i) if len(str(i)) == 2 else '0' + str(i)
    if (h.count(str(K)) + m.count(str(K)) + s.count(str(K))) >= 1:
        ans += 1

print(ans)