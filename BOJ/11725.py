# N = int(input())
# tree = [[] for _ in range(N + 1)]
# root = [0] * (N + 1)
# visit = [0] * (N + 1)
#
# for i in range(N - 1):
#     u, v = map(int, input().split())
#     tree[u].append(v)
#     tree[v].append(u)
#
#
# def dfs():
#     stack = [1]
#     while stack:
#         tmp = stack.pop()
#         visit[tmp] = 1
#         for node in tree[tmp]:
#             if not visit[node]:
#                 root[node] = tmp
#                 stack.append(node)
#
#
# dfs()
# for i in range(2, N + 1):
#     print(root[i])


import sys
sys.setrecursionlimit(100000000)

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(N + 1)]


def dfs(s, tree, parents):
    for i in tree[s]:
        if parents[i] == 0:
            parents[i] = s
            dfs(i, tree, parents)


dfs(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])
