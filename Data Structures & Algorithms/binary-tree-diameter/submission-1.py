# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #DFS Approach

        # Initialize diamter variable
        self.diameter = 0

        # DFS helper method
        def longest_path(node):
            # Base case if no node
            if not node:
                return 0

            # Recursively find the longest path in left and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            
            # Update the diameter if left_path plus right_path is larger
            self.diameter = max(self.diameter, left_path + right_path)

            # Return the longest one between left and right path
            # Remember to add 1 for the path connecting the node and it's parent
            return max(left_path, right_path) + 1

        # Call helper method on root
        longest_path(root)

        # Return the final diameter
        return self.diameter