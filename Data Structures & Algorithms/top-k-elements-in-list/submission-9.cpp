class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int n : nums) {
            ++count[n];
        }
        
        vector<vector<int>> freq(nums.size() + 1);
        for (auto& [num, cnt]: count) {
            freq[cnt].push_back(num);
        }

        vector<int> result;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int num : freq[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result;
                }
            }
        }
        return result; // should not reach here because of constraints, but added for completness
    }
};
