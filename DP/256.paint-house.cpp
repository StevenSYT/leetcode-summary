class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int n = costs.size();
        auto dp = vector<vector<int>>(n, vector<int>(3, 0));
        for (int j = 0; j < 3; j++) {
            dp[0][j] = costs[0][j];
        }
        for (int i = 1; i < n; i++) {
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
        }
        
        int res = INT_MAX / 2;
        for (int j = 0; j < 3; j++) {
            res = min(res, dp[n-1][j]);
        }
        return res;
    }
};