class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_str = ""
        res_len = 0

            

        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_str = s[l:r + 1]
                    res_len = (r - l + 1)
                l -= 1
                r += 1
            # Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_str = s[l:r + 1]
                    res_len = (r - l + 1)
                l -= 1
                r += 1

        return res_str