from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))
visit = set(lst)

Q = deque()
for i in lst:
    Q.append((i - 1, 1))
    Q.append((i + 1, 1))

ans = 0
while K:
    x, sam = Q.popleft()
    if x in visit:
        continue
    visit.add(x)
    ans += sam
    Q.append((x - 1, sam + 1))
    Q.append((x + 1, sam + 1))
    K -= 1
print(ans)