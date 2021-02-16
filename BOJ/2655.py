N = int(input())
arr = [(0, 0, 0, 0)]
for i in range(N):
    a, h, w = map(int, input().split())
    arr.append((a, w, h, i + 1))
arr.sort()

dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            print(dp[i], dp[j] + arr[i][2])
            dp[i] = max(dp[i], dp[j] + arr[i][2])

max_h = max(dp)
index = N
answer = []
while index != 0:
    if max_h == dp[index]:
        answer.append(arr[index][3])
        max_h -= arr[index][2]
    index -= 1

print(len(answer))
[print(i) for i in answer[::-1]]
