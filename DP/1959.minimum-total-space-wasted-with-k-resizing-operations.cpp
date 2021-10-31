/*
 * @lc app=leetcode id=1959 lang=cpp
 *
 * [1959] Minimum Total Space Wasted With K Resizing Operations
 */

// @lc code=start
class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        int n = nums.size();
        int dp[n][k+1];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = INT_MAX/2;
            }
        }
        
        // dp[i][0] means, if there is no chance to resize the array,
        // we need to set the size of the array to be the maximum value 
        // of nums[0:i] and compute the wasted space as the value of 
        // dp[i][0]
        int maxNum = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            maxNum = max(maxNum, nums[i]);
            sum += nums[i];
            dp[i][0] = maxNum * (i + 1) - sum;
        }
        
        
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= min(i, k); j++) {
                int upperBound = 0;
                int cumSum = 0;
                for (int s = i; s >= 1; s--) {
                    // X X X X A B C
                    //        [s xx i]
                    upperBound = std::max(upperBound, nums[s]);
                    cumSum += nums[s];
                    dp[i][j] = std::min(dp[i][j], dp[s-1][j-1] + upperBound * (i - s + 1) - cumSum);
                }
            }
        }
        
        return dp[n-1][k];
    }
};
// @lc code=end

