

def nCr(n, r, mod):
    lst = [0] * (n+1)
    lst[0] = 1
    for i in range(1, n+1):
        lst[i] = lst[i-1] * i % mod
    A = lst[n]
    B = pow(lst[r], (mod-2), mod) % mod
    C = pow(lst[n-r], (mod-2), mod) % mod
    return (A * B * C) % mod


for T in range(1, int(input()) + 1):
    N, R = map(int,input().split())
    answer = nCr(N, R, 1234567891)
    print('#{} {}'.format(T, answer))