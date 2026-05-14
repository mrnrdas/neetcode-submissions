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
    public int MaxDepth(TreeNode root) {
        // If the root is null
        if (root == null) {
            // Return zero
            return 0;
        }

        // Do a recursive solution to figure out the Max depth
        return 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
    }
}
