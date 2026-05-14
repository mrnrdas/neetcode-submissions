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

public class Solution {
    public bool HasCycle(ListNode head) {
        // Initialzie slow and fast pointers to head
        ListNode slow = head;
        ListNode fast = head;

        // if while loop ends it means the list has reached the end without encountering a cycle
        while (fast != null && fast.next != null) {
            // Fast pointers moves two steps at a time
            fast = fast.next.next;
            // Slow pointer moves one step at a time
            slow = slow.next;
            // If slow is equal to fast then we have found a cycle
            if (slow.Equals(fast)) {
                // We can return true
                return true;
            }
        }
        // Otherwise return false there is no cycle
        return false;
    }
}
