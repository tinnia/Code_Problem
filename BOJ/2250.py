class Node:
    def __init__(self, number, left, right):
        self.parent = 1
        self.number = number
        self.left = left
        self.right = right


def order2(node, level):
    global depth, x
    depth = max(depth, level)
    if node.left != '-1':
        order2(tree[node.left], level + 1)
    Min[level] = min(Min[level], x)
    Max[level] = max(Max[level], x)
    x += 1
    if node.right != '-1':
        order2(tree[node.right], level + 1)

N = int(input())
tree = {}
Min = [N]
Max = [0]
root = -1
x = depth = 1

for i in range(1, N + 1):
    tree[i] = Node(i, -1, -1)
    Min.append(N)
    Max.append(0)

for _ in range(N):
    n, l, r = map(int, input().split())
    tree[n].left = l
    tree[n].right = r
    if l != -1:
        tree[l].parent = n
    if r != -1:
        tree[r].parent = n

for i in range(1, n + 1):
    if tree[i].parent == 1:
        root = i

order2(tree[root], 1)

result = 1
result