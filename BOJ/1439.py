s = input()
ans = 0
tmp = s[0]
for i in range(1, len(s)):
    if s[i] != tmp:
        tmp = s[i]
        ans += 1
if ans % 2:
    print(ans // 2 + 1)
else:
    print(ans // 2)
