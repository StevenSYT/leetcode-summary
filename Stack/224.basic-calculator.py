#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []

        i = 0
        cur_num = 0
        sign = 1
        res = 0
        n = len(s)

        while i < n:
            if s[i].isdigit():
                while i < n and s[i].isdigit():
                    cur_num = cur_num * 10 + int(s[i])
                    i += 1
                res += cur_num * sign
                cur_num = 0
                sign = 1
            else:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    # Note that the sign that gets pushed in the stack
                    # is actually the sign of the parenthesis.
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif s[i] == ")":
                    res *= stack.pop()
                    res += stack.pop()
                i += 1
        return res


# @lc code=end

