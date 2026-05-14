public class Solution {
    public int LongestConsecutive(int[] nums) {

        // Initialize a set with all the numbers from array to get rid of repeating numbers
        HashSet<int> numSet = new HashSet<int>(nums);

        // Initialize a variable to measure the longest length
        int longest = 0;

        // Loop through each number in the set
        foreach (int n in numSet) {

            // If the set does not contain n - 1 then it is the smallest number of a subsequence
            if (!numSet.Contains(n - 1)) {

                // Initialize the length of the subsequence to one
                int length = 1;

                // If there is another number with one more than the current number and if not the while loop ends
                while (numSet.Contains(n + length)) {

                    // Increase the length
                    length++;
                }

                // Assign the max of length and longest
                longest = Math.Max(length, longest);
            }
        }

        // Return the longest
        return longest;
    }
}
