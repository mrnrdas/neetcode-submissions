# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(s, t):
            if not s and not t:
                return True

            if not s or not t or s.val != t.val:
                return False

            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        def dfs(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)