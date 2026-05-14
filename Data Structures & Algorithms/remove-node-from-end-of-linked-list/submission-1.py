# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Getting length of linked list
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        # Determine the index of the node to remove from the start
        removeIndex = N - n
        if removeIndex == 0:
            # If the node to remove is the head, return the next node
            return head.next

        # Traverse the list to find the node just before the one to remove
        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                # Remove the nth node from the end by skipping it
                cur.next = cur.next.next
                break
            cur = cur.next
        
        # Return the modified list
        return head