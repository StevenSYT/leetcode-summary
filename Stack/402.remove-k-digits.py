#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"
        stack = []
        count = 0
        for ch in num:
            if count < k:
                while stack and stack[-1] > ch and count < k:
                    count += 1
                    stack.pop()
            stack.append(ch)
        res = str(int("".join(stack[:n - k])))
        return res if res else "0"
            
# @lc code=end

