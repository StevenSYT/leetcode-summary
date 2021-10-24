/*
 * @lc app=leetcode id=940 lang=cpp
 *
 * [940] Distinct Subsequences II
 */

// @lc code=start
class Solution {
    // number of distinct non-empty subsequences of s, including "".
    long dp[2001];
    // last[c - 'a']: Last occurance of char value is the index of it in s.
    int last[26];
public:
    int distinctSubseqII(string s) {
        int n = s.size();
        long M = 1e9 + 7;
        dp[0] = 1;
        
        // Offset "#" to allow easier dp[0] definition.
        // dp[0] means "no char in the string is selected", and the result is "" since
        // empty string counts in our definition.
        // Will need to remove the "" when we return the result.
        s = "#" + s;
        
        for (int i = 1; i <= n; i++) {
            dp[i] = (dp[i-1] * 2) % M;
            
            // Remove duplicate
            int j = last[s[i] - 'a'];
            if (j > 0) {
                dp[i] = (dp[i] - dp[j-1] + M) % M;
            }
            last[s[i]-'a'] = i;
        }
        return dp[n] - 1;
    }
};
// @lc code=end

