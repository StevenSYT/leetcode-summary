#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        word_freqs = Counter(s)
        res = 0
        for ch in word_freqs.keys():
            if word_freqs[ch] < k:
                for sub_str in s.split(ch):
                    res = max(res, self.longestSubstring(sub_str, k))
                return res
        return len(s)
        
# @lc code=end

