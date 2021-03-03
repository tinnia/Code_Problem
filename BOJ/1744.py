N = int(input())
pos, neg, one = [], [], []
for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num <= 0:  # 음수에선 0을 곱하는게 더 나으니깐
        neg.append(num)
    else:
        one.append(num)

pos.sort(reverse=True)
neg.sort()
ans = 0
if len(pos) % 2:
    for i in range(0, len(pos) - 1, 2):
        ans += pos[i] * pos[i + 1]
    ans += pos[-1]
else:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i + 1]

if len(neg) % 2:
    for i in range(0, len(neg) - 1, 2):
        ans += neg[i] * neg[i + 1]
    ans += neg[-1]
else:
    for i in range(0, len(neg), 2):
        ans += neg[i] * neg[i + 1]

print(ans + sum(one))
