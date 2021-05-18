#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
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
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sum_set = {0, -lower, -upper}
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
            sum_set.add(sums[-1])
            sum_set.add(sums[-1] - lower)
            sum_set.add(sums[-1] - upper)
        
        ranks = {s: rank + 1 for rank, s in enumerate(sorted(sum_set))}
        n = len(ranks)
        self.fw_tree = FenwickTree(n)
        
        res = 0
        for s in sums:
            res += self.fw_tree.query(ranks[s - lower]) - self.fw_tree.query(ranks[s - upper] - 1)
            
            self.fw_tree.update(ranks[s], 1)
        
        return res
# @lc code=end

