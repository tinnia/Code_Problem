# class Node:
#     def __init__(self, parent, left, right):
#         self.parent = parent
#         self.left = left
#         self.right = right
#
#
# N = int(input())
# tree = [Node(-1, -1, -1) for _ in range(N + 1)]
# Min = [N] * (N + 1)
# Max = [0] * (N + 1)
# root = 0
# x = 1
#
#
# def order2(node, level):
#     global tree, x
#     if tree[node].left != -1:
#         order2(tree[node].left, level + 1)
#     Min[level] = min(Min[level], x)
#     Max[level] = max(Max[level], x)
#     print(Min, Max)
#     x += 1
#     if tree[node].right != -1:
#         order2(tree[node].right, level + 1)
#
#
# for _ in range(N):
#     n, l, r = map(int, input().split())
#     tree[n].left = l
#     tree[n].right = r
#     if l != -1:
#         tree[l].parent = n
#     if r != -1:
#         tree[r].parent = n
# print(tree)
#
#
# for i in range(1, N + 1):
#     if tree[i].parent == -1:
#         root = i
#         break
#
# order2(root, 1)
#
# val = level = 0
# for i in range(N + 1):
#     gap =