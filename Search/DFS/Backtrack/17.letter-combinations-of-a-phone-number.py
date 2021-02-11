#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_to_chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []
        self.dfs('', key_to_chars, digits, res)
        return res
        
    def dfs(self, path, key_to_chars, digits, res):
        if not digits:
            if path:
                res.append(path)
            return
        
        for ch in key_to_chars[digits[0]]:
            self.dfs(path + ch, key_to_chars, digits[1:], res)
        
# @lc code=end

