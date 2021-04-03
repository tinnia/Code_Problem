def delete_node(idx, trees):
    trees[idx] = -2
    for node in range(len(trees)):
        if idx == trees[node]:
            delete_node(node, trees)


N = int(input())
tree = list(map(int, input().split()))
delete_idx = int(input())

delete_node(delete_idx, tree)

answer = 0
for node in range(len(tree)):
    if tree[node] != -2 and node not in tree:
        answer += 1

print(answer)