#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#


# @lc code=start
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        op_stack = []
        val_stack = []
        exp = expression[0]
        for i in range(1, len(expression)):
            if expression[i] == ",":
                exp += "+"
                continue
            if expression[i] == "{":
                prev = expression[i - 1]
                if prev == "}" or prev.isalpha():
                    exp += "*"
            if expression[i].isalpha() and expression[i - 1] == "}":
                exp += "*"
            exp += expression[i]

        i = 0
        while i < len(exp):
            if exp[i] == "{":
                op_stack.append(exp[i])
            elif exp[i].isalpha():
                val = ''
                while i < len(exp) and exp[i].isalpha():
                    val += exp[i]
                    i += 1
                val_stack.append([val])
                i -= 1
            elif exp[i] == "}":
                while op_stack and op_stack[-1] != "{":
                    op = op_stack.pop()
                    val2 = val_stack.pop()
                    val1 = val_stack.pop()
                    val_stack.append(self.applyOp(val1, val2, op))
                op_stack.pop()
            # operators ("*" or "+")
            else:
                while op_stack and self.priority(
                        op_stack[-1]) >= self.priority(exp[i]):
                    # Process operator with higher priority
                    op = op_stack.pop()
                    val2 = val_stack.pop()
                    val1 = val_stack.pop()
                    val_stack.append(self.applyOp(val1, val2, op))
                op_stack.append(exp[i])
            i += 1

        while op_stack:
            op = op_stack.pop()
            val2 = val_stack.pop()
            val1 = val_stack.pop()
            val_stack.append(self.applyOp(val1, val2, op))
        return sorted(set(val_stack[-1]))

    # Return priority of the op, the larger the number, the higher.
    def priority(self, op):
        if op == "*":
            return 2
        if op == "+":
            return 1
        return 0

    # a and b are input lists.
    def applyOp(self, a, b, op):
        if op == "+":
            return a + b
        if op == "*":
            return [c1 + c2 for c1 in a for c2 in b]


# @lc code=end
