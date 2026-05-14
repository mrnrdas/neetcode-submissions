public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Set up a dictionary to hold both indices
        Dictionary<int, int> indices = new Dictionary<int, int>();

        // For each int i in nums
        for (int i = 0; i < nums.Length; i++) {
            // Calculate the difference needed of target - the number
            var diff = target - nums[i];

            // If indices contains the key of the diff we calculated
            if (indices.ContainsKey(diff)) {

                // We can return an int array which has the index of the diff, and the current index of the loop
                return new int[] {indices[diff], i};
            }

            // Add the number in the array as a key and the index as the value
            indices[nums[i]] = i;
        }

        // The function should return null if nothing happens
        return null;
    }
}
