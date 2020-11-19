#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def buildCharDict(s):
            d = {ch : 0 for ch in string.ascii_lowercase}
            for ch in s:
                d[ch] += 1
            return d
        l, r = 0, len(p) - 1
        cnt_s, cnt_p = buildCharDict(s[:r+1]), buildCharDict(p)
        res = []
        while r < len(s):
            if cnt_s == cnt_p:
                res.append(l)
            cnt_s[s[l]] -= 1
            l += 1
            r += 1
            if r < len(s):
                cnt_s[s[r]] += 1
        return res
        
# @lc code=end

