def check(idx):
    for i in range(idx):
        if row[idx] == row[i] or abs(row[idx] - row[i]) == idx - i:
            return False
    return True

def dfs(idx):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        row[idx] = i
        if check(idx):
            dfs(idx + 1)


for T in range(1, int(input())+1):
    N = int(input())
    row = [0] * N
    ans = 0
    dfs(0)

    print('#{} {}'.format(T, ans))