prime = [2]
for i in range(3, int((10 ** 7) ** 0.5), 2):
    for p in prime:
        if i % p == 0:
            break
    else:
        prime.append(i)

answer = []
for T in range(1, int(input()) + 1):
    A = int(input())
    ans = 1
    if A ** 0.5 != int(A ** 0.5):
        for i in prime:
            cnt = 0
            while not A % i:
                A //= i
                cnt += 1
            if cnt % 2:
                ans *= i
            if A == 1 or i > A:
                break
        if A > 1:
            ans *= A
    answer.append('#{} {}'.format(T, ans))

for i in answer:
    print(i)
