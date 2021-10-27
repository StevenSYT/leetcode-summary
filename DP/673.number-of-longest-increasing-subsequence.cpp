/*
 * @lc app=leetcode id=673 lang=cpp
 *
 * [673] Number of Longest Increasing Subsequence
 */

// @lc code=start
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        // 这题需要同时两个DP更新
        // 关键定义在于len[i]和times[i]都对应的是以nums[i]为结尾的
        // 递增子序列
        int n = nums.size();
        auto len = std::vector<int>(n, 1);
        auto times = std::vector<int>(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] >= nums[i]) continue;
                if (len[j] + 1 > len[i]) {
                    len[i] = len[j] + 1;
                    times[i] = times[j];
                } else if (len[j] + 1 == len[i]) {
                    times[i] += times[j];
                }
            }
        }

        int maxLen = 1;
        int result = 0;

        for (int i = 0; i < n; i++) {
            if (len[i] == maxLen) {
                result += times[i];
            } else if (len[i] > maxLen) {
                maxLen = len[i];
                result = times[i];
            }
        }
        return result;
    }
};
// @lc code=end

