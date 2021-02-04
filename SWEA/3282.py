def func(idx, v_s, c_s):
    global ans
    if idx == N:
        return
    if v_s + lst[idx][0] > K:
        return
    if c_s + lst[idx][1] > ans:
        ans = c_s + lst[idx][1]
    func(idx + 1, v_s, c_s)
    func(idx + 1, v_s + lst[idx][0], c_s + lst[idx][1])


T = int(input())
N, K = map(int, input().split())
ans = 0
lst = []
for _ in range(N):
    v, c = map(int, input().split())
    lst.append((v, c))

for i in range(N):
    func(i, lst[i][0], lst[i][1])

print('#{} {}'.format(T, ans))

