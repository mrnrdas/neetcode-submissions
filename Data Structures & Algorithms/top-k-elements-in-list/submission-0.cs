public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {

        // Initialize a dictionary called count to count
        Dictionary<int, int> count = new Dictionary<int, int>();

        // Initialize a list called freq where each index represents a freqeuncy
        List<int>[] freq = new List<int>[nums.Length + 1];

        // For each index in the list put a list at the index
        for (int i = 0; i < freq.Length; i++) {
            freq[i] = new List<int>();
        }

        // For each int n in nums
        foreach (int n in nums) {

            // If n is a Key in count
            if (count.ContainsKey(n)) {
                // Increment the vaue at the key by one
                count[n]++;
            } else {

                // Otherwise initialize it to 1
                count[n] = 1;
            }
        }

        // For each value in the count dictionary
        foreach (var entry in count){

            /*
                At the freq list
                entry.Value is the amount of times an entry was seen
                So at that entry.Value index of the freq list we add
                entry.Key which is the actual number
            */
            freq[entry.Value].Add(entry.Key);
        }

        // Initialize a list with length of k
        int[] res = new int[k];

        // Initialize an index to zero
        int index = 0;

        /*
            For i starting at the end of the array
            while i does not reach the end of the array
            and the index of zero is less than k
            we decrement i to go backwards from end to start
            once the index reaches k the loop will terminate
        */
        for (int i = freq.Length - 1; i > 0 && index < k; i--) {

            /* For each int n in freq list 
            (Since at each index there is a list of numbers that appeard at the same frequency)
            */
            foreach (int n in freq[i]) {

                // At the current index of res add the current number and post increment index
                res[index++] = n;

                // After the post increment if we reach the same level of k than we can return the res array
                if (index == k) {
                    return res;
                }
            }
        }

        // In the case that the array is smaller than k this will still return the current res array
        return res;
    }
}

