from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = defaultdict(int)
        hash_map_t = defaultdict(int)

        for char in s:
            hash_map_s[char] += 1
        
        for char in t:
            hash_map_t[char] += 1

        if hash_map_s == hash_map_t:
            return True

        return False



