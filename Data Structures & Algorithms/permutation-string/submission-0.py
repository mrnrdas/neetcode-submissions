from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, word_length = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1

            if i >= word_length and s2[i - word_length] in counter:
                counter[s2[i - word_length]] += 1

            if all([counter[i] == 0 for i in counter]):
                return True

        return False