# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Assign previous as null and curr as head
        prev, curr = None, head
        
        # While the curr variable is not null
        while curr:
            # Assign temp to be next
            temp = curr.next
            # Assign the next to be prev
            curr.next = prev
            # Assign prev to be current
            prev = curr
            # Assign the new current to be temp
            curr = temp
        # Return previous
        return prev