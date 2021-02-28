def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def backtrack(x):
    global res
    if x == N:
        res += 1
        return
    for i in range(N):
        row[x] = i
        if check(x):
            backtrack(x + 1)


N = int(input())
row = [0] * N
res = 0
backtrack(0)
print(res)


















