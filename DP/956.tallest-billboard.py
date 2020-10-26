#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#


# @lc code=start


        # Use a <diff, max_height> map to store left,right pairs combination info.
        # Diff means left and right pillar heights difference, value of it is the maximum height 
        # of the lower pillar with this pair height difference.
       
        # Assume we have an init state like this
        # ------- y ------|----- d -----|
        # ------- y ------|

        # case 1
        # If put x to tall side
        # ------- y ------|----- d -----|----- x -----|
        # ------- y ------|

        # We update dp[d + x] = max(dp[d + x], y )

        # case 2.1
        # Put x to low side and d >= x:
        # -------y------|----- d -----|
        # -------y------|--- x ---|

        # We update dp[d-x] = max(dp[d - x], y + x)

        # case 2.2
        # Put x to low side and d < x:
        # ------- y ------|----- d -----|
        # ------- y ------|------- x -------|
        # We update dp[x - d] = max(dp[x - d], y + d)

        # case 2.1 and case2.2 can merge into dp[abs(x - d)] = max(dp[abs(x - d)], y + min(d, x))
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for rod in rods:
            for key, val in list(dp.items()):
                dp[key + rod] = max(dp.get(key + rod, 0), val)
                dp[abs(key - rod)] = max(dp.get(abs(key - rod), 0), val + min(key, rod))
        return dp[0]
# @lc code=end

