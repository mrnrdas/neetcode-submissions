/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        // If the root is null
        if (root == null) {
            // Return null
            return null;
        }

        // Create a new node with the same value as the current root
        TreeNode node = new TreeNode(root.val);

        // Assign the right pointer to the node which was originally the left of the root
        node.right = InvertTree(root.left);

        // Assign the left pointer to the node which was originally the right of the root
        node.left = InvertTree(root.right);

        return node;
    }
}
