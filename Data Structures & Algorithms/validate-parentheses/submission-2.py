class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack
        stack = []
        # Initialize the dictionary with correct mappings
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            # Check if the character is a closing bracket
            if char in pairs:
                # If the stack is empty or the top element of the stack doesn't match the corresponding opening bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # Otherwise, assume it's an opening bracket and push onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0

        