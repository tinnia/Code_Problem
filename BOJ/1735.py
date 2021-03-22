def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


A, B = map(int, input().split())
C, D = map(int, input().split())
num1 = B * D // gcd(B, D)
print(A * num1 // B + C * num1 // D, num1)