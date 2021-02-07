class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def order1(node):
    print(node.data, end='')
    if node.left != '.':
        order1(tree[node.left])
    if node.right != '.':
        order1(tree[node.right])


def order2(node):
    if node.left != '.':
        order2(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        order2(tree[node.right])


def order3(node):
    if node.left != '.':
        order3(tree[node.left])
    if node.right != '.':
        order3(tree[node.right])
    print(node.data, end='')




N = int(input())
tree = {}
for i in range(N):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

order1(tree['A'])
print()
order2(tree['A'])
print()
order3(tree['A'])