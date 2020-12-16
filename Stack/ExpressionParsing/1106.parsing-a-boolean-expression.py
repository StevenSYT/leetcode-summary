#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#


# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        op = expression[0]
        if op == "t":
            return True
        elif op == "f":
            return False
        elif op == "!":
            return not self.parseBoolExpr(expression[2:-1])
        elif op == "&":
            sub_exps = self.getSubExps(expression[2:-1])
            return all([self.parseBoolExpr(exp) for exp in sub_exps])
        elif op == "|":
            sub_exps = self.getSubExps(expression[2:-1])
            return any([self.parseBoolExpr(exp) for exp in sub_exps])

    def getSubExps(self, s):
        sub_exps = []
        start = 0
        p_cnt = 0
        for i in range(start, len(s)):
            if s[i] == "," and p_cnt == 0:
                sub_exps.append(s[start:i])
                start = i + 1
            if s[i] == "(":
                p_cnt += 1
            if s[i] == ")":
                p_cnt -= 1
        sub_exps.append(s[start:])
        return sub_exps


# @lc code=end
