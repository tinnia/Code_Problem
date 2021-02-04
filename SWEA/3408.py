# for T in range(1, int(input()) + 1):
#     N = int(input())
#     a = b = c = 0
#     for i in range(1, N + 1):
#         a += i
#         b += (i * 2 - 1)
#         c += i * 2
#
#     print('#{} {} {} {}'.format(T, a, b, c))

for T in range(1, int(input()) + 1):
    N = int(input())
    a = N * (N + 1) // 2
    b = N * (N * 2) // 2
    c = N * ((N + 1) * 2) // 2
    print('#{} {} {} {}'.format(T, a, b, c))