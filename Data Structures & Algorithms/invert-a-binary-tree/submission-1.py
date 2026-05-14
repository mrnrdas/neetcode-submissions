# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is null
        if not root:
            # Return nothing
            return None
        
        # Create a new Tree Node with the same value as root
        node = TreeNode(root.val)

        # Assign the right of the node using the invertTree method and the left of the root
        node.right = self.invertTree(root.left)

        # Assign the left of the node using the invertTree method and the right of the root
        node.left = self.invertTree(root.right)

        return node        