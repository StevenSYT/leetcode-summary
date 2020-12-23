#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#

# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        state = 0 # bitmask '00000' 表示全为偶数个元音
        res = 0
        for r in range(len(s)):
            vowel_idx = "aeiou".find(s[r])
            if vowel_idx >= 0:
                # 假如当前char是一个vowel 'e', 匹配得到vowel_idx = 1
                # 那么对应的bit码为00010, 这时候和state取一个异或得到当前
                # substring里元音的奇偶情况。
                state ^= (1 << vowel_idx) 
            if state in seen:
                # 如果之前出现过相同的state在位置i，
                # 那么substring [i + 1, r] 就是一个符合条件的
                # substring，这时候跟当前的最大长度比较一下。
                res = max(res, r - seen[state])
            else:
                seen[state] = r
        return res

# @lc code=end

