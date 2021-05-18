#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#


# @lc code=start
class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def low_bit(self, i):
        return i & (-i)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += self.low_bit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.low_bit(i)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        ranks = {num: rank + 1 for rank, num in enumerate(sorted(num_set))}
        n = len(ranks)
        res = [0] * len(nums)
        self.fw_tree = FenwickTree(n)

        for i, num in enumerate(reversed(nums)):
            res[i] = self.fw_tree.query(ranks[num] - 1)
            self.fw_tree.update(ranks[num], 1)

        return reversed(res)


# @lc code=end
