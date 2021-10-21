/*
 * @lc app=leetcode id=446 lang=cpp
 *
 * [446] Arithmetic Slices II - Subsequence
 */

// @lc code=start
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int N = nums.size();
        auto dp = std::vector<std::unordered_map<long, int>>(N);
        unordered_set<int> num_set(begin(nums), end(nums));
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                long diff = static_cast<long>(nums[i]) - nums[j];
                int count = dp[j].count(diff) ? dp[j][diff] : 0;
                if (num_set.count(nums[i] + diff))
                    dp[i][diff] += count + 1;
                result += count;
            }
        }
        return result;
    }
};
// @lc code=end

