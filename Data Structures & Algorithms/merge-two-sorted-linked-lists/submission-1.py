# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create the dummy node
        dummy = ListNode(0)
        # Create a node value from the dummy to traverse
        node = dummy

        # While both lists are not null
        while (list1 and list2):

            # If the value in list1 is less than the value in list2
            if list1.val < list2.val:
                # The next node is list1 and move list1 to the next
                node.next = list1
                list1 = list1.next
            # If the value in list2 is less than the value in list1
            else:
                # The next node is list2 and move list2 to the next
                node.next = list2
                list2 = list2.next
            node = node.next
        
        # If either list is left over than add the remaining list
        if list1 == None:
            node.next = list2
        else:
            node.next = list1

        # Return the next node from the dummy
        return dummy.next