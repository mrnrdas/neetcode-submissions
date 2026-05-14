# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node and initialize two pointers
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move the right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until the right pointer reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        left.next = left.next.next

        # Return the head of the modified list
        return dummy.next