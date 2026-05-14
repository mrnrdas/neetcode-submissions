class Solution:
    
    def encode(self, strs: List[str]) -> str:

        # Result is at first an empty string
        res = ""

        # For each string in strs array
        for s in strs:
            # Add the str to the array with the length of the string and # seperating the contents of the string
            res += str(len(s)) + "#" + s
        
        # Return result
        return res

    def decode(self, s: str) -> List[str]:

        # Prepare a result array
        res = []

        # Set i to zero
        i = 0
        
        # While i is less than the length of the string
        while i < len(s):

            # Create another index j equal to i
            j = i

            # While the current string is not at a #
            while s[j] != '#':

                # Increment j to find the index of the #
                j += 1
            # Once we find the # we can slice out the length of the string
            length = int(s[i:j])

            # Then we can get the index of the first letter of our string
            i = j + 1

            # Using the length we can find the last letter of our string
            j = i + length

            # Then with our new pointers we can add the string
            res.append(s[i:j])

            # Move the i index to the start of a new string
            i = j
        
        # Return a result
        return res

