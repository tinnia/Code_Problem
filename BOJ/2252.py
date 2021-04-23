from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
in_degree[0] = -1

tree = [[] for _ in range(N + 1)]
Q = deque()
for _ in range(M):
    A, B = map(int, input().split())
    in_degree[B] += 1
    tree[A].append(B)

for i in range(1, N + 1):
    if in_degree[i] == 0:
        Q.append(i)

while Q:
    q = Q.popleft()
    print(q, end=' ')
    for node in tree[q]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            Q.append(node)