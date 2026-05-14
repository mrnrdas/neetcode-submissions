from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for character in word:
                freq[ord(character) - ord('a')] += 1
            hash_map[tuple(freq)].append(word)

        return list(hash_map.values())
        