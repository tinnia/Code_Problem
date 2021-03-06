def func(a, b):
    if b == 1:
        return a % c
    else:
        tmp = func(a, b // 2)
        if b % 2:
            return a * tmp * tmp % c
        else:
            return tmp * tmp % c


a, b, c = map(int, input().split())
print(func(a, b))

# A, B, C = map(int, input().split())
# print(pow(A, B, C))