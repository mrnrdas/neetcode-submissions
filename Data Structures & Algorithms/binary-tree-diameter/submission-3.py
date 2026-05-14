# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def get_longest(node):
            if not node:
                return 0

            left_path = get_longest(node.left)
            right_path = get_longest(node.right)

            self.diameter = max(self.diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        get_longest(root)

        return self.diameter