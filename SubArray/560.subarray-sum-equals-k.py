#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Use a dictionary storing the frequency of a target sum.
        # We can use one-pass to finish the checking: use a cumulative sum Si
        # recording the sum of the first i nums. Whenever getting a new sum Sn, 
        # check the dictionary to see if there is a sum Sm where Sn - Sm == k.
        # If there is one, that means subarray [m, n] is a match.
        sum_dict = collections.defaultdict(int)
        sum_dict[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_dict:
                count += sum_dict[cur_sum - k]
            sum_dict[cur_sum] += 1
        return count

# @lc code=end

