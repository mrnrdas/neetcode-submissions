public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> set = new HashSet<int>();

        foreach (int x in nums) {
            if (set.Contains(x)) return true;
            set.Add(x);
        }
        return false;
    }
}
