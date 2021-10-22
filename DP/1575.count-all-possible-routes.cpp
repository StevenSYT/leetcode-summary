/*
 * @lc app=leetcode id=1575 lang=cpp
 *
 * [1575] Count All Possible Routes
 */

// @lc code=start
class Solution {
    // dp[f][c] number of routes starting from start and end at c with fuel level f.
    long dp[201][101];
    long M = 1e9 + 7;
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        
        int n = locations.size();
        int res = 0;
        
        // initial state
        dp[fuel][start] = 1;
        
        for (int f = fuel; f >= 0; f--) {
            for (int c = 0; c < n; c++) {
                for (int d = 0; d < n; d++) {
                    if (d == c) continue;
                    int delta = std::abs(locations[d] - locations[c]);
                    if (f + delta > fuel) continue;
                    dp[f][c] = (dp[f][c] + dp[f+delta][d]) % M;
                }
            }
        }
        for (int f = 0; f <= fuel; f++) {
            res = (res + dp[f][finish]) % M;
        }
        return res;
    }
};
// @lc code=end

