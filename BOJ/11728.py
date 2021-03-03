N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []
a = b = 0
while a <= N and b <= M:
    if a == N:
        ans += B[b:]
        break
    if b == M:
        ans += A[a:]
        break
    if A[a] >= B[b]:
        ans.append(B[b])
        b += 1
    elif B[b] > A[a]:
        ans.append(A[a])
        a += 1
print(*ans)
