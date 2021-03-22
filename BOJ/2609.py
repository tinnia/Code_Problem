def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


N, M = map(int, input().split())
num = gcd(N, M)
print(num)
print(N * M // num)
