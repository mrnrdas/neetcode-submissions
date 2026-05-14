class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Assign pointers left and right
        l, r = 0, len(s) - 1

        # While they do not meet
        while l < r:
            # While left pointer is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                # Increment the left pointer
                l += 1
            # While right pointers is not alphanumberic
            while r > l and not self.alphaNum(s[r]):
                # Decrement the right pointer
                r -= 1
            # If they both do not equal eachoter
            if s[l].lower() != s[r].lower():
                # You may return false
                return False
            # Otherwise increment and decrement the two pointers
            l, r = l + 1, r - 1
        # Return true if finished
        return True
    
    # Method to check the unicode characters
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

        