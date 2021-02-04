def find(p):
    if p == parent[p]:
        return p
    else:
        x_root = find(parent[p])
        parent[p] = x_root
        return parent[p]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parent[y_root] = x_root
        number[x_root] += number[y_root]


for _ in range(int(input())):
    F = int(input())

    parent, number = {}, {}

    for _ in range(F):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
