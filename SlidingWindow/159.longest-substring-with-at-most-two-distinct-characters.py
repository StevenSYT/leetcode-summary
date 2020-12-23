class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_cnter = collections.Counter()
        l = 0
        res = 0
        for r in range(len(s)):
            char_cnter[s[r]] += 1
            while len(char_cnter) > 2:
                char_cnter[s[l]] -= 1
                if char_cnter[s[l]] == 0:
                    del char_cnter[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res