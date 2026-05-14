#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> freq;

        for (int num : nums) {
            freq[num]++;
        }

        for (auto const& [key, value] : freq) {
            if (value > 1) {
                return true;
            }
        }

        return false;
    }
};