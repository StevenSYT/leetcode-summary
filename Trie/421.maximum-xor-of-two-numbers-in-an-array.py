#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#


# @lc code=start
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, num):
        node = self.root
        result = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in node:
                result = (result << 1) + 1
                node = node[1 - bit]
            else:
                result = (result << 1) + 0
                node = node[bit]
        return result


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)

        res = 0
        for num in nums:
            res = max(res, trie.query(num))

        return res


# @lc code=end
