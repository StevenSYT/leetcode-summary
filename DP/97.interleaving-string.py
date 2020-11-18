#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k, cache):
            if i < 0 and j < 0 and k < 0:
                return True 
            if (i, j, k) in cache:
                return cache[i, j, k]
            if i < 0:
                cache[i, j, k] = s2[:j + 1] == s3[:k + 1]
                return cache[i, j, k]
            if j < 0:
                cache[i, j, k] = s1[:i + 1] == s3[:k + 1]
                return cache[i, j, k]
            if s1[i] == s3[k] and dfs(i-1, j, k-1, cache):
                cache[i, j, k] = True
                return True
            if s2[j] == s3[k] and dfs(i, j-1, k-1, cache):
                cache[i, j, k] = True
                return True
            cache[i, j, k] = False
            return False
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        return dfs(l1 - 1, l2 - 1, l3 - 1, {})
# @lc code=end

