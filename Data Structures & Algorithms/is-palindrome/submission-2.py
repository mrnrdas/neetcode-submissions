class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(char):
            char = char.lower()
            return ('a' <= char <= 'z') or ('0' <= char <= '9')

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlphaNumeric(s[l]):
                l += 1
                continue

            while l < r and not isAlphaNumeric(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
