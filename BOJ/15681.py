import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def countNode(x):
    cnt[x] = 1
    for i in tree[x]:
        if not cnt[i]:
            countNode(i)
            cnt[x] += cnt[i]


N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)

for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

countNode(R)

for _ in range(Q):
    print(cnt[int(input())])