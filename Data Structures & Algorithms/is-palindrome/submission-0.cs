public class Solution {
    public bool IsPalindrome(string s) {

        // Initialize two pointers at the end and start of the array
        int left = 0;
        int right = s.Length - 1;

        // While left and right pointers are not equal
        while (left < right) {

            // If the character is not a letter or a digit
            if (!char.IsLetterOrDigit(s[left])) {
                // Move the pointer forwards
                left++;
            
            // If the character is not a letter of a digit
            } else if (!char.IsLetterOrDigit(s[right])) {
                // Move the pointer back
                right--;

            // Otherwise if they are both characters
            } else {
                // Check if the lowercase version is equal or not
                if (char.ToLower(s[left]) != char.ToLower(s[right])) {
                    // If they are not equal we can return false
                    return false;
                }

                // If they are equal we can increment/decrement the pointers
                left++;
                right--;
            }
        }

        // If the while loop executes we can return true
        return true;
    }
}
