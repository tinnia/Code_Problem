N, M = map(int, input().split())
answer = 1
for i in range(N, N-M, -1):
    answer *= i
for i in range(M, 1, -1):
    answer //= i
print(answer)