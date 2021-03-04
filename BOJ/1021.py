from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))
Q = deque(list(range(1, N + 1)))
ans = 0
for i in lst:
    l = len(Q)
    idx = Q.index(i)
    if idx < l - idx:
        while 1:
            if Q[0] == i:
                Q.popleft()
                break
            else:
                Q.append(Q.popleft())
                ans += 1
    else:
        while 1:
            if Q[0] == i:
                Q.popleft()
                break
            else:
                Q.insert(0, Q.pop())
                ans += 1
print(ans)