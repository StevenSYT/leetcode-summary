/*
 * @lc app=leetcode id=1639 lang=cpp
 *
 * [1639] Number of Ways to Form a Target String Given a Dictionary
 */

// @lc code=start
class Solution {
    // dp[i][k] number of ways to form target[0:i] using word[0:k]
    long dp[1001][1001]; 
    // count[p][c-'a'] For word[p], the count for char c
    long count[1001][27]; 
    long M = 1e9 + 7;
    
public:
    int numWays(vector<string>& words, string target) {
        int n = target.size();
        int m = words[0].size();
        
        // offset target with "#" so that we can construct initial conditions.
        target  = "#" + target;
        
        // Building count, valid entries are from 1:m.
        for (const auto& word : words) {
            for (int p = 0; p < m; p++) {
                count[p + 1][word[p] - 'a'] += 1;
            }
        }
        
        // Initial condition.
        for (int k = 0; k <= m; k++)
            dp[0][k] = 1;            
        
        for (int i = 1; i <= n; i++) {
            for (int k = 1; k <= m; k++) {
                dp[i][k] = dp[i][k - 1];
                if (count[k][target[i] - 'a'] > 0)
                    dp[i][k] += count[k][target[i] - 'a'] * dp[i - 1][k -1 ] % M;
                    dp[i][k] %= M;
            }
        }
        return dp[n][m];       
    }
};
// @lc code=end

