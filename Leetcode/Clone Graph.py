"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if not node: return node

        tree = dict()
        # 노드 생성
        nodes = Node(node.val, [])
        tree[node] = nodes

        Q = deque()
        Q.append(node)
        while Q:
            tmp = Q.popleft()
            for neigh in tmp.neighbors:
                if neigh not in tree:
                    tree[neigh] = Node(neigh.val, [])
                    Q.append(neigh)
                tree[tmp].neighbors.append(tree[neigh])
        return nodes