public class Solution {
    public bool hasDuplicate(int[] nums) {
        // Initialize a set to check all unique numbers from the array
        HashSet<int> set = new HashSet<int>();

        // For each num in nums
        foreach (int num in nums) {

            // If the set contains num
            if (set.Contains(num)) {

                // We are done we can return true
                return true;
            }

            // Add the num to the set
            set.Add(num);
        }

        // Return false if no duplicates were found
        return false;

        
    }
}
