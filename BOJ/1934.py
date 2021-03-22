def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


for T in range(int(input())):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))