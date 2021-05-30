# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.defaultdict(int)
        answer = []

        def find(node):
            if not node:
                return

            key = (node.val, find(node.left), find(node.right))
            count[key] += 1

            if count[key] == 2:
                answer.append(node)

            return key

        find(root)
        return answer