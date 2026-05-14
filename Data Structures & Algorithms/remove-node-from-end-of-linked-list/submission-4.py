# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialzing Variables
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Moving right pointer n steps forward
        while n > 0:
            right = right.next
            n -= 1

        # Get left pointer to point at nth node from end of the list
        while right:
            right = right.next
            left = left.next

        # Remove the nth node from end
        left.next = left.next.next

        # Return the head of the list
        return dummy.next
        
