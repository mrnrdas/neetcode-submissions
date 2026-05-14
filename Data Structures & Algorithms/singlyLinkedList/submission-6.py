class ListNode:
    # Initialize the constructor to have val and next_node if no value is provided for next_node then set it to null
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    # Constructor will create a dummy node for the head and have the tail to be equal to the head
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        # Get the current which is right after the dummy node
        curr = self.head.next
        # Set i to zero
        i = 0
        
        # While current is not null
        while curr:
            # If we find the correct index
            if i == index:
                # Return the value at the index
                return curr.val
            # Otherwise increment the i
            i += 1
            # Change curr to the next node
            curr = curr.next
        # Return -1 if the node is never found
        return -1
        

    def insertHead(self, val: int) -> None:
        # Create the new node
        new_node = ListNode(val)
        # Assign the next of the new node to the next of the dummy head
        new_node.next = self.head.next
        # Change the next of the dummy head to the new node
        self.head.next = new_node
        # If there is no next for the new node aka null then also set the tail to be the new node
        if not new_node.next:
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        # Set the next of the current tail to the new node
        self.tail.next = ListNode(val)
        # Set the tail to the new node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # Initalize zero
        i = 0
        # Get current as the dumm node
        curr = self.head
        # While we have not made it to 1 less of the index and curr still exists
        while i < index and curr:
            # Increment i
            i += 1
            # Move curr to the next node
            curr = curr.next

        # If the curr is not null and the next of curr is not null
        if curr and curr.next:
            # First check if curr.next is equal to the tail
            if curr.next == self.tail:
                # Then I will need to set the new tail to curr
                self.tail = curr
            # Then I will remove the next node by getting curr to just point at the node next from the next
            curr.next = curr.next.next
            # Return true since the node is removed
            return True
        # Return false since the index was out of bounds
        return False
        

    def getValues(self) -> List[int]:
        # Get the current node after the dummy node
        curr = self.head.next
        # Get an empty result array
        res = []
        # While curr is not null
        while curr:
            # Append the curr value to the result array
            res.append(curr.val)
            # Increment next node
            curr = curr.next
        # Return the result array
        return res
        
