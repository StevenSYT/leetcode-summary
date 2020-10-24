#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#


# @lc code=start
class Solution:
    # The goal is to get the smallest possible final weight.
    # To think about the sequence, it is eventually gonna be a
    # sequence of a-b - c + d - e... => |stonesA - stonesB|
    # And we want to have two groups of stones with closest
    # sum, let's assume stonesA <= stonesB, then stonesA <= sum(stones) // 2
    # if we find out a stone set A within stones that has a closest sum to
    # sum(stones) // 2, it should be the best case.
    # Then the problem becomes, find a sub-stones set with highest sum smaller than
    # but most close to sum(stones) // 2
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
