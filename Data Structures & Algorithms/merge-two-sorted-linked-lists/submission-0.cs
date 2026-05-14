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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {

        /*
            Initialize a dummy listnode
            Save the dummy node in a dummy variable
            Create another ListNode called node that will be used to traverse
        */
        ListNode dummy = new ListNode(0);
        ListNode node = dummy;
        
        // While there are still nodes in either list
        while (list1 != null && list2 != null) {
            // If the value in list1 is less than the value in list2
            if (list1.val < list2.val) {
                // Next node will be the current node at list 1
                node.next = list1;
                // Move the node at list one to the next node
                list1 = list1.next;
            // Otherwise if the value in list2 is less than the value in list 1
            } else {
                // The next node is the node at list2
                node.next = list2;
                // Move the node at list2 next
                list2 = list2.next;
            }

            // Move the node to the next node we are going to fill
            node = node.next;
        }

        // If there is either list remaining since it is sorted you can just add the remaining list
        if (list1 != null) {
            node.next = list1;
        } else {
            node.next = list2;
        }

        // After the dummy node the next node will be the merged list
        return dummy.next;
    }
}