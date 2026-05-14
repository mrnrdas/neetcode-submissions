public class Solution {

    public string Encode(List<string> strs) {

        // Initialize the result string
        string res = "";

        // For each string in the strs list
        foreach (string s in strs) {
            
            // Add to the result string the length then a # then the string
            res += s.Length.ToString() + "#" + s;
        }

        // Return the resulting encoded string
        return res;
    }

    public List<string> Decode(string s) {

        // Initalize a result list
        List<string> res = new List<string>();

        // Initalize i at 0
        int i = 0;

        // While i is not at the end of the string
        while (i < s.Length) {
            
            // Get j to equal i
            int j = i;

            // While the index of s[j] does not equal the #
            while (s[j] != '#') {
                
                // Increment j in order to obtain the length
                j++;
            }

            /*
                Get the length by using the Substring of where the length is kept
                Make sure to Parse the integer from the string
                Use Substring to slice the length out
                j - i will get the exact length i am looking for to get the length
            */
            int length = int.Parse(s.Substring(i, j - i));

            // Increment j to go past the #
            j++;

            // Get the extracted substring using the length I extracted and the j index
            string extractedString = s.Substring(j, length);

            // Add this new extracted string into my result List
            res.Add(extractedString);

            // Move i to the length of the start of the next encoded string
            i = j + length;
        }

        // Finally return the result array
        return res;
    }
}
