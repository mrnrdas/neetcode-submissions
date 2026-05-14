from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for c in s:
            freq_s[c] += 1
        for c in t:
            freq_t[c] += 1

        for key, value in freq_s.items():
            if freq_s[key] != freq_t[key]:
                return False

        return True
        