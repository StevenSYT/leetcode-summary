/*
 * @lc app=leetcode id=1987 lang=cpp
 *
 * [1987] Number of Unique Good Subsequences
 */

// @lc code=start
class Solution {
    long dp[100001];
    
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        int n = binary.size();
        int m = 0;
        int last0 = 0, last1 = 0;
        int mod = 1e9 + 7;
        binary = "#" + binary;
        
        for (int i = 0; i <= n; i++) {
            if (binary[i] == '1') {
                m = i;
                dp[i] = 1;
                break;
            }
        }
        
        for (int i = m + 1; i <= n; i++) {
            int j;
            if (binary[i] == '0') {
                j = last0;
                last0 = i;
            } else {
                j = last1;
                last1 = i;
            }
            dp[i] = (dp[i-1] * 2 % mod - (j > 0 ? dp[j - 1] : 0) + mod) % mod;
        }
        return dp[n] + (binary.find('0') != -1);
    }
};
// @lc code=end

