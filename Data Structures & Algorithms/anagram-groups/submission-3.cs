public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        // Create a dictionary that takes in a string and a list of strings
        var ans = new Dictionary<string, List<string>>();

        // For each of the strings in strs
        foreach (var s in strs) {

            // Initialize a new array of size 26 to represent letters of the alphabet
            var count = new int[26];

            // For each character in the string
            foreach (var c in s) {
                // Find the index and add one to it
                count[c - 'a']++;
            }

            // Create a key from joining the count array
            var key = string.Join(',', count);

            // If the key has never been in the dictionary before
            if (!ans.ContainsKey(key)) {
                // Within the value of the key add a list of strings
                ans[key] = new List<string>();
            }

            // Add the string to the list of strings
            ans[key].Add(s);
        }

        // Return a list of the of all the lists of strings
        return new List<List<string>>(ans.Values);
    }
}
