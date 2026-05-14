/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

 /*

 */
 
public class Solution {
    public ListNode ReverseList(ListNode head) {
        // Initialize prev variable to null and curr to point at head
        ListNode prev = null, curr = head;

        // While the current node is not null
        while (curr != null) {
            // Create a temporary variable to hold the node that is next from curr
            var temp = curr.next;

            // Assign the next curr value to be whatever was previous
            curr.next = prev;

            // Move prev to the current value
            prev = curr;

            // Assign current to the temporary value
            curr = temp;
        }

        // Once outside of the while loop prev will be the reversed list
        return prev;
    }
}
