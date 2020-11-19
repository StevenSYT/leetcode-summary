#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j, cache):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if (i, j) in cache:
                return cache[i, j]
            if word1[i] == word2[j]:
                cache[i, j] = dfs(i - 1, j - 1, cache)
                return cache[i, j]
            cache[i, j] = 1 + min(dfs(i, j - 1, cache), dfs(i - 1, j, cache),
                                  dfs(i - 1, j - 1, cache))
            return cache[i, j]
        return dfs(len(word1) - 1, len(word2) - 1, {})

# @lc code=end
