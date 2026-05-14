public class Solution {
    public int Search(int[] nums, int target) {
        // Set up the low and high pointers
        int low = 0;
        int high = nums.Length - 1;

        // While the low and high pointers are not together
        while (low <= high) {

            // Calculate the mid value
            int mid = (low + high) / 2;

            // If the number at mid is equal to the targer
            if (nums[mid] == target) {
                // Return the mid index
                return mid;

            // Check if the lower half is sorted
            } else if (nums[low] <= nums[mid]) {
                /*
                    If the lower half is sorted and the value is greater than number at mid or less than number at low
                    It implies that the target is not in this sorted range
                    Therefore adjust low to mid + 1 to search other half
                    Otherwise adjust high to mid - 1 to continue search within the sorted range
                */
                if (target > nums[mid] || target < nums[low]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
                // If the upper half is sorted
            } else {
                /*
                    If the target is less than nums[mid] or great than nums[high]
                    It imples the target is not in the upper half so adjust high to mid - 1
                    Otherwise adjust low to mid + 1 to search within the sorted upper half
                */
                if (target < nums[mid] || target > nums[high]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        
        // If the loop exits without finding the target return -1
        return -1;
    }
}
