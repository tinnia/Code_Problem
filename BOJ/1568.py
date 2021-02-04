n = int(input())
cnt, k = 0, 1

while n > 0:
    if k > n:
        k = 1
    n -= k
    cnt += 1
    k += 1
print(cnt)
