from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))

            hash_map[sorted_word].append(word)

        return [value for value in hash_map.values()]