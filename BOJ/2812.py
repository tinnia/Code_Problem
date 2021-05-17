N, K = map(int, input().split())
num = input()

ans, k = [], K
for i in range(N):
    while k > 0 and ans and ans[-1] < num[i]:
        ans.pop()
        k -= 1
    ans.append(num[i])
print(''.join(ans[:N-K]))