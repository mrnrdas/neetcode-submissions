#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_freq;
        unordered_map<char, int> t_freq;

        for (char c : s) {
            s_freq[c]++;
        }

        for (char c : t) {
            t_freq[c]++;
        }

        for (const auto& [key, value] : s_freq) {
            if (s_freq[key] != t_freq[key]) {
                return false;
            } 
        }

        return true;
    }
};
