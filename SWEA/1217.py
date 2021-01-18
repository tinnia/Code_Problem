def power(num, cnt):
    if cnt == 1:
        return num
    return power(num * N, cnt - 1)

for _ in range(10):
    T = int(input())
    N, M = map(int, input().split())

    print("#{} {}".format(T, power(N, M)))