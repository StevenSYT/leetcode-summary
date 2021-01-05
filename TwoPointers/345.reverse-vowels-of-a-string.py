#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        chars = [ch for ch in s]
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
                continue
            if chars[l] not in vowels:
                l += 1
            if chars[r] not in vowels:
                r -= 1
        return ''.join(chars)


# @lc code=end
