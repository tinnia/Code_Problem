# class Node:
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# def order1(node):
#     print(node.data, end='')
#     if node.left != '.':
#         order1(tree[node.left])
#     if node.right != '.':
#         order1(tree[node.right])
#
#
# def order2(node):
#     if node.left != '.':
#         order2(tree[node.left])
#     print(node.data, end='')
#     if node.right != '.':
#         order2(tree[node.right])
#
#
# def order3(node):
#     if node.left != '.':
#         order3(tree[node.left])
#     if node.right != '.':
#         order3(tree[node.right])
#     print(node.data, end='')
#
#
#
#
# N = int(input())
# tree = {}
# for i in range(N):
#     data, left, right = input().split()
#     tree[data] = Node(data, left, right)
#
# order1(tree['A'])
# print()
# order2(tree['A'])
# print()
# order3(tree['A'])


# 나 👉 왼쪽 👉 오른쪽
def preOrder(x):
    if x < 0:
        return
    print(chr(x + ord('A')), end='')
    preOrder(tree[x][0])
    preOrder(tree[x][1])


# 왼쪽 👉 나 👉 오른쪽
def inOrder(x):
    if x < 0:
        return
    inOrder(tree[x][0])
    print(chr(x + ord('A')), end='')
    inOrder(tree[x][1])


# 왼쪽 👉 오른쪽 👉 나
def postOrder(x):
    if x < 0:
        return
    postOrder(tree[x][0])
    postOrder(tree[x][1])
    print(chr(x + ord('A')), end='')


N = int(input())
tree = [[-1] * 2 for _ in range(N)]
for i in range(N):
    parent, left, right = map(str, input().split())
    if left != '.':
        tree[ord(parent) - ord('A')][0] = ord(left) - ord('A')
    if right != '.':
        tree[ord(parent) - ord('A')][1] = ord(right) - ord('A')

preOrder(0)
print()
inOrder(0)
print()
postOrder(0)























