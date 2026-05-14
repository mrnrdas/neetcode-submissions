public class Solution {
    public bool IsValid(string s) {
        // Initialize a stack for chars
        var stack = new Stack<char>();

        // Initialize a dictionary with these key value pairs
        var pairs = new Dictionary<char, char>() {
            [')'] = '(',
            [']'] = '[',
            ['}'] = '{'
        };

        // For each char in the string
        foreach (char c in s) {
            // If c is not an opening bracket
            if (!pairs.ContainsKey(c)) {
                // Pushed onto stack
                stack.Push(c);
                /*
                    If c is a closing bracket
                    Checks if the stack is empty which would mean there's no corresponding opening bracket thus false
                    If the stack is not empty it pops the top of the stack
                    The popped character should be matching opening bracket for c
                */
            } else if (stack.Count == 0 || stack.Pop() != pairs[c]) {
                // If both conditions fail then false
                return false;
            }
        }
        // If by the end the stack is empty then we can return true
        return stack.Count == 0;
    }
}
