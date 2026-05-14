class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        longest_sub = 0

        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            longest_sub = max(longest_sub, r - l + 1)
        return longest_sub
    


            
            