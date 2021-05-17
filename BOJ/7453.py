N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

a_b = dict()
for i in range(N):
    for j in range(N):
        tmp = A[i] + B[j]
        if tmp in a_b:
            a_b[tmp] += 1
        else:
            a_b[tmp] = 1

answer = 0
for i in range(N):
    for j in range(N):
        tmp = -(C[i] + D[j])
        if tmp in a_b:
            answer += a_b[tmp]
print(answer)