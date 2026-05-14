public class Solution {
    public int[] ProductExceptSelf(int[] nums) {

        // Initialize prefix to one which will accumulate product to the left of element
        int prefix = 1;

        // Intialize the postfix to one which will accumulate product to the right of the element
        int postfix = 1;

        // Intialize result array to be the same length of nums
        int[] res = new int[nums.Length];  
        
        /*
            Loop from left to right of the array
            The logic in the loop will make sure the prefix includes the product of all the elements to the left up to to current index
        */
        for(int i = 0; i < nums.Length; i++){

            // At the current index in the result array it will equal the prefix
            res[i] = prefix;
            
            // Then multiply the current prefix by the number at the current position in the array
            prefix *= nums[i];
        }
        
        /*
            Make a second pass through the array going backwards
            The logic in the loop will make sure the postfix includes the product of all elements to the right up to the current index
        */
        for(int i = nums.Length - 1; i >= 0; i--){

            // At the current index in the result it will equal postfix
            res[i] *= postfix;

            // Multiply the postfix by the number at the current position in the array
            postfix *= nums[i];
        }

        // Return the result array
        return res;
    }
}

