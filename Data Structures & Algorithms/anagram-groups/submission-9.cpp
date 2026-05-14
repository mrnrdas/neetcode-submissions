#include <vector>
#include <unordered_map>
#include <string>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> freq;

        for (string word : strs) {
            vector<int> count(26, 0);
            for (char c : word) {
                count[c - 'a']++;
            }

            string key;
            for (int i = 0; i < 26; i++) {
                key += "#" + to_string(count[i]);
            }

            freq[key].push_back(word);
        }

        vector<vector<string>> result;
        for (auto& pair : freq) {
            result.push_back(pair.second);
        }
        return result;
    }
};
