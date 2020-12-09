#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)
        stack = []
        op = "+"
        cur_num = 0
        i = 0

        while i < n:
            if s[i].isdigit():
                while i < n and s[i].isdigit():
                    cur_num = cur_num * 10 + int(s[i])
                    i += 1
            if i == n or s[i] in ["+", "-", "*", "/"]:
                if op == "+":
                    stack.append(cur_num)
                elif op == "-":
                    stack.append(-cur_num)
                elif op == "*":
                    tmp = stack.pop()
                    stack.append(tmp * cur_num)
                elif op == "/":
                    tmp = stack.pop()
                    stack.append(int(tmp / cur_num))
                    print(tmp, cur_num, int(tmp / cur_num))
                if i < n:
                    op = s[i]
                    cur_num = 0
                    i += 1
        return sum(stack)
# @lc code=end

