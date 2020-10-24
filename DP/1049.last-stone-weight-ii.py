#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightIISolution1(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        target = sum_stones // 2

        dp = [True] + [False for _ in range(target)]

        upper_limit = 0
        for stone in stones: 
            upper_limit += stone
            for s in range(upper_limit, -1, -1):
                if (s + stone > target): continue

                if (dp[s]):
                    dp[s + stone] = True
        for s in range(target, -1, -1):
            if dp[s]:
                return sum_stones - 2 * s
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        target = sum_stones // 2
        dp = set([0])
        for stone in stones:
            next_set = set()
            for s in dp:
                if s + stone <= target:
                    next_set.add(s + stone)
            dp |= next_set
        return min([sum_stones - 2 * s for s in dp])

# @lc code=end

