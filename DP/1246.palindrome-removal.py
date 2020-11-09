class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # The trick here is, if we find a k in [left+1, right] where arr[left] == arr[k],
        # we can directly call for sub-problem dp[left+1][k-1] + dp[k+1][right], since however
        # we are gonna solve dp[left][k-1], at last the remaining substring in [left+1, k-1] will
        # be a palindrom combining arr[left] and arr[k].
        # 
        # Corner cases:
        # 1. left and left + 1 numbers are the same, can be directly reduced to subproblem dp[left+2][right] + 1
        # 2. if arr[left] == arr[right], directly reduce to dp[left+1][right-1], but dp[k+1][right] might cause index out of bounds issue,
        # so we need to initialize dp to be (n+1) x (n+1) instead of n x n.
        # 
        # Seems that it is probably gonna be more clear to use a memo recursion to solve this.
        #
        for d in range(0, n):
            for left in range(0, n - d):
                right = left + d
                if d == 0:
                    dp[left][right] = 1
                    continue
                dp[left][right] = dp[left+1][right] + 1
                if arr[left] == arr[left+1]:
                    dp[left][right] = min(dp[left][right], dp[left+2][right] + 1) 
                for k in range(left+2, right+1):
                    if arr[k] == arr[left]:
                        dp[left][right] = min(dp[left][right], dp[left+1][k-1] + dp[k+1][right])
        return dp[0][n-1]
                    
                    