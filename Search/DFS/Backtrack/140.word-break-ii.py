#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = self.dfs(s, 0, wordDict, {})
        return res

    def dfs(self, s, pos, wordDict, cache):
        if pos == len(s):
            return [""]
        if pos in cache:
            return cache[pos]
        res = []
        for word in wordDict:
            if self.beginWith(s, pos, word):
                subpaths = self.dfs(s, pos + len(word), wordDict, cache)
                for path in subpaths:
                    delimeter = " " if path else ""
                    res.append(word + delimeter + path)
        cache[pos] = res
        return res

    def beginWith(self, s, pos, target):
        return s[pos:pos + len(target)] == target


# @lc code=end
