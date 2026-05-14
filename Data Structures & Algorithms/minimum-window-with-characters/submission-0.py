from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)  # Characters and their frequencies in t
        window = Counter()
        l, r = 0, 0
        valid = 0
        start, min_len = 0, float('inf')
        
        while r < len(s):
            # Expand the right end of the window
            char = s[r]
            r += 1
            
            # Include the character in the window if it is needed
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1
            
            # Contract the window from the left if it already contains all needed characters
            while valid == len(need):
                # Update the minimum window if the current is smaller
                if r - l < min_len:
                    start = l
                    min_len = r - l
                
                # The character to be removed from the window
                d = s[l]
                l += 1
                
                # Update the window counters and valid count
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if min_len == float('inf') else s[start:start + min_len]