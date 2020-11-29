#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#

# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [False] * len(queries)
        for idx, query in enumerate(queries):
            res[idx] = self.isMatch(query, pattern)
        return res
    def isMatch(self, query, pattern):
        pos = 0
        for i in range(len(query)):
            if pos < len(pattern) and query[i] == pattern[pos]:
                pos += 1
            elif query[i].isupper():
                return False
        return pos == len(pattern)
# @lc code=end

