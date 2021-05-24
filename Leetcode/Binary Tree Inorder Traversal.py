# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [], []
        node = root
        while node or stack:
            # 왼쪽 노드가 존재할 때까지
            while node:
                stack.append(node)
                node = node.left
            # stack에 쌓인 마지막 왼쪽 노드를 빼고, val을 ans에 append한 후 node를 오른쪽 노드로 바꿔줌
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans