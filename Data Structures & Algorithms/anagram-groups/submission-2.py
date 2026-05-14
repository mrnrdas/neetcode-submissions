class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Use default dict in order to have a dictionary that will also set a key if it does not exist
        ans = defaultdict(list)

        # Loop through the strings in the strs list
        for s in strs:

            # Initialize an array of zeros to represent letters of the alphabet
            count = [0] * 26

            # Loop through every character in each string
            for c in s:

                # At the index using the ord function add 1 if the letter exists in this spot
                count[ord(c) - ord("a")] += 1

            # Using a tuple create a key and append the string to the key
            ans[tuple(count)].append(s)

        # Return the dictionary with only the values grouped together
        return ans.values()
